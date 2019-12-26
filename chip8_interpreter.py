# Python emulator for Chip-8
import random

MODBYTE = 0x100
MODNIB = 0x10
BYTEMASK = 0xFF
NIBMASK = 0x0F
MEMSIZE = 0x1000
REGSIZE = 0x10
CHIP8_STRT = 0x200

class Interpreter():
    def __init__(self):
        self.memory = bytearray(MEMSIZE)
        for i in range(MEMSIZE):
            self.memory[i] = random.randint(0, MODBYTE-1)

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
        self.Instr_HL = self.Instr_H & NIBMASK
        self.Instr_LH = self.Instr_L >> 4
        self.Instr_LL = self.Instr_L & NIBMASK
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

# This is the main exec loop. Simple Opcodes are handled here immediately.
# Complex Opcodes '8', 'F' are delegated to the object
#

    if (i.Instr_HH == 3):    #Skip if Vx == KK
        if (i.V[i.Instr_HL] == i.Instr_L):
            i.skip()
    if (i.Instr_HH == 4):    #Skip if Vx != KK
        if (i.V[i.Instr_HL] != i.Instr_L):
            i.skip()
    if (i.Instr_HH == 5):    #Skip if Vx == Vy
        if (i.V[i.Instr_HL] == i.V[i.Instr_LH]):
            i.skip()
    if (i.Instr_HH == 6):    #Set Vx = KK
        i.V[i.Instr_HL] = i.Instr_L
    if (i.Instr_HH == 7):    #Set Vx = Vx + KK
        i.V[i.Instr_HL] = (i.V[i.Instr_HL] + i.Instr_L) % MODBYTE
    if (i.Instr_HH == 9):    #Skip if Vx != Vy
        if (i.V[i.Instr_HL] == i.V[i.Instr_LH]):
            i.skip()
    if (i.Instr_HH == 0xA):  #Set I = NNN
        i.I = (i.Instr_HL*MODBYTE + i.Instr_L) % MEMSIZE

"""
