from enum import IntEnum
from utils import ContainsEnumMeta


class SurfaceGroup(IntEnum, metaclass=ContainsEnumMeta):
    General = 1
    Trainer = 2
    DriveMode = 3
    ThrottleCut = 4

    MOA = 7
    IdleUp = 8
    Traction = 9
    ABS = 10
    AVC = 11
    ROSS = 12
    Dual = 13

    Analog = 100
    Digital = 101
    Trim = 102
    Servo = 103
    Expo = 105
    PMix = 106
    Sequencer = 107
    Tweak = 108
    CenterReport = 109
    Roller = 110
    Rates = 111
    VirtualSwitch = 112
    AWS = 113
    ChannelCurve = 114
    RMD = 115

    Identification = 208
    Status = 209
    Calibration = 210

    DebugMemoryAccess = 211

    Unknown = 255

    def sub_group(self, id):
        if self == SurfaceGroup.General:
            return GeneralCP.name_of(id)
        elif self == SurfaceGroup.Trainer:
            return Trainer.name_of(id)
        elif self == SurfaceGroup.DriveMode:
            return DriveMode.name_of(id)
        elif self == SurfaceGroup.ThrottleCut:
            return ThrottleCut.name_of(id)

        elif self == SurfaceGroup.MOA:
            return MOA.name_of(id)
        elif self == SurfaceGroup.IdleUp:
            return IdleUp.name_of(id)
        elif self == SurfaceGroup.Traction:
            return Traction.name_of(id)
        elif self == SurfaceGroup.ABS:
            return ABS.name_of(id)
        elif self == SurfaceGroup.AVC:
            return AVC.name_of(id)
        elif self == SurfaceGroup.ROSS:
            return ROSS.name_of(id)
        elif self == SurfaceGroup.Dual:
            return Dual.name_of(id)

        elif self == SurfaceGroup.Analog:
            return Analog.name_of(id)
        elif self == SurfaceGroup.Digital:
            return Digital.name_of(id)
        elif self == SurfaceGroup.Trim:
            return Trim.name_of(id)
        elif self == SurfaceGroup.Servo:
            return Servo.name_of(id)
        elif self == SurfaceGroup.Expo:
            return Expo.name_of(id)
        elif self == SurfaceGroup.PMix:
            return PMix.name_of(id)
        elif self == SurfaceGroup.Sequencer:
            return Sequencer.name_of(id)
        elif self == SurfaceGroup.Tweak:
            return Tweak.name_of(id)
        elif self == SurfaceGroup.CenterReport:
            return CenterReport.name_of(id)
        elif self == SurfaceGroup.Roller:
            return Roller.name_of(id)
        elif self == SurfaceGroup.Rates:
            return Rates.name_of(id)
        elif self == SurfaceGroup.VirtualSwitch:
            return VirtualSwitch.name_of(id)
        elif self == SurfaceGroup.AWS:
            return AWS.name_of(id)
        elif self == SurfaceGroup.ChannelCurve:
            return ChannelCurve.name_of(id)
        elif self == SurfaceGroup.RMD:
            return RMD.name_of(id)

        elif self == SurfaceGroup.Identification:
            return Identification.name_of(id)
        elif self == SurfaceGroup.Status:
            return StatusInfo.name_of(id)
        elif self == SurfaceGroup.Calibration:
            return Calibration.name_of(id)

        return f'0x{id:02X}'


class SurfaceDevID(IntEnum, metaclass=ContainsEnumMeta):
    INHIBIT = 0

    SERVO_STR = 1
    SERVO_THR = 2
    SERVO_AUX1 = 3
    SERVO_AUX2 = 4
    SERVO_AUX3 = 5
    SERVO_AUX4 = 6
    SERVO_AUX5 = 7

    CHAN_OUT_STR = 32
    CHAN_OUT_THR = 33
    CHAN_OUT_AUX1 = 34
    CHAN_OUT_AUX2 = 35
    CHAN_OUT_AUX3 = 36
    CHAN_OUT_AUX4 = 37
    CHAN_OUT_AUX5 = 38

    # --- Analog IDs --- #
    WHEEL_STICK = 64
    THROTTLE_STICK = 65
    KNOB = 66

    # --- Switches --- #
    SWITCH_E = 82
    SWITCH_H = 83
    SWITCH_I = 84
    SWITCH_LEFT = 85  # Left Button
    SWITCH_RIGHT = 86  # Right Button
    SWITCH_TRAINER = 87
    # Defines a switch that is always at Position 1.
    # Used to set a mix that is always enabled.
    SWITCH_ALWAYS_POS1 = 88

    # --- Extended Trims --- #
    TRIM_A_EX = 91
    TRIM_B_EX = 92
    TRIM_C_EX = 93
    TRIM_D_EX = 94
    TRIM_F_EX = 95
    TRIM_G_EX = 96
    TRIM_V_1_EX = 97
    TRIM_V_2_EX = 98
    TRIM_V_3_EX = 99
    TRIM_V_4_EX = 100
    TRIM_V_5_EX = 101
    TRIM_V_6_EX = 102
    TRIM_V_7_EX = 103
    TRIM_V_8_EX = 104
    TRIM_ROLLER_EX = 105

    # --- Trims --- #
    TRIM_A = 108
    TRIM_B = 109
    TRIM_C = 110
    TRIM_D = 111
    TRIM_F = 112
    TRIM_G = 113
    TRIM_V_1 = 114
    TRIM_V_2 = 115
    TRIM_V_3 = 116
    TRIM_V_4 = 117
    TRIM_V_5 = 118
    TRIM_V_6 = 119
    TRIM_V_7 = 120
    TRIM_V_8 = 121
    TRIM_ROLLER = 122

    # --- Rates --- #
    RATES_WHEEL = 128
    RATES_THROTTLE = 129

    # --- Expos --- #
    EXPO_WHEEL = 130
    EXPO_THROTTLE = 131

    # --- Soft Switches --- #
    SOFT_SWITCH_KNOB_L = 132
    SOFT_SWITCH_KNOB_R = 133
    SOFT_SWITCH_LEVER_L = 134
    SOFT_SWITCH_LEVER_R = 135
    SOFT_SWITCH_TRIMMER_L = 136
    SOFT_SWITCH_TRIMMER_R = 137
    SOFT_SWITCH_TRAINER = 138
    SOFT_SWITCH_F_MODE = 139
    SOFT_SWITCH_GEAR = 140
    SOFT_SWITCH_AUX2 = 141
    SOFT_SWITCH_FLAP = 142
    SOFT_SWITCH_GOV = 143
    SOFT_SWITCH_HOLD = 144

    DRIVE_MODE = 145

    # --- Mixes (User-Defined) --- #
    PMIX_1 = 146
    PMIX_2 = 147
    PMIX_3 = 148
    PMIX_4 = 149
    PMIX_5 = 150
    PMIX_6 = 151
    PMIX_7 = 152
    PMIX_8 = 153
    PMIX_9 = 154
    PMIX_10 = 155
    PMIX_11 = 156
    PMIX_12 = 157
    PMIX_13 = 158
    PMIX_14 = 159
    PMIX_15 = 160
    PMIX_16 = 161
    PMIX_17 = 162
    PMIX_18 = 163
    PMIX_19 = 164
    PMIX_20 = 165
    PMIX_21 = 166
    PMIX_22 = 167
    PMIX_23 = 168
    PMIX_24 = 169

    CRV_MIXER_STR = 175
    CRV_MIXER_THR = 176

    # --- Built-In Mixes --- #
    MIX_AWS = 177
    MIX_MOA = 178
    MIX_AVC_STR = 179
    MIX_AVC_THR = 180
    MIX_DUAL_BRK = 181
    MIX_IDLE_UP = 183
    MIX_DUAL_ST = 184
    MIX_DUAL_THR = 185
    MIX_ROSS = 186

    AWS_MIX_DM_1 = 190
    AWS_MIX_DM_2 = 191
    AWS_MIX_DM_3 = 192
    AWS_MIX_DM_4 = 193
    AWS_MIX_DM_5 = 194

    SWITCH_V00 = 200
    SWITCH_V01 = 201
    SWITCH_V02 = 202
    SWITCH_V03 = 203
    SWITCH_V04 = 204
    SWITCH_V05 = 205
    SWITCH_V06 = 206
    SWITCH_V07 = 207
    SWITCH_V08 = 208
    SWITCH_V09 = 209
    SWITCH_V10 = 210
    SWITCH_V11 = 211
    SWITCH_V12 = 212
    SWITCH_V13 = 213
    SWITCH_V14 = 214
    SWITCH_V15 = 215

    SW_CLEAR = 224
    SW_BACK = 225
    SW_ROLLER = 226

    SEQUENCER_1 = 232
    SEQUENCER_2 = 233
    SEQUENCER_3 = 234
    SEQUENCER_4 = 235
    SEQUENCER_5 = 236

    SEQUENCER_1_B = 240
    SEQUENCER_2_B = 241
    SEQUENCER_3_B = 242
    SEQUENCER_4_B = 243
    SEQUENCER_5_B = 244

    SW_COMBO = 253

    MAX = 0xFE


class GeneralCP(IntEnum, metaclass=ContainsEnumMeta):
    ModelType = 1
    ModelSubTypeA = 2
    ModelSubTypeB = 3
    ModelSubTypeC = 4
    FrameRate = 5
    GeneralTrimMode = 6
    ThrottleTrimReverse = 7
    ModelSubTypeD = 8
    TrimTypeMask = 9
    RFAllowMask = 10
    SoftSwitch = 11
    TrimId = 12
    DModeAnalog = 13
    ModelMatchID = 14
    ModelSaveTimeout = 15
    ModelSaveDelta = 16


class Trainer(IntEnum, metaclass=ContainsEnumMeta):
    Type = 1
    ConditionID = 2
    MixOrNormal = 3
    MixRatio = 4
    DestSlot = 5
    ConditionID_F = 6
    MasterOverride = 7
    ActivePositions = 8
    Wireless = 9


class DriveMode(IntEnum, metaclass=ContainsEnumMeta):
    Switch = 1
    SwitchA = 1
    SwitchB = 2
    SwitchC = 3
    SwitchD = 4
    PriorityMode = 5
    OutputTable = 6
    ActivePositions = 7
    PriorityModeActivePositions = 8
    REC_DriveModeTable = 128


class ThrottleCut(IntEnum, metaclass=ContainsEnumMeta):
    ConditionID = 1
    Percent = 2
    RampSpeed = 3
    ActivePositions = 4


class MOA(IntEnum, metaclass=ContainsEnumMeta):
    ConditionId = 1
    OtfId = 2
    ActivePositions = 3
    RearRate = 4


class IdleUp(IntEnum, metaclass=ContainsEnumMeta):
    ActivePositions = 1
    OtfId = 2
    ConditionId = 2
    Value = 3


class Traction(IntEnum, metaclass=ContainsEnumMeta):
    ConditionID = 1
    OTFId = 2
    ActivePositions = 3
    CutoffPct = 4
    RampRate = 5


class ABS(IntEnum, metaclass=ContainsEnumMeta):
    AbsConditionID = 1
    AbsActivePositions = 2
    AbsPulses = 3
    AbsPoint = 4
    AbsWidth = 5
    AbsDelay = 6
    REC_SurfABS = 128


class AVC(IntEnum, metaclass=ContainsEnumMeta):
    AvcActivePositions = 1
    AvcConditionId = 2
    AvcSteeringGainOTFId = 3
    AvcSteeringGainValue = 4
    AvcThrottleGainOTFId = 5
    AvcThrottleGainValue = 6
    AvcSteeringPriorityOTFId = 7
    AvcSteeringPriorityValue = 8
    REC_SurfAVC = 128
    REC_SurfAVCCfg = 129


class ROSS(IntEnum, metaclass=ContainsEnumMeta):
    RossActivePositions = 1
    ROSSOTFId = 2
    RossConditionID = 2


class Dual(IntEnum, metaclass=ContainsEnumMeta):
    DualSteeringOn = 1
    DualThrottleOn = 2
    DualBrakeOn = 3


class Analog(IntEnum, metaclass=ContainsEnumMeta):
    AdcValue = 1
    Pos0 = 2
    Pos1 = 3
    Pos2 = 4
    REC_AnalogInputs = 128


class Digital(IntEnum, metaclass=ContainsEnumMeta):
    AdcValue = 1
    Pos0 = 2
    Pos1 = 3
    Pos2 = 4
    SwitchIsToggle = 5
    REC_DigitalInputs = 128


class Trim(IntEnum, metaclass=ContainsEnumMeta):
    InputDataAdcValue = 1
    InputDataPos0 = 2
    InputDataPos1 = 3
    InputDataPos2 = 4
    Clicks = 5
    MaxClicks = 6
    CurrentValue = 7
    OutputValue = 7
    StepSize = 8
    Repeat = 9
    NextRepeat = 10
    RepeatReload = 11
    NextRepeatReload = 12
    NextDelta = 13
    MinRepeat = 14
    CommonMode = 15
    Mode = 15
    IncrementMask = 16
    DecrementMask = 17
    Control = 18
    Ctrl = 18
    Steps = 19
    REC_TrimMask = 128
    REC_INPUT_TRIM = 129


class Servo(IntEnum, metaclass=ContainsEnumMeta):
    SourceId = 1
    ConditionId = 2
    ActivePositions = 3
    Speed = 4
    SpeedDown = 5
    SpeedMode = 6
    Position = 7
    SubTrim = 8
    TravelLimitHigh = 9
    TravelLimitLow = 10
    Reverse = 11
    Name = 12
    Pulse = 13
    AbsLimitHigh = 14
    AbsLimitLow = 15
    SpeedOutputValue = 16
    VSource = 17
    AS3XFlags = 18
    TrimId = 19
    UseManualName = 20
    NameShort = 21
    NameLong = 22
    BalancePoints = 23
    BalanceX = 24
    BalanceY = 25
    SpeedOTFId = 26
    REC_ServoSpeed = 128
    REC_Servo = 129


class Expo(IntEnum, metaclass=ContainsEnumMeta):
    AnalogID = 1
    ConditionID = 2
    ActivePositions = 3
    OTFId = 4
    High = 5
    Low = 6
    AssignedCurve = 7
    REC_ExpoRates = 128


class PMix(IntEnum, metaclass=ContainsEnumMeta):
    AnalogID = 1
    ConditionID = 2
    TrimID = 3
    OutChan = 4
    ActivePositions = 5
    SwitchIsToggle = 5
    ToggleState = 5
    ComboConditionID1 = 6
    ComboConditionID2 = 7
    ComboRelation = 8
    ComboActivePositions1 = 9
    ComboActivePositions2 = 10
    CurvePoints = 11
    CurveX = 12
    CurveY = 13
    Name = 14
    REC_PMix = 128
    REC_PMixActivation = 129


class Sequencer(IntEnum, metaclass=ContainsEnumMeta):
    ConditionID = 1
    ConditionID1 = 2
    ActivePositions1 = 3
    ActivePositions = 4
    ActivePositionsReverse = 5
    Speed = 6
    SpeedReverse = 7
    TripPosition = 8
    TripPositionRev = 9
    TarA = 10
    TarB = 11
    TarRevA = 12
    TarRevB = 13
    OutPos = 14
    OutPosRev = 15
    StepsActive = 16
    SpeedOutputValue = 17
    TextA = 18
    TextB = 19
    OutModeA = 20
    OutModeB = 21
    TripLow = 22
    TripHigh = 23
    ShortNameA = 24
    ShortNameB = 25


class Tweak(IntEnum, metaclass=ContainsEnumMeta):
    SourceID = 1
    Active = 2
    ControlMask = 3


class CenterReport(IntEnum, metaclass=ContainsEnumMeta):
    Alarm = 1
    Action = 2


class Roller(IntEnum, metaclass=ContainsEnumMeta):
    ConditionID = 1
    ActivePositions = 2
    Position = 3
    StepSize = 4
    Raw = 5


class Rates(IntEnum, metaclass=ContainsEnumMeta):
    RateConditionId = 1
    RateActivePositions = 2
    Rate0 = 3
    Rate1 = 3
    SteeringRateOTFId = 5
    SteeringOverrideOTFId = 6
    SteeringOverrideRate = 7
    REC_ChannelRate = 128


class VirtualSwitch(IntEnum, metaclass=ContainsEnumMeta):
    CurrentPosition = 1
    Value = 2
    REC_VirtSwitchValues = 128


class AWS(IntEnum, metaclass=ContainsEnumMeta):
    ActivePositions = 1
    ConditionID = 2
    Left = 3
    Right = 4
    Mode = 5
    Trim = 6
    REC_SurfAWS = 128


class ChannelCurve(IntEnum, metaclass=ContainsEnumMeta):
    AnalogID = 1
    ConditionID = 2
    ActivePositions = 3
    TrimmerID = 4
    AssignedCurve = 5
    Rate = 6
    CurvePoints = 7
    CurveX = 8
    CurveY = 9
    TrimActiveMask = 10
    Delay = 11
    MixName = 12
    REC_ChannelCurve = 128


class RMD(IntEnum, metaclass=ContainsEnumMeta):
    CPMisc = 1
    Servos1 = 2
    Servos2 = 3
    Servos3 = 4
    Servos4 = 5
    Curve1Part1 = 6
    Curve1Part2 = 7
    Curve2Part1 = 8
    Curve2Part2 = 9
    Expo = 10
    SurfMisc = 11
    Trims1 = 12
    Trims2 = 13
    Trims3 = 14
    PMixs1 = 15
    PMixs2 = 16
    EnablesAlarms = 17
    ChanOverrides = 18


class Identification(IntEnum, metaclass=ContainsEnumMeta):
    SerialNumber = 1
    ParameterCRC = 2
    ProductCode = 3
    FirmwareMajorVersion = 4
    FirmwareMinorVersion = 5
    FirmwareBuildVersion = 6
    RFPID = 7
    SystemRegion = 8
    BootloaderVersion = 9


class StatusInfo(IntEnum, metaclass=ContainsEnumMeta):
    BindStatus = 1
    BindType = 2
    AllChannelMonitorData = 3
    GlueData = 4
    OutputValue = 7
    DevicePosition = 8
    AllChannelMonitorDataEx = 9
    RuntimeMonitorStatus = 10


class Calibration(IntEnum, metaclass=ContainsEnumMeta):
    Calibration = 3


class SurfRuntimeData:
    def __init__(self):

        self.channels = []
        """
        Size: 6 channels
        Format: 16 bits unsigned int (ushort)
        Description: [STR, THR, AUX1, AUX2, AUX3, AUX4]
        """

        self.extra = []
        """
        Size: 10 channels
        Format: 16 bits unsigned int (ushort)
        Description: Unused
        """

        self.inputs = []
        """
        Size: 3 Channels
        Format: 16 bits signed int (short)
        Description: [WheelInput, ThrottleInput, KnobJInput]
        """

    @staticmethod
    def parse(data):
        surf = SurfRuntimeData()
        for i in range(0, 6):
            if len(data) > (i * 2) + 1:
                surf.channels.append(int((data[i*2] << 8) + data[i*2+1]) & 0xffff)

        for i in range(0, 3):
            if len(data) > (i * 2) + 31:
                surf.inputs.append(int((data[(i * 2) + 30] << 8)) + int(data[(i * 2) + 31]))

        print(surf)

        return surf

    def __str__(self):
        return f"[{', '.join([str(c) for c in self.channels])}] [{', '.join([str(i) for i in self.inputs])}]"
