class InstructionError(Exception):
    pass

def group_0(i, lower_byte, graphics):
    if lower_byte == 0xE0:
        # 00E0 - Clear screen
        graphics.clear_screen()
    elif lower_byte == 0xEE:
        # 00EE - Return from subroutine
        i.PC = i.stack.pop(-1)
    else:
        # 0NNN - Execute machine language subroutine at address NNN
        raise InstructionError("Instruction 0NNN not implemented.")

# 2NNN - Execute subroutine starting at address NNN


def group_2(i, address):
    i.stack.append(i.PC + 1)
    i.PC = address

# 3XNN - Skip the following instruction if the value of register VX equals NN


def group_3(i, register, lower_byte):
    if i.V[register] == lower_byte:
        i.skip()
# 4XNN - Skip the following instruction if the value of register VX is not equal to NN


def group_4(i, register, lower_byte):
    if i.V[register] != lower_byte:
        i.skip()

# 5XY0 - Skip the following instruction if the value of register VX is equal to the value of register VY


def group_5(i, register_x, register_y):
    if i.V[register_x] == i.V[register_y]:
        i.skip()


def group8(i, vx, vy, subop):
    if (subop == 1):
        i.V[vx] = i.V[vx] | i.V[vy]
if (subop == 1):
        i.V[vx] = i.V[vx] | i.V[vy]
if (subop == 1):
        i.V[vx] = i.V[vx] | i.V[vy]
if (subop == 1):
        i.V[vx] = i.V[vx] | i.V[vy]
if (subop == 1):
        i.V[vx] = i.V[vx] | i.V[vy]
if (subop == 1):
        i.V[vx] = i.V[vx] | i.V[vy]
if (subop == 1):
        i.V[vx] = i.V[vx] | i.V[vy]

def groupF(i, vx, vy, subop):
#def group8(i, vx, vy, subop):
