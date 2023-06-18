# Spektrum Bootloader and SG3 Decoder
> **Note**: This plugin is still a work-in-progress and may contain bugs
> 
This is a High Level Analyzer for Saleae Logic 2.x software. It supports the decoding of a couple of
Serial communication formats used by Spektrum in their DX and iX series of Surface and Air 
Transmitters and Receivers.

## Features
- Decode bootloader messages between Spektrum Programmer software for Windows and compatible Spektrum Receivers and Transmitters. 
- Decode UART messages between an Android-based Spektrum Radio (DX6R, iX12, iX14, iX20), and it's corresponding Channel Processor (CP).


## Images
![](docs/images/img6.png)
![](docs/images/img5.png)
![](docs/images/model_saved.png)
![](docs/images/img4.png)
![](docs/images/img3.png)
![](docs/images/img2.png)
![](docs/images/img1.png)

### Spektrum Programmer
#### About
Communication is done via serial communication over a single wire.
#### Wiring Setup
- Use a `Spektrum TX/RX USB Programming Cable (SPMA3065)`
- Use a standard `Y-Harness` connector for servo cables. (Example: `SPMA3058`)
- Connect the programming cable to your computer's USB port.
- Connect the servo end of the programming cable to one of the two shrouded connectors on the Y-Harness.
- Connect the servo end of the Y-Harness to your compatible TX/RX.
- Connect your Logic Analyzer's Ground to the Ground pin of the leftover shrouded connector.
- Connect one of your Logic Analyzer's Pins to the Signal pin of that same connector.

![](docs/images/usb_y_harness.png)

#### Logic2 Setup
- Create an `Async Serial` Analyzer with the speed `115200` and rest leave as default.
- Create a new `Spektrum TX/RX Bootloader and SG3 Decoder` Analyzer and link it with the `Async Serial` Analyzer you used in the previous step.
#### Diagrams
Flash new firmware to compatible Spektrum TX or RX using Spektrum Programmer software.
```mermaid
%% NOTE: View rendered diagrams on GitHub repo
sequenceDiagram
    actor U as User
    participant SP as Spektrum Programmer
    participant TX as Compatible TX / RX
    U->>SP: Connect
    SP->>TX: CABLE_SYN
    TX->>SP: CABLE_ACK
    SP->>TX: ID_REQUEST
    TX->>SP: ID_RESPONSE
    U->>SP: Flash Firmware
    SP->>TX: SAX_ERASE
    TX-->>TX: Erase Data
    TX->>SP: SAX_ERASE_RESPONSE
    loop For each block of SAX file
        SP->>TX: SAX_WRITE
        TX-->>TX: Write Data
        TX->>SP: SAX_WRITE_RESPONSE
    end
    SP->>TX: SAX_EOF
    TX->>SP: SAX_EOF_RESPONSE
    SP->>U: Success
```

### iX12/14/20 and DX6R LibSG3
#### About
The Android based iX12, iX14, and iX20 Air Transmitters and DX6R Surface Transmitter communicate from the Android application to the 
Channel Processor (CP) using a custom Spektrum C/C++ Library called LibSG3, which uses UART on port `/dev/ttyS0` @ `115200` baud rate.

#### Wiring Setup
- Probe the various Test Points on the PCB for anything sending Serial communication
- On a DX6R, the UART is on `TP35` and `TP36`

#### Logic2 Setup
- Create 2 `Async Serial` Analyzers with the speed `115200` and rest leave as default.
- Create a new `Spektrum TX/RX Bootloader and SG3 Decoder` Analyzer for each `Async Serial` Analyzer you created in the previous step.

#### Diagrams
Example communications of a DX6R radio
```mermaid
%% NOTE: View rendered diagrams on GitHub repo
sequenceDiagram
    actor U as User
    box Android
        participant AW as AirWare / RaceWare (C#35;)
        participant SG3 as Lib SG3 (C/C++)
    end
    participant CP as Channel Processor (CP)
    
    U->>AW: Open RaceWare
    
    AW->>SG3: initLibSG3()
    SG3->>CP: DISCOVER
    CP->>SG3: DISCOVER_RESPONSE
    SG3->>AW: SG3ERR_SUCCESS
    
    AW->>SG3: enableRadio()
    SG3->>CP: SET_RF_MODE
    CP->>SG3: ACK
    CP->>SG3: SET_RF_MODE_RESPONSE
    SG3->>CP: ACK
    SG3->>AW: SG3ERR_SUCCESS
    
    loop Every 50ms
        CP->>SG3: SurfaceRuntimeData
        SG3->>AW: SurfaceRuntimeData Event
    end

    U->>AW: Set Brake Rate
    AW->>SG3: setBrakeRate()
    SG3->>CP: WRITE_FIELD
    CP->>SG3: ACK
    CP->>SG3: WRITE_FIELD_RESPONSE
    SG3->>CP: ACK
    SG3->>AW: SG3ERR_SUCCESS
    SG3-->>SG3: Wait for timeout
    SG3->>AW: ModelSavedToFlash
```
