# Python emulator for Chip-8
import random

MEMSIZE = 0x1000
REGSIZE = 0x10
CHIP8_STRT = 0x200

memory = bytearray(MEMSIZE)
V = bytearray(REGSIZE)
I = random
PC = CHIP8_STRT
Instr_H = 0x00
Instr_L = 0x00


def Ifetch(prog_cntr):
    global Instr_H
    global Instr_L

    Instr_H = memory[prog_cntr]
    Instr_L = memory[prog_cntr+1]
    prog_cntr += 2
    return

def chip8_init():
    for i in range(MEMSIZE):
        memory[i] = random.randint(0, 0xFF)

chip8_init() # initialize chip8
print(memory[0x180:0x280].hex())

while True:
    Ifetch(PC)
    print(Instr_H, Instr_L)
    if PC == 0x220:
      break
