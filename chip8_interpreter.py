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

i.memory[0x200] = 0xCA
i.memory[0x201] = 0xFF
i.memory[0x202] = 0xA2
i.memory[0x203] = 0x20
i.memory[0x204] = 0xFA
i.memory[0x205] = 0x33

print(i.memory[0x200:0x206].hex())

while True:
    i.Ifetch()
 #   i.decode()
 #   i.execute()
    if (i.Instr_HH == 0):   # group 0
        group_0(i, i.Instr_L, None)
    elif (i.Instr_HH == 1):
        address = (i.Instr_HL*MODBYTE + i.Instr_L) % MEMSIZE
        group_1(i, address)
    elif (i.Instr_HH == 2):
        address = (i.Instr_HL*MODBYTE + i.Instr_L) % MEMSIZE
        group_2(i, address)
    elif (i.Instr_HH == 3):
        group_3(i, i.Instr_HL, i.Instr_L)
    elif (i.Instr_HH == 4):
        group_4(i, i.Instr_HL, i.Instr_L)
    elif (i.Instr_HH == 5):
        group_5(i, i.Instr_HL, i.Instr_LH)
    elif (i.Instr_HH == 6):
        group_6(i, i.Instr_HL, i.Instr_L)
    elif (i.Instr_HH == 7):
        group_7(i, i.Instr_HL, i.Instr_L)
    elif (i.Instr_HH == 8):
        group_8(i, i.Instr_HL, i.Instr_LH, i.Instr_LL)
    elif (i.Instr_HH == 9):
        group_9(i, i.Instr_HL, i.Instr_LH)
    elif (i.Instr_HH == 0xA):
        address = (i.Instr_HL*MODBYTE + i.Instr_L) % MEMSIZE
        group_A(i, address)
    elif (i.Instr_HH == 0xB):
        address = (i.Instr_HL*MODBYTE + i.Instr_L) % MEMSIZE
        group_B(i, address)
    elif (i.Instr_HH == 0xC):
        group_C(i, i.Instr_HL, i.Instr_L)
    elif (i.Instr_HH == 0xE):
        group_E(i, i.Instr_HL, i.Instr_L)
    elif (i.Instr_HH == 0xF):
        group_F(i, i.Instr_HL, i.Instr_L, delay_timer_t)

#    print(i.PC, i.Instr_H, i.Instr_L, i.Instr_HH, i.Instr_HL, i.Instr_LH, i.Instr_LL)
    if i.PC == 0x206:
        break
print(i.memory[0x220:0x22F].hex())
print('done')
