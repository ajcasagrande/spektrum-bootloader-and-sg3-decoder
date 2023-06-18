from enum import auto, IntEnum
from utils import ContainsEnumMeta


EMPTY_BYTE = 0x00
START_BYTE = 0x01
BEGIN_DATA_BYTE = 0x02
END_DATA_BYTE = 0x03
ACK = 0x06
NAK = 0x15
ESCAPE = 0x1b
END_MESSAGE_BYTE = 0x0d

BL_HEADER_BYTE = 0x48
BL_HEADER_END = 0x00
EVENT_MESSAGE_TYPE = 0x09
TELEMETRY_MESSAGE_TYPE = 0x0a
FORWARD_PROGRAMMING_TYPE = 0x0b

OFFSET = 0x20
SG3_RESPONSE_OFFSET = 0x80  # amount added to SG3 commands to get the response type
BL_RESPONSE_OFFSET = 0x85  # amount added to BL commands to get the BL response type

CHECKSUM_SEED = 0x170


class SG3MessageType(IntEnum, metaclass=ContainsEnumMeta):
    DISCOVER = 0x01
    SG3_VERSION = 0x02
    FLASH_SAVE = 0x03
    BOOTLOAD_MODE = 0x04
    SET_RF_MODE = 0x05
    SET_PROCESSING_STATE = 0x06
    WRITE_FIELD = 0x07
    READ_FIELD = 0x08

    EVENT = 0x09
    TELEMETRY = 0x0a
    FORWARD_PROGRAMMING = 0x0b

    WRITE_FIELD_EX = 0x0c
    READ_FIELD_EX = 0x0d

    CPU_RESET = 0x25
    CM_ZAP = 0x26

    READ_FIELD_ERROR = 0x47  # todo: these are a guess
    WRITE_FIELD_ERROR = 0x48  # todo: these are a guess

    # todo: refactor out the below message types
    ACK = 0xff01            # this is a fake type, hacked to work with existing code
    NAK = 0xff02            # this is a fake type, hacked to work with existing code
    BL_MESSAGE = 0xff03     # this is a fake type, hacked to work with existing code

    # Responses
    DISCOVER_RESPONSE = DISCOVER + SG3_RESPONSE_OFFSET
    SG3_VERSION_RESPONSE = SG3_VERSION + SG3_RESPONSE_OFFSET
    FLASH_SAVE_RESPONSE = FLASH_SAVE + SG3_RESPONSE_OFFSET
    BOOTLOAD_MODE_RESPONSE = BOOTLOAD_MODE + SG3_RESPONSE_OFFSET
    SET_RF_MODE_RESPONSE = SET_RF_MODE + SG3_RESPONSE_OFFSET
    SET_PROCESSING_STATE_RESPONSE = SET_PROCESSING_STATE + SG3_RESPONSE_OFFSET
    WRITE_FIELD_RESPONSE = WRITE_FIELD + SG3_RESPONSE_OFFSET
    READ_FIELD_RESPONSE = READ_FIELD + SG3_RESPONSE_OFFSET


class BLCommand(IntEnum, metaclass=ContainsEnumMeta):
    """Bootloader commands"""

    ID_REQUEST = 0x01   # confirmed
    CABLE_SYN = 0x02    # confirmed

    CMD_0x03 = 0x03     # todo: unknown

    BIN_ERASE = 0x04    # confirmed
    BIN_WRITE = 0x05    # confirmed

    CMD_0x06 = 0x06     # todo: unknown

    SAX_ERASE = 0x07    # confirmed
    SAX_WRITE = 0x08    # confirmed

    SAX_EOF = 0x09      # todo: this is a guess / assumed

    SAX_IX_ERASE = 0xa    # confirmed
    SAX_IX_WRITE = 0xb    # confirmed

    # Responses
    ID_RESPONSE = ID_REQUEST + BL_RESPONSE_OFFSET  # confirmed
    CABLE_ACK = CABLE_SYN + BL_RESPONSE_OFFSET  # confirmed
    CMD_0x03_RESPONSE = CMD_0x03 + BL_RESPONSE_OFFSET
    BIN_ERASE_RESPONSE = BIN_ERASE + BL_RESPONSE_OFFSET  # confirmed
    BIN_WRITE_RESPONSE = BIN_WRITE + BL_RESPONSE_OFFSET  # confirmed
    CMD_0x06_RESPONSE = CMD_0x06 + BL_RESPONSE_OFFSET
    SAX_ERASE_RESPONSE = SAX_ERASE + BL_RESPONSE_OFFSET  # confirmed
    SAX_WRITE_RESPONSE = SAX_WRITE + BL_RESPONSE_OFFSET  # confirmed
    SAX_EOF_RESPONSE = SAX_EOF + BL_RESPONSE_OFFSET
    SAX_IX_ERASE_RESPONSE = SAX_IX_ERASE + BL_RESPONSE_OFFSET  # confirmed
    SAX_IX_WRITE_RESPONSE = SAX_IX_WRITE + BL_RESPONSE_OFFSET  # confirmed


class SG3Error(IntEnum, metaclass=ContainsEnumMeta):
    Success = 0
    InvalidParameters = -1
    NotInitialized = -2
    UnknownError = -3
    NoResources = -4
    DataReceiveError = -5
    Timeout = -6
    UnknownField = -7
    WriteToReadOnly = -8
    OperationFailed = -9
    NotSupported = -10
    NotSaxFile = -11
    CorruptedSaxFile = -12
    TruncatedSaxFile = -13
    InvalidSaxFileVersion = -14
    InvalidSaxFileSerial = -15
    InvalidProductCode = -16
    WriteFailed = -17
    EraseFailed = -18
    BadAppCrc = -19
    BadEraseAddress = -20
    BadWriteAddress = -21
    NoResponse = -22

    @classmethod
    def name_of(cls, item, prefix=''):
        if item >= 0:  # Anything over 0 represents bytes read, so still success
            return SG3Error.Success.name
        return cls(item).name if cls.__contains__(item) else f'{prefix}0x{item:02X}'


class SG3EventType(IntEnum, metaclass=ContainsEnumMeta):
    TrimEvent = 1
    DebugMessage = 2
    ThrottleCut = 3
    DriveModeChanged = 4
    ButtonEvent = 5
    CenterReport = 6
    SurfaceRuntimeData = 7
    AirRuntimeData = 8
    ModelSavedToFlash = 9


class State(IntEnum, metaclass=ContainsEnumMeta):
    Pending = auto()

    Started = auto()
    FoundId = auto()
    PostId = auto()
    EventType = auto()
    Data = auto()
    Checksum = auto()

    StartAckNak = auto()
    AckNakId = auto()
    DoneAckNak = auto()

    BlHeaderBegin = auto()
    BlHeaderEnd = auto()
    BlFoundCommand = auto()
    BlData = auto()
    BlChecksum = auto()

    Complete = auto()


class RFMode(IntEnum, metaclass=ContainsEnumMeta):
    OFF = 0
    RESUME = 1
    STARTBIND = 2
