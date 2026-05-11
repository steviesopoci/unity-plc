class PLCMemory:
    """
    PLC memory abstraction:
    - coils = digital IO
    - registers = analog IO
    """

    def __init__(self, size=10):
        self.coils = [0] * size
        self.registers = [0] * size

    # DIGITAL
    def read_coil(self, i): return self.coils[i]
    def write_coil(self, i, v): self.coils[i] = 1 if v else 0

    # ANALOG
    def read_reg(self, i): return self.registers[i]
    def write_reg(self, i, v): self.registers[i] = int(v)