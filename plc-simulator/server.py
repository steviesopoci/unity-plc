from pymodbus.server import StartTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusSlaveContext,
    ModbusServerContext
)

from core import PLCMemory
from logic import PLCLogic
import threading

# -----------------------------
# INIT PLC MEMORY
# -----------------------------
memory = PLCMemory()

# -----------------------------
# START PLC LOGIC THREAD
# -----------------------------
logic = PLCLogic(memory)
threading.Thread(target=logic.run, daemon=True).start()

# -----------------------------
# MODBUS MEMORY MAP
# -----------------------------
store = ModbusSlaveContext(
    co=ModbusSequentialDataBlock(0, memory.coils),
    hr=ModbusSequentialDataBlock(0, memory.registers)
)

context = ModbusServerContext(slaves=store, single=True)

# -----------------------------
# START SERVER
# -----------------------------
print("========================")
print("UnityPLC Running")
print("Port: 1502")
print("========================")

StartTcpServer(
    context=context,
    address=("0.0.0.0", 1502)
)