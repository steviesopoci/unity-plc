import time

class PLCLogic:
    """
    Simulated PLC scan cycle
    """

    def __init__(self, memory):
        self.memory = memory

    def scan(self):
        motor_start = self.memory.read_coil(0)
        estop = self.memory.read_coil(2)

        # SAFETY FIRST
        if estop:
            self.memory.write_coil(1, 0)
            return

        # MOTOR LOGIC
        if motor_start:
            self.memory.write_coil(1, 1)
        else:
            self.memory.write_coil(1, 0)

    def run(self):
        print("[PLC] Scan loop started")

        while True:
            self.scan()
            time.sleep(0.1)