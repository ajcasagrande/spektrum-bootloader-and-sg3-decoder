from enum import IntEnum
from utils import ContainsEnumMeta


class AirGroup(IntEnum, metaclass=ContainsEnumMeta):
    ProtocolVersion = 0,
    GeneralCp = 1,
    Trainer = 2,
    FlightMode = 3,
    ThrottleCut = 4,
    ThrottleCurve = 5,

    CrackRoll = 6,
    ThrottleLimiter = 7,
    ThrottleKill = 8,

    AcroFlapSys = 10,
    AcroRaeMix = 11,
    AcroRudderDiff = 12,
    AcroAilRudMix = 13,
    AcroEleFlpMix = 14,
    AcroDifferential = 15,
    AcroGyro = 16,
    AcroPitCurve = 17,
    AcroMultiEngine = 18,

    SailFlapSys = 30,
    SailRaeMix = 31,
    SAilRudderDiff = 32,
    SailAilDiff = 33,
    SailFlapDiff = 34,
    SailTipDiff = 35,
    SailFlpEleMix = 36,
    SailEleFlpMix = 37,
    SailArMix = 38,
    SailAfMix = 39,
    SailCamberMix = 40,
    SailCamberPreset = 41,
    SailCrowMix = 42,

    HeliPitCurve = 50,
    HeliTailCurve = 51,
    HeliGyro = 52,
    HeliGovernor = 53,
    HeliCyclic = 54,
    HeliSwashMix = 55,
    HeliSwashPlate = 56,
    HeliFmDelays = 57,

    MultiFlapSys = 70,
    MultiRaeMix = 71,
    MultiRudderDiff = 72,
    MultiAilRudMix = 73,
    MultiEleFlpMix = 74,
    MultiDifferential = 75,
    MultiGyro = 76,
    MultiPitCurve = 77,
    MultiChannelSet = 78,

    Analog = 100,
    Digital = 101,
    Trim = 102,
    Servo = 103,
    DrExpo = 104,
    Special = 105,
    PMix = 106,
    Sequencer = 107,
    Tweak = 108,
    CenterReport = 109,
    LogicalSwitch = 110,
    ComboSwitch = 111,
    VirtualSwitch = 112,
    AnalogTrim = 113,
    GenericCurve = 114,
    TouchInput = 115,

    CurrentModelGeneral = 140,
    CurrentModelRhythmTimer = 141,
    CurrentModelTimer = 142,
    CurrentModelAcroWarning = 143,
    CurrentModelSailWarning = 144,
    CurrentModelHeliWarning = 145,
    CurrentModelMultiWarning = 146,
    CurrentModelTelemetry = 147,
    CurrentModelFmNames = 148,
    CurrentModelPreflight = 149,
    CurrentModelVox = 150,
    CurrentModelVtx = 151,
    CurrentModelLapTimer = 152,
    CurrentModel2CpuGeneral = 153,
    CurrentModel2CpuStickWarning = 154,
    CurrentModel2CpuServoWarning = 155,
    CurrentModel2CpuSwitchWarning = 156,

    TxSystemIdentity = 170,
    TxSystemConfig = 171,
    TxSystemCalibration = 172,
    TxSystemBattery = 173,
    TxSystemDisplay = 174,
    TxSystemSounds = 175,

    ForwardProgramming = 180,

    RfModUpdate = 185,

    Identification = 208,
    StatusInfo = 209,
    CalibrationInfo = 210,
    DebugMemoryAccess = 211,
    ModelUtility = 212,
    CpUtility = 213,
    Compliance = 214,

    def sub_group(self, id):
        # if self == AirGroup.ProtocolVersion:
        #     return ProtocolVersion.name_of(id)
        if self == AirGroup.GeneralCp:
            return General.name_of(id)
        elif self == AirGroup.Trainer:
            return Trainer.name_of(id)
        # elif self == AirGroup.FlightMode:
        #     return FlightMode.name_of(id)
        # elif self == AirGroup.ThrottleCut:
        #     return ThrottleCut.name_of(id)
        elif self == AirGroup.ThrottleCurve:
            return ThrottleCurve.name_of(id)

        # elif self == AirGroup.CrackRoll:
        #     return CrackRoll.name_of(id)
        # elif self == AirGroup.ThrottleLimiter:
        #     return ThrottleLimiter.name_of(id)
        # elif self == AirGroup.ThrottleKill:
        #     return ThrottleKill.name_of(id)

        # elif self == AirGroup.AcroFlapSys:
        #     return AcroFlapSys.name_of(id)
        # elif self == AirGroup.AcroRaeMix:
        #     return AcroRaeMix.name_of(id)
        # elif self == AirGroup.AcroRudderDiff:
        #     return AcroRudderDiff.name_of(id)
        # elif self == AirGroup.AcroAilRudMix:
        #     return AcroAilRudMix.name_of(id)
        # elif self == AirGroup.AcroEleFlpMix:
        #     return AcroEleFlpMix.name_of(id)
        # elif self == AirGroup.AcroDifferential:
        #     return AcroDifferential.name_of(id)
        # elif self == AirGroup.AcroGyro:
        #     return AcroGyro.name_of(id)
        # elif self == AirGroup.AcroPitCurve:
        #     return AcroPitCurve.name_of(id)
        # elif self == AirGroup.AcroMultiEngine:
        #     return AcroMultiEngine.name_of(id)

        # elif self == AirGroup.SailFlapSys:
        #     return SailFlapSys.name_of(id)
        # elif self == AirGroup.SailRaeMix:
        #     return SailRaeMix.name_of(id)
        # elif self == AirGroup.SAilRudderDiff:
        #     return SAilRudderDiff.name_of(id)
        # elif self == AirGroup.SailAilDiff:
        #     return SailAilDiff.name_of(id)
        # elif self == AirGroup.SailFlapDiff:
        #     return SailFlapDiff.name_of(id)
        # elif self == AirGroup.SailTipDiff:
        #     return SailTipDiff.name_of(id)
        # elif self == AirGroup.SailFlpEleMix:
        #     return SailFlpEleMix.name_of(id)
        # elif self == AirGroup.SailEleFlpMix:
        #     return SailEleFlpMix.name_of(id)
        # elif self == AirGroup.SailArMix:
        #     return SailArMix.name_of(id)
        # elif self == AirGroup.SailAfMix:
        #     return SailAfMix.name_of(id)
        # elif self == AirGroup.SailCamberMix:
        #     return SailCamberMix.name_of(id)
        # elif self == AirGroup.SailCamberPreset:
        #     return SailCamberPreset.name_of(id)
        # elif self == AirGroup.SailCrowMix:
        #     return SailCrowMix.name_of(id)

        # elif self == AirGroup.HeliPitCurve:
        #     return HeliPitCurve.name_of(id)
        # elif self == AirGroup.HeliTailCurve:
        #     return HeliTailCurve.name_of(id)
        # elif self == AirGroup.HeliGyro:
        #     return HeliGyro.name_of(id)
        # elif self == AirGroup.HeliGovernor:
        #     return HeliGovernor.name_of(id)
        # elif self == AirGroup.HeliCyclic:
        #     return HeliCyclic.name_of(id)
        # elif self == AirGroup.HeliSwashMix:
        #     return HeliSwashMix.name_of(id)
        # elif self == AirGroup.HeliSwashPlate:
        #     return HeliSwashPlate.name_of(id)
        # elif self == AirGroup.HeliFmDelays:
        #     return HeliFmDelays.name_of(id)

        # elif self == AirGroup.MultiFlapSys:
        #     return MultiFlapSys.name_of(id)
        # elif self == AirGroup.MultiRaeMix:
        #     return MultiRaeMix.name_of(id)
        # elif self == AirGroup.MultiRudderDiff:
        #     return MultiRudderDiff.name_of(id)
        # elif self == AirGroup.MultiAilRudMix:
        #     return MultiAilRudMix.name_of(id)
        # elif self == AirGroup.MultiEleFlpMix:
        #     return MultiEleFlpMix.name_of(id)
        # elif self == AirGroup.MultiDifferential:
        #     return MultiDifferential.name_of(id)
        # elif self == AirGroup.MultiGyro:
        #     return MultiGyro.name_of(id)
        # elif self == AirGroup.MultiPitCurve:
        #     return MultiPitCurve.name_of(id)
        # elif self == AirGroup.MultiChannelSet:
        #     return MultiChannelSet.name_of(id)

        elif self == AirGroup.Analog:
            return AnalogAdc.name_of(id)
        # elif self == AirGroup.Digital:
        #     return Digital.name_of(id)
        # elif self == AirGroup.Trim:
        #     return Trim.name_of(id)
        # elif self == AirGroup.Servo:
        #     return Servo.name_of(id)
        # elif self == AirGroup.DrExpo:
        #     return DrExpo.name_of(id)
        elif self == AirGroup.Special:
            return Special.name_of(id)
        # elif self == AirGroup.PMix:
        #     return PMix.name_of(id)
        # elif self == AirGroup.Sequencer:
        #     return Sequencer.name_of(id)
        # elif self == AirGroup.Tweak:
        #     return Tweak.name_of(id)
        # elif self == AirGroup.CenterReport:
        #     return CenterReport.name_of(id)
        # elif self == AirGroup.LogicalSwitch:
        #     return LogicalSwitch.name_of(id)
        # elif self == AirGroup.ComboSwitch:
        #     return ComboSwitch.name_of(id)
        # elif self == AirGroup.VirtualSwitch:
        #     return VirtualSwitch.name_of(id)
        # elif self == AirGroup.AnalogTrim:
        #     return AnalogTrim.name_of(id)
        # elif self == AirGroup.GenericCurve:
        #     return GenericCurve.name_of(id)
        # elif self == AirGroup.TouchInput:
        #     return TouchInput.name_of(id)

        # elif self == AirGroup.CurrentModelGeneral:
        #     return CurrentModelGeneral.name_of(id)
        # elif self == AirGroup.CurrentModelRhythmTimer:
        #     return CurrentModelRhythmTimer.name_of(id)
        # elif self == AirGroup.CurrentModelTimer:
        #     return CurrentModelTimer.name_of(id)
        # elif self == AirGroup.CurrentModelAcroWarning:
        #     return CurrentModelAcroWarning.name_of(id)
        # elif self == AirGroup.CurrentModelSailWarning:
        #     return CurrentModelSailWarning.name_of(id)
        # elif self == AirGroup.CurrentModelHeliWarning:
        #     return CurrentModelHeliWarning.name_of(id)
        # elif self == AirGroup.CurrentModelMultiWarning:
        #     return CurrentModelMultiWarning.name_of(id)
        # elif self == AirGroup.CurrentModelTelemetry:
        #     return CurrentModelTelemetry.name_of(id)
        # elif self == AirGroup.CurrentModelFmNames:
        #     return CurrentModelFmNames.name_of(id)
        # elif self == AirGroup.CurrentModelPreflight:
        #     return CurrentModelPreflight.name_of(id)
        # elif self == AirGroup.CurrentModelVox:
        #     return CurrentModelVox.name_of(id)
        elif self == AirGroup.CurrentModelVtx:
            return CurrentModelVtx.name_of(id)
        # elif self == AirGroup.CurrentModelLapTimer:
        #     return CurrentModelLapTimer.name_of(id)
        elif self == AirGroup.CurrentModel2CpuGeneral:
            return CurrentModel2CpuGen.name_of(id)
        # elif self == AirGroup.CurrentModel2CpuStickWarning:
        #     return CurrentModel2CpuStickWarning.name_of(id)
        # elif self == AirGroup.CurrentModel2CpuServoWarning:
        #     return CurrentModel2CpuServoWarning.name_of(id)
        # elif self == AirGroup.CurrentModel2CpuSwitchWarning:
        #     return CurrentModel2CpuSwitchWarning.name_of(id)

        # elif self == AirGroup.TxSystemIdentity:
        #     return TxSystemIdentity.name_of(id)
        elif self == AirGroup.TxSystemConfig:
            return TxSystemConfig.name_of(id)
        elif self == AirGroup.TxSystemCalibration:
            return TxSystemCalibration.name_of(id)
        # elif self == AirGroup.TxSystemBattery:
        #     return TxSystemBattery.name_of(id)
        # elif self == AirGroup.TxSystemDisplay:
        #     return TxSystemDisplay.name_of(id)
        # elif self == AirGroup.TxSystemSounds:
        #     return TxSystemSounds.name_of(id)

        elif self == AirGroup.ForwardProgramming:
            return ForwardProgramming.name_of(id)

        elif self == AirGroup.RfModUpdate:
            return RfModule.name_of(id)

        elif self == AirGroup.Identification:
            return Identity.name_of(id)
        elif self == AirGroup.StatusInfo:
            return Status.name_of(id)
        elif self == AirGroup.CalibrationInfo:
            return Calibration.name_of(id)
        # elif self == AirGroup.DebugMemoryAccess:
        #     return DebugMemoryAccess.name_of(id)
        elif self == AirGroup.ModelUtility:
            return Model.name_of(id)
        elif self == AirGroup.CpUtility:
            return CP.name_of(id)
        elif self == AirGroup.Compliance:
            return Compliance.name_of(id)

        return f'0x{id:02X}'


class Identity(IntEnum, metaclass=ContainsEnumMeta):
    SerialNumber = 1
    ParamCrc = 2
    ProductCode = 3
    FwMajorVersion = 4
    FwMinorVersion = 5
    FwBuildVersion = 6
    RfPid = 7
    SystemRegion = 8
    BootloaderVersion = 9
    RfCodeVersion = 10
    SecuritySerial = 11


class Status(IntEnum, metaclass=ContainsEnumMeta):
    BindStatus = 1
    BindType = 2
    ChannelMonitorData = 3
    GlueData = 4
    TrainerStatus = 5
    TrainerData = 6
    OutputValue = 7
    Position = 8
    ChannelMonitorDataEx = 9
    TxBatteryVolt = 10
    RuntimeMonitor = 11
    EnableRangeCheck = 12
    RuntimeMonitorCustomId = 13
    NumPositions = 14
    SwitchInfo = 15
    SwitchStatus = 16
    ScreenState = 17
    RFMode = 18
    ProcessingState = 19
    OperationalState = 20
    PreFlightDone = 21
    ExtUiShutdown = 22
    CurBatVoltage = 23
    UIHeartbeat = 24


class Calibration(IntEnum, metaclass=ContainsEnumMeta):
    Max = 1
    Min = 2
    Neutral = 3


class Model(IntEnum, metaclass=ContainsEnumMeta):
    Dump = 1
    Info = 2
    Load = 3
    Save = 4
    Delete = 5
    Copy = 6


class CP(IntEnum, metaclass=ContainsEnumMeta):
    BufSize = 1
    Dump = 2
    ApplyDump = 3
    GetDumpCrc = 4
    StartDefPull = 5
    DefaultPull = 6
    GetDefPullCrc = 7


class Compliance(IntEnum, metaclass=ContainsEnumMeta):
    Mode = 1
    Region = 2
    Command = 3
    Antenna = 4
    Protocol = 5
    ResetRF = 6


class Types(IntEnum, metaclass=ContainsEnumMeta):
    Type = 1
    SubTypeA = 2
    SubTypeB = 3
    SubTypeC = 4
    FrameRate = 5
    TrimMode = 6
    ThrTrimRev = 7
    SubTypeD = 8
    TrimTypeMask = 9
    RfAllowMask = 10
    SoftSw = 11
    TrimId = 12
    FModeAnalog = 13
    ModelMatchId = 14
    SerialProtocol = 15
    ExtPwrEnable = 16
    StickMode = 17
    OutputChannelCount = 18


class General(IntEnum, metaclass=ContainsEnumMeta):
    FlightModeAnalogArray = 130


class Trainer(IntEnum, metaclass=ContainsEnumMeta):
    ReceiverBind = 10
    ReceiverBindStatus = 11
    ReceiverBindType = 12
    TrainerChipDirection = 13


class ThrottleCurve(IntEnum, metaclass=ContainsEnumMeta):
    AnalogId = 1


class SailEfm(IntEnum, metaclass=ContainsEnumMeta):
    Offset = 1
    FlapLeft = 2
    FlapRight = 3
    FlaperonLeft = 4
    FlaperonRight = 5
    TiperonLeft = 6
    TiperonRight = 7
    ConditionId = 11


class SailArAf(IntEnum, metaclass=ContainsEnumMeta):
    MixLeft = 1
    MixLeft1 = 2
    MixLeft2 = 3
    MixRight = 4
    MixRight1 = 5
    MixRight2 = 6
    MixConditionId = 7
    ConditionId = 8


class GovGyro(IntEnum, metaclass=ContainsEnumMeta):
    ConditionId = 2
    TrimId = 3
    FPercent = 4
    OutChannel = 6


class MultiCS(IntEnum, metaclass=ContainsEnumMeta):
    TrimActive = 2


class AnalogAdc(IntEnum, metaclass=ContainsEnumMeta):
    Value = 1


class Srv(IntEnum, metaclass=ContainsEnumMeta):
    TrimId = 17


class Special(IntEnum, metaclass=ContainsEnumMeta):
    SourceId = 1


class CR(IntEnum, metaclass=ContainsEnumMeta):
    Alarm = 1


class Touch(IntEnum, metaclass=ContainsEnumMeta):
    ZoneSensitivity = 1


class CurrentModelVtx(IntEnum, metaclass=ContainsEnumMeta):
    Power = 1
    Band = 2
    Channel = 3
    RacePit = 4
    SendUpdate = 5


class CurrentModel2CpuGen(IntEnum, metaclass=ContainsEnumMeta):
    ModelNum = 1
    Status = 2
    CreateVersion = 3
    UniqueId = 4
    CpCrc = 5
    WarnCrc = 6
    TrimClicks = 7
    TrimClicksEx = 8
    BindInfo = 9
    ModelMatch = 10
    WaitForPreFlight = 11
    StartWithRf = 12
    Checksum = 13
    ModelName = 14
    ResetTrimClicks = 15


class TxSystem(IntEnum, metaclass=ContainsEnumMeta):
    RfModuleType = 9
    AdcDirection = 10


class TxSystemConfig(IntEnum, metaclass=ContainsEnumMeta):
    IsEnabled = 2
    StickMode = 7
    Region = 8
    UserName = 9
    Language = 15


class TxSystemCalibration(IntEnum, metaclass=ContainsEnumMeta):
    IsCalibrated = 1


class ForwardProgramming(IntEnum, metaclass=ContainsEnumMeta):
    RequestPage = 1
    SimpleMessage = 2


class RfModule(IntEnum, metaclass=ContainsEnumMeta):
    Command = 1
    BuildUartRecord = 2
    ResetRadio = 3


class AirDevID(IntEnum, metaclass=ContainsEnumMeta):
    Inhibit = 0,
    ThrottleOutput = 1,
    MotorOutput = -100,
    Gear = 52,
    Aux1 = 53,
    Aux2 = 54,
    Aux3 = 55,
    Aux4 = 56,
    Aux5 = 57,
    Aux6 = 58,
    Aux7 = 59,
    ThrottleStick = 96,
    AileronStick = 97,
    ElevatorStick = 98,
    RudderStick = 99,
    LeftKnob = 100,
    RightKnob = 101,
    SliderA = 102,
    SliderB = 103,
    SliderC = 104,
    SliderD = 105,
    SliderE = 106,
    SliderF = 107,
    SwitchA = 120,
    SwitchB = 121,
    SwitchC = 122,
    SwitchD = 123,
    SwitchE = 124,
    SwitchF = 125,
    SwitchG = 126,
    SwitchH = 127,
    SwitchI = 130,
    SwitchD2 = 131,
    SwitchE2 = 132,
    AlwaysOn = 149,
    TrimThrottle = 150,
    TrimAileron = 151,
    TrimElevator = 152,
    TrimRudder = 153,
    TrimLeftDigital = 154,
    TrimLeftAnalog = 112,
    TrimRightDigital = 155,
    TrimRightAnalog = 113,
    TrimLeftTopDigital = 160,
    TrimLeftTopAnalog = 114,
    TrimRightTopDigital = 161,
    TrimRightTopAnalog = 115,
    TrimFlap = 156,
    TrimPitch = 157,
    TrimGryo = 158,
    TrimGovernor = 159,
    TrimLeftKnob = 162,
    TrimRightKnob = 163,
    TrimSliderA = 164,
    TrimSliderB = 165,
    FlightMode = 195,
    Sequencer1A = 288,
    Sequencer2A = 289,
    Sequencer3A = 290,
    Sequencer4A = 291,
    Sequencer5A = 292,
    Sequencer6A = 293,
    Sequencer7A = 294,
    Sequencer8A = 295,
    Sequencer1B = 296,
    Sequencer2B = 297,
    Sequencer3B = 298,
    Sequencer4B = 299,
    Sequencer5B = 300,
    Sequencer6B = 301,
    Sequencer7B = 302,
    Sequencer8B = 303,
    SpoilerStick = 108,
    ComboSwitch = 312,
    Gyro1 = 304,
    Gyro2 = 305,
    Gyro3 = 306,
    TouchSwitchA = 388,
    TouchSwitchB = 389,
    TouchSwitchC = 390,
    TouchSwitchD = 391,
    TouchSwitchE = 392,
    TouchSwitchF = 393,
    TouchSwitchG = 394,
    TouchSwitchH = 395,
    TouchSwitchI = 398,
    TouchSwitchD2 = 399,
    TouchSwitchE2 = 400,
    TouchLeftStick = 412,
    TouchRightStick = 414,
