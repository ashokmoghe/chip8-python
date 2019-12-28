# Python emulator for Chip-8
import random
from constants import *
import threading
from timers import *
import threaded_timers
from instructions import *


class Interpreter():
    def __init__(self):
        self.memory = bytearray(MEMSIZE)
        for i in range(MEMSIZE):
            self.memory[i] = random.randint(0, MODBYTE-1)

        self.V = bytearray(REGSIZE)
        self.I = random.randint(0, MEMSIZE)
        self.PC = CHIP8_STRT
        self.stack = []
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
delay_timer = Timer()
#get the time tick going
timetick = threading.Thread(target=tick_function, args=(1, delay_timer))
timetick.start()
# threaded timer
delay_timer_t = threaded_timers.Timer()
delay_timer_t.start()

print(i.memory[0x200:0x220].hex())

while True:
    i.Ifetch()
 #   i.decode()
 #   i.execute()
    print(i.PC, i.Instr_H, i.Instr_L, i.Instr_HH, i.Instr_HL, i.Instr_LH, i.Instr_LL)
    if i.PC == 0x220:
      break

i.V[7] = 255

group_F(i, 7, 15, delay_timer)
k=1
while (k !=0):
    group_F(i, 8, 7, delay_timer)
    k = i.V[8]

print('done')

# This is the main exec loop. Simple Opcodes are handled here immediately.
# Complex Opcodes '8', 'F' are delegated to the object
#
"""
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
        i.V[register_x] = (i.V[register_x]  + i.Instr_L) % MODBYTE
    if (i.Instr_HH == 9):    #Skip if Vx != Vy
        if (i.V[i.Instr_HL] == i.V[i.Instr_LH]):
            i.skip()
    if (i.Instr_HH == 0xA):  #Set I = NNN
        i.I = (i.Instr_HL*MODBYTE + i.Instr_L) % MEMSIZE
"""


