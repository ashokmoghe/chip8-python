import random
from constants import *

class InstructionError(Exception):
    pass

def group_0(i, lower_byte, graphics):
    if lower_byte == 0xE0:
        # 00E0 - Clear screen
        graphics.clear_screen()
    elif lower_byte == 0xEE:
        # 00EE - Return from subroutine
        i.PC = i.stack.pop(-1) % MEMSIZE
    else:
        # 0NNN - Execute machine language subroutine at address NNN
        raise InstructionError("Instruction 0NNN not implemented.")

# 2NNN - Execute subroutine starting at address NNN
def group_2(i, address):
    i.stack.append(i.PC)
    i.PC = address % MEMSIZE

# 3XKK - Skip the following instruction if the value of register VX equals KK
def group_3(i, register, lower_byte):
    if i.V[register] == lower_byte:
        i.skip()

# 4XKK - Skip the following instruction if the value of register VX is not equal to KK
def group_4(i, register, lower_byte):
    if i.V[register] != lower_byte:
        i.skip()

# 5XY0 - Skip the following instruction if the value of register VX is equal to the value of register VY
def group_5(i, register_x, register_y):
    if i.V[register_x] == i.V[register_y]:
        i.skip()

# 6XKK - Set Vx = KK
def group_6(i, register_x, lower_byte):
    i.V[register_x] = lower_byte & BYTEMASK

# 7XKK - Set Vx = Vx + KK; Carry is ignored and doesn't affect VF
def group_7(i, register_x, lower_byte):
    i.V[register_x] = (i.V[register_x] + lower_byte) % MODBYTE

# 8XYP - Airthmatic Instructions Operands Vx, Vy and Operator P
def group_8(i, register_x, register_y, subop):
    vx = i.V[register_x]
    vy = i.V[register_y]
    vf = 0
    temp = 0
    if (subop == 0):
        temp = vy
    elif (subop == 1):
        temp = (vx | vy)
    elif (subop == 2):
        temp = (vx & vy)
    elif (subop == 3):
        temp = (vx ^ vy)
    elif (subop == 4):
        temp = (vx + vy)
    elif (subop == 5):
        temp = (vx - vy)
    elif (subop == 6):
        temp = (vx >> 1)
        vf = vx & 0x1
    elif (subop == 7):
        temp = (vy - vx)
    elif (subop == 0xE):
        temp = (vx << 1)
        vf = (vx & 0x80)>>7






# 9XY0 - Skip the following instruction if the value of register VX is not equal to the value of register VY
def group_9(i, register_x, register_y):
    if i.V[register_x] != i.V[register_y]:
        i.skip()

# ANNN - Set pointer I to address NNN
def group_A(i, address):
    i.I = address % MEMSIZE

# BNNN	Jump to address NNN + V0
def group_B(i, address):
    i.PC = (address + i.V[0]) % MEMSIZE

# CXKK	Set VX to a random number with a mask of KK
def group_C(i, register, lower_byte):
    i.V[register] == random.randint(0, MODBYTE-1) & lower_byte:

def groupF(i, vx, vy, subop):
    pass
