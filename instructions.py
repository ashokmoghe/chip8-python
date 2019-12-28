import random
from constants import *
from timers import *

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

def group_1(i, address):
    i.PC = address % MEMSIZE

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
    vf = i.V[0xF]
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
        if (temp > BYTEMASK): vf = 1
    elif (subop == 5):
        temp = (vx - vy)
        if (vx >= vy): vf = 1
    elif (subop == 6):
        temp = (vy >> 1)
        vf = vy & 0x1
    elif (subop == 7):
        temp = (vy - vx)
        if (vy >= vx): vf = 1
    elif (subop == 0xE):
        temp = (vy << 1)
        vf = (vy & 0x80)>>7
    i.V[register_x] = temp % MODBYTE
    i.V[0xF] = vf
    return

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
def group_C(i, register_x, lower_byte):
    i.V[register_x] = random.randint(0, MODBYTE-1) & lower_byte

def group_E(i, register_x, lower_byte):
    keypress = None
    # EX9E - Skip the following instruction if the key corresponding to the hex value currently stored in register VX is pressed
    if lower_byte == 0x9E:
        if keypress == i.V[register_x]:
            i.skip()
    # EXA1 - Skip the following instruction if the key corresponding to the hex value currently stored in register VX is not pressed
    elif lower_byte == 0xA1:
        if keypress != i.V[register_x]:
            i.skip()
    else:
        raise InstructionError("Invalid lower byte for group E.")

 #FXPP - Complex Instructions Operand Vx, Subinstruction PP
def group_F(i, register_x, subop, deltimer):
    vx = i.V[register_x] % MODBYTE
    temp = 0
    if (subop == 0x07):
        i.V[register_x] = deltimer.get_timer()
    elif (subop == 0x0A):
        pass
        #keypress to be inmplemented
    elif (subop == 0x15):
        deltimer.set_timer(vx)
    elif (subop == 0x18):
  #      sound_timer.set_timer(vx)
        pass
    elif (subop == 0x1E):
        i.I += vx
    elif (subop == 0x29):
        i.I = HEXFONT_BASE + (vx & NIBMASK)
    elif (subop == 0x33):
        digit2 = vx // 100
        digit1 = (vx % 100) // 10
        digit0 = vx % 10
        addr = i.I % MEMSIZE
        i.memory[addr] = digit2 & BYTEMASK
        i.memory[addr + 1] = digit1 & BYTEMASK
        i.memory[addr + 2] = digit0 & BYTEMASK
    elif (subop == 0x55):
        for index in range((register_x+1)&NIBMASK):
            i.setmem(i.I,i.V[index])
            i.I += 1
    elif (subop == 0x65):
        for index in range((register_x+1)&NIBMASK):
            i.V[index] = i.getmem(i.I)
            i.I += 1
    return
