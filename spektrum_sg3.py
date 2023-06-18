# This HLA takes a stream of bytes and attempts to decode it as a Spektrum Bootloader message or
# a Spektrum SG3 UART message.
# It only supports Async Serial analyzers

from surface import SurfaceGroup, SurfaceDevID, SurfRuntimeData
from air import AirGroup, AirDevID
from enum_types import *
import sax

# Settings constants.
from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting
from saleae.data import GraphTimeDelta, GraphTime

SURFACE = 'Surface Raio'
AIR = 'Air Radio'


class SG3Packet:
    def __init__(self, hla):
        self.hla = hla
        self.raw_data = []
        self.data = []
        self.count = 0
        self.message_id = 0
        self.message_type = None
        self.checksum = []
        self.state = State.Pending
        self.start_time = 0
        self.end_time = 0
        self.prev_frame_time = None
        self.current_frame_time = None
        self.escaped = False
        self.event_type = None
        self.telemetry_type = None
        self.bl_command = None

    def reset(self, msg=None):
        self.state = State.Pending
        self.start_time = 0
        self.end_time = 0
        self.message_id = 0
        self.message_type = None
        self.checksum = []
        self.raw_data = []
        self.data = []
        self.count = 0
        if msg is not None:
            print(msg)

    def next(self, frame, val):
        self.prev_frame_time = self.current_frame_time
        self.current_frame_time = frame.end_time
        self.count += 1

        if self.state in [State.Data, State.BlData]:
            self.raw_data.append(val)

        if val == ESCAPE:
            self.escaped = True
            return

        if self.escaped:
            self.escaped = False
            val += OFFSET

        elif self.state == State.Pending:
            if val == START_BYTE:
                self.state = State.Started
                self.start_time = frame.start_time
            elif val in [ACK, NAK]:
                self.state = State.StartAckNak
                self.start_time = frame.start_time
                self.message_type = SG3MessageType.ACK if val == ACK else SG3MessageType.NAK
            elif val == BL_HEADER_BYTE:
                self.state = State.BlHeaderBegin
                self.start_time = frame.start_time
                self.message_type = SG3MessageType.BL_MESSAGE

        elif self.state == State.Started:
            self.message_id = val - OFFSET
            self.state = State.FoundId

        elif self.state == State.FoundId:
            if val == BEGIN_DATA_BYTE:
                self.state = State.Data
            else:
                self.reset(f'Expected BEGIN_DATA_BYTE (0x{BEGIN_DATA_BYTE:02X}), but got 0x{val:02X}')

        elif self.state == State.Data:
            if val == END_DATA_BYTE:
                self.state = State.Checksum
            elif self.message_type is None:
                self.message_type = val - OFFSET
            elif self.message_type == SG3MessageType.EVENT and self.event_type is None:
                self.event_type = val - OFFSET
            elif self.message_type == SG3MessageType.TELEMETRY and self.telemetry_type is None:
                self.telemetry_type = val - OFFSET
            else:
                self.data.append(val - OFFSET)

        elif self.state == State.Checksum:
            if val == END_MESSAGE_BYTE:
                self.state = State.Complete
                self.end_time = frame.end_time
            else:
                self.checksum.append(val)

        elif self.state == State.Complete:
            if val == EMPTY_BYTE:
                self.end_time = frame.end_time

        elif self.state == State.StartAckNak:
            self.message_id = val - OFFSET
            self.state = State.AckNakId

        elif self.state == State.AckNakId:
            if val == END_MESSAGE_BYTE:
                self.state = State.Complete
                self.end_time = frame.end_time
            else:
                self.reset(f'Expected END_MESSAGE_BYTE (0x{END_MESSAGE_BYTE:02X}), but got 0x{val:02X}')

        elif self.state == State.BlHeaderBegin:
            if val == BL_HEADER_BYTE:
                self.state = State.BlHeaderEnd
            else:
                self.reset(f'Expected BL_HEADER_BYTE (0x{BL_HEADER_BYTE:02X}), but got 0x{val:02X}')

        elif self.state == State.BlHeaderEnd:
            self.bl_command = val
            self.state = State.BlFoundCommand

        elif self.state == State.BlFoundCommand:
            if val == BL_HEADER_END:
                self.state = State.BlData
            else:
                self.reset(f'Expected BL_HEADER_END (0x{BL_HEADER_END:02X}), but got 0x{val:02X}')

        elif self.state == State.BlData:
            self.data.append(val)
            # todo: this should be based on the blchecksum or timeout
            if self.bl_command in [1, 3, 4, 5, 6, 7, 8, 9, BLCommand.CABLE_ACK]:
                if self.count >= 524:
                    self.state = State.BlChecksum
            elif self.count >= 75:
                self.state = State.BlChecksum

        elif self.state == State.BlChecksum:
            self.checksum.append(val)
            if len(self.checksum) == 2:
                self.state = State.Complete
                self.end_time = frame.end_time

                if self.bl_command == BLCommand.ID_RESPONSE:
                    print("ID_RESPONSE:", end=' ')
                    self.data_at_offset(0x22)
                    self.data_at_offset(0x23)
                    self.data_at_offset(0x24)
                    self.data_at_offset(0x25)
                    self.data_at_offset(0x2e)
                    self.data_at_offset(0x2f)
                    self.data_at_offset(0x30)
                    self.data_at_offset(0x3a)
                    self.data_at_offset(0x3f)
                    print()

                # if self.valid or len(self.raw_data) > 75:
                #
                # else:
                #     # checksum wasn't ready yet, data must be larger, so put checksum back into raw_data
                #     # and clear checksum
                #     self.raw_data.extend(self.checksum)
                #     self.checksum = []
                #     self.state = State.BlData

        # reset count if we are still pending
        if self.state == State.Pending:
            self.count = 0

    def normalized_type(self):
        return self.message_type - SG3_RESPONSE_OFFSET if self.is_response() else self.message_type

    def payload(self):
        if self.message_type in [SG3MessageType.READ_FIELD_RESPONSE, SG3MessageType.WRITE_FIELD]:
            return self.data[5:5+self.data[4]]  # data[4] is length
        return self.data[5:]

    def data_at_offset(self, offset):
        # subtract 4 because of header is included in the offset
        print(f'id[0x{offset:02x}]=0x{self.data[offset-4]:02x}', end=' ')

    def __str__(self):
        return f'ID: 0x{self.message_id:02X}, Type: {self.type_str()} (0x{self.message_type:02X})'

    @property
    def started(self) -> bool:
        return self.state != State.Pending

    def _compute_checksum(self):
        c = CHECKSUM_SEED
        for x in self.raw_data:
            c += x
            c &= 0xffff
        return c

    @property
    def valid(self) -> bool:
        # todo: this does not work properly yet!
        cc = self._compute_checksum()
        # if len(self.checksum) == 2:
        #     print(f'cc: 0x{cc:04X}, self.checksum: {self.checksum}, compute: 0x{(self.checksum[0] << 8) + self.checksum[1]:04X}')
        return len(self.checksum) == 2 and cc == ((self.checksum[1] << 8) + self.checksum[0])

    def type_str(self):
        if self.message_type is None:
            return 'Unknown'
        elif self.message_type == SG3MessageType.BL_MESSAGE:
            if self.bl_command in BLCommand:
                return 'BL_' + BLCommand(self.bl_command).name
            elif self.bl_command - BL_RESPONSE_OFFSET in BLCommand:
                return 'BL_' + BLCommand(self.bl_command - BL_RESPONSE_OFFSET).name.replace('_REQUEST', '') + '_RESPONSE'
            return 'BL_' + BLCommand(self.bl_command).name if self.bl_command in BLCommand else f'BL_COMMAND_0x{self.bl_command:02X}'
        elif self.message_type == SG3MessageType.EVENT:
            return SG3EventType(self.event_type).name if self.event_type in SG3EventType else f'EVENT_0x{self.event_type:02X}'
        elif self.message_type == SG3MessageType.TELEMETRY:
            return f'TELEM_0x{self.telemetry_type:02X}'
        elif self.message_type == SG3MessageType.FORWARD_PROGRAMMING:
            return f'FWD_PGM'  # todo: additional data/types?
        elif self.message_type in SG3MessageType:
            return SG3MessageType(self.message_type).name
        elif self.message_type - SG3_RESPONSE_OFFSET in SG3MessageType:
            return SG3MessageType(self.message_type - SG3_RESPONSE_OFFSET).name + '_RESPONSE'
        return f'Unknown_0x{self.message_type:02X}'

    def field_id(self):
        if self.hla.radio_type == SURFACE:
            return self.surf_field_id()
        else:
            return self.air_field_id()

    def surf_field_id(self):
        fid = SurfaceGroup.name_of(self.data[0])
        if self.data[1] != 0:
            fid += f'[{SurfaceDevID.name_of(self.data[1])}]'
        fid += '.'
        if self.data[0] in SurfaceGroup:
            fid += SurfaceGroup(self.data[0]).sub_group(self.data[2])
        else:
            fid += f'0x{self.data[2]:02X}'
        if len(self.data) > 3 and self.data[3] != 0:
            fid += f'[{SurfaceDevID.name_of(self.data[3])}]'
        return fid

    def air_field_id(self):
        fid = AirGroup.name_of(self.data[0])
        if self.data[1] != 0:
            fid += f'[{AirDevID.name_of(self.data[1])}]'
        fid += '.'
        if self.data[0] in AirGroup:
            fid += AirGroup(self.data[0]).sub_group(self.data[2])
        else:
            fid += f'0x{self.data[2]:02X}'
        if len(self.data) > 3 and self.data[3] != 0:
            fid += f'[{AirDevID.name_of(self.data[3])}]'
        return fid

    def dev_id(self, id):
        if self.hla.radio_type == SURFACE:
            return SurfaceDevID.name_of(id)
        else:
            return AirDevID.name_of(id)

    def analyzer_frame(self):
        frame_data = {}
        if self.message_id != 0:
            frame_data['id'] = f'0x{self.message_id:02X}'

        if self.message_type == SG3MessageType.TELEMETRY and self.telemetry_type is not None:
            frame_data['tel'] = f'0x{self.telemetry_type:02X}'

        if self.message_type != SG3MessageType.BL_MESSAGE and self.is_response() and len(self.data) > 4:
            frame_data['sg3_err'] = SG3Error.name_of(self.data[4])

        if self.message_type == SG3MessageType.SET_RF_MODE:
            frame_data['rf_mode'] = RFMode.name_of(self.data[0])
        elif self.message_type - SG3_RESPONSE_OFFSET == SG3MessageType.SET_RF_MODE:
            frame_data['sg3_err'] = SG3Error.name_of(self.data[0])
        elif self.normalized_type() in [SG3MessageType.READ_FIELD, SG3MessageType.WRITE_FIELD]:
            frame_data['field'] = self.field_id()
            if self.is_response() or self.normalized_type() == SG3MessageType.WRITE_FIELD:
                frame_data['ascii'] = ''.join([chr(d) if 0x20 <= d <= 0x7E else '.' for d in self.payload()])  # ascii printable characters are 0x20 - 0x7E
                frame_data['payload'] = ' '.join([f'0x{d:02X}' for d in self.payload()])
        elif self.message_type == SG3MessageType.EVENT and self.event_type == SG3EventType.SurfaceRuntimeData:
            frame_data['payload'] = str(SurfRuntimeData.parse(self.data))
        elif self.message_type == SG3MessageType.EVENT and self.event_type == SG3EventType.ButtonEvent:
            frame_data['device'] = self.dev_id(self.data[1])
            frame_data['pos'] = str(self.data[2])
        elif self.message_type == SG3MessageType.EVENT and self.event_type == SG3EventType.TrimEvent:
            frame_data['device'] = self.dev_id(self.data[1])
            frame_data['direction'] = str(self.data[2])
            frame_data['steps'] = str((self.data[4] << 8) + self.data[3]) if len(self.data) > 4 else str(self.data[3])
        elif len(self.raw_data) > 0:
            if self.message_type == SG3MessageType.BL_MESSAGE and self.bl_command == BLCommand.SAX_WRITE:
                decrypt_keys = self.hla.decryption_keys()
                if decrypt_keys is not None:
                    self.data = sax.decode_sax_data(self.data, len(self.data), decrypt_keys)
                    frame_data['address'] = f'0x{sax.next_uint32(self.data):08X}'
                    print(''.join([chr(d) if 0x20 <= d <= 0x7E else '.' for d in self.data]))
            # frame_data['count'] = self.count
            frame_data['data_len'] = str(len(self.data))
            # frame_data['valid'] = self.valid
            frame_data['ascii'] = ''.join([chr(d) if 0x20 <= d <= 0x7E else '.' for d in self.data])
            frame_data['bytes'] = ' '.join([f'0x{d:02X}' for d in self.data])
            # printable characters 0x20 - 0x7E

        # if len(self.checksum) > 0:
        #     # frame_data['checksum'] = ' '.join([f'0x{c:02X}' for c in self.checksum])
        #     frame_data['valid'] = self.valid

        return AnalyzerFrame(self.type_str(), self.start_time, self.end_time, frame_data)

    def is_response(self):
        return self.message_type >= SG3_RESPONSE_OFFSET


class SpektrumSG3(HighLevelAnalyzer):
    # Extension Settings:
    packet_timeout = NumberSetting(label='Packet Timeout [s]', min_value=1E-3, max_value=1)
    radio_type = ChoicesSetting([AIR, SURFACE])

    # NOTE: The names for these do not match on purpose due to the way Logic2 sorts the setting fields
    decryption_key_d = StringSetting(label='Decryption Key A (Optional)')
    decryption_key_c = StringSetting(label='Decryption Key B (Optional)')
    decryption_key_b = StringSetting(label='Decryption Key C (Optional)')
    decryption_key_a = StringSetting(label='Decryption Key D (Optional)')

    def __init__(self):
        self.packet = SG3Packet(self)

    def decryption_keys(self):
        try:
            return [int(self.decryption_key_d, 16), int(self.decryption_key_c, 16), int(self.decryption_key_b, 16), int(self.decryption_key_a, 16)]
        except Exception:
            return None

    def decode(self, frame: AnalyzerFrame):
        # This class method is called once for each frame produced by the input analyzer.
        # the "data" dictionary contents is specific to the input analyzer type.
        # all frames contain some common keys: start_time, end_time, and type.

        # This function can either return nothing, a single new frame, or an array of new frames.
        # all new frames produced are dictionaries and need to have the required keys: start_time, end_time, and type
        # in addition, protocol-specific information should be stored in the "data" key, so that they can be accessed
        # by rendering (using the format strings), by export, by the terminal view, and by the protocol
        # search results list.

        maximum_delay = GraphTimeDelta(second=self.packet_timeout or 1)

        # handle serial data
        if frame.type == "data" and "data" in frame.data.keys():
            value = frame.data["data"][0]
            if self.packet.state != State.Pending \
                    and self.packet.current_frame_time is not None \
                    and self.packet.current_frame_time + maximum_delay < frame.start_time:
                self.packet.reset('Packet timeout exceeded!')
            self.packet.next(frame, value)

            if self.packet.state == State.Complete:
                ret = self.packet.analyzer_frame()
                if self.packet.message_id != 0:
                    print(self.packet)
                self.packet = SG3Packet(self)
                return ret
