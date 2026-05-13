# unity-plc

Industrial automation and controls digital twin prototype built with Unity, Python, OpenPLC, and Modbus TCP.

UnityPLC is a modular industrial simulation system designed to explore PLC communication, factory simulation workflows, SCADA/HMI concepts, and digital twin architecture using Unity as the real-time visualization layer.

The project separates industrial communication, PLC logic, and simulation systems into modular layers that can later integrate with OPC UA systems, industrial protocols, and real PLC hardware.

---

## 🎥 Demo

https://github.com/user-attachments/assets/19253db7-34de-46f5-8266-c6afede7e90e

---

## 🧠 System Architecture

UnityPLC follows a layered industrial architecture:

```text
PLC Runtime / Simulator  
↓  
Modbus TCP  
↓  
Unity PLC Driver Layer  
↓  
Tag System  
↓  
Factory Simulation / HMI
``` 

Key principles:
- Unity simulation logic does not depend on PLC vendor
- Communication is abstracted through Modbus
- Tag system decouples logic from raw registers
- Modular architecture enables future protocol swaps

---

## 🔌 Current Features

- Modbus TCP communication
- Python-based PLC simulator
- Unity digital twin environment
- Config-driven PLC connection system
- Abstracted PLC tag architecture
- Real-time polling and synchronization
- SCADA/HMI-ready architecture
- Vendor-agnostic system design

---

## 🏭 Planned Features

### Factory Simulation
- Conveyor control systems
- Motorized production lines
- Sensor feedback systems
- VFD simulation
- Robotic cell coordination

### Controls Systems
- Start/Stop panels
- Emergency stop logic
- Interlocks and sequencing
- Alarm states

### Industrial Protocols
- OPC UA integration
- EtherNet/IP support
- Siemens S7 communication
- Beckhoff TwinCAT integration
- MQTT/IIoT systems

### SCADA / HMI
- Real-time dashboards
- Tag visualization
- Historian logging
- Alarm/event tracking
- Trend visualization

### Future Expansion
- OpenCV vision systems
- Robotics simulation workflows
- Predictive maintenance experimentation
- Distributed digital twin systems

---

## 🛠️ Tech Stack

- Unity 6
- C#
- Python
- Modbus TCP
- EasyModbus
- PyModbus
- OpenPLC

---

## ⚙️ Setup

### Unity
1. Download and install [Unity Hub](https://unity3d.com/get-unity/download) and [Unity Version: LTS Release Unity 6.4 (6000.4.6f1)](https://unity3d.com/unity/qa/lts-releases?page=2).
2. Ensure [Git](https://git-scm.com/) and [Git LFS (Large File Storage)](https://git-lfs.github.com) are properly downloaded and installed before cloning from **Git Bash**.
3. Naviagte to **Unity Hub** and open `Main` in **Unity Version: LTS Release Unity 6.4 (6000.4.6f1)**.
4. In order to test the project, press the `Play` button in the **Unity Editor**.

### Python PLC Simulator

Open a terminal and run the following commands:

```bash
cd plc-simulator

python3 -m venv venv

source venv/bin/activate

pip install pymodbus==3.5.4

python server.py
```

---

## 📡 Use Cases

- Industrial digital twins
- PLC training systems
- Factory simulation
- SCADA visualization
- Controls engineering demos
- Robotics simulation

---

## 📌 Notes

- Prototype system
- Educational and experimental
- Designed for extensibility

---

## 🪪 License

MIT — feel free to fork and build on this for fun, for education, or even for production.
