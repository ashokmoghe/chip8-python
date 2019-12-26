# Python emulator for Chip-8
import random

MEMSIZE = 0x1000
REGSIZE = 0x10
CHIP8_STRT = 0x200

class Interpreter():
    def __init__(self):
        self.memory = bytearray(MEMSIZE)
        for i in range(MEMSIZE):
            self.memory[i] = random.randint(0, 0xFF)

        self.V = bytearray(REGSIZE)
        self.I = random.randint(0, MEMSIZE)
        self.PC = CHIP8_STRT
        self.Instr_H = 0x00
        self.Instr_L = 0x00
        self.Instr_HH = 0x0
        self.Instr_HL = 0x0
        self.Instr_LH = 0x0
        self.Instr_LL = 0x0


    def Ifetch(self):
        self.Instr_H = self.memory[self.PC]
        self.Instr_L = self.memory[self.PC + 1]
        self.Instr_HH = self.Instr_H >> 4
        self.Instr_HL = self.Instr_H & 0x0F
        self.Instr_LH = self.Instr_L >> 4
        self.Instr_LL = self.Instr_L & 0x0F
        self.PC = (self.PC + 2) % MEMSIZE

    def skip(self):
        self.PC = (self.PC + 2) % MEMSIZE


# initialize chip8
i = Interpreter()
print(i.memory[0x200:0x220].hex())

while True:
    i.Ifetch()
 #   i.decode()
 #   i.execute()
    print(i.PC, i.Instr_H, i.Instr_L, i.Instr_HH, i.Instr_HL, i.Instr_LH, i.Instr_LL)

    if i.PC == 0x220:
      break
