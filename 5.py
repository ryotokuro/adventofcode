"""
5.py: Intcode Computer

Op-codes
---------------------------------------------------------------------------------------
# 1: Add numbers from position n+1 and n+2 and store in position n+3
# 2: Multiply numbers from position n+1 and n+2 and store in position n+3
# 3: Takes an integer input and save it to the position specified in the only parameter
# 4: Outputs the value stored in the position specified in the only parameter
# 99: Program finished, halt
"""

# Imports
# -------
import sys
import os

# Globals
# -------
IP = 0  # Instruction Pointer

# Get input stored in file
def get_program():
    contents = (open("5.txt")).read()
    return list(map(int, contents.split(',')))

program = get_program()  # global program sequence


# Computer Functions
# ------------------
# 0. Nop: do nothing
def nop():
    pass

# 1. Add: Add p1 and p2 and save to position pos
def add(p1, p2, pos):
    global program
    program[pos] = program[p1] + program[p2]

# 2. Multiply: Multiply p1 and p2 and save to position pos
def mul(p1, p2, pos):
    global program
    program[pos] = program[p1] * program[p2]
    
# 3. Input: Save input to position p
def inp(p):
    global program
    program[p] = int(input('Enter ID: '))
    
# 4. Output: Output value at position p
def out(p):
    print(program[p])

# 5. Jump-if-true: if p1 is non-zero, IP goes to value from p2 (otherwise, do nothing)
def tjmp(p1, p2):
    if p1 != 0:  # if p1 is non zero
        # ip goes to value from p2
        IP = program[p2]
    else:
        nop()  # otherwise, do nothing

# 6. Jump-if-false: if p1 is 0, set IP to value from p2 (otherwise, do nothing)
def fjmp:
    

# 7. Less than: if p1 < p2, store 1 in the position given by p3 (otherwise, store 0)


# 8. Equals: if p2 == p2 store 1 in position given by p3 (otherwise, store 0)
def eql(p1, p2, pos):
    if p1 == p2

# 99. Stop: Kill yourself
def stop():
    sys.exit()

# Other Functions
# ---------------
# Make instruction 5 bits long
def padding(instruction):
    return '0'*(5-len(instruction)) + instruction

def get_parameters(instruction):
    global IP
    global program
    # Position
    # A = 0: Position
    if instruction[0] == '0':
        pos = program[IP+3]
    # A = 1: Immediate
    else:
        pos = IP+3

    # P2
    # B = 0: Position
    if instruction[1] == '0':
        p2 = program[IP+2]
    # B = 1: Value
    else:
        p2 = IP+2
        
    # P1
    # C = 0: Position
    if instruction[2] == '0':
        p1 = program[IP+1]
    # C = 1: Value
    else:
        p1 = IP+1

    return pos, p1, p2

def execute(instruction):
    global IP
    # Instruction (ABCDE) bits are in the format:
    # - A:  Position Mode
    # - B:  P2 Mode
    # - C:  P1 Mode
    # - DE: Opcode
    
    # Padding
    instruction = padding(instruction)
    # print(instruction)  # debug instruction sequence

    # Parameters
    pos, p1, p2 = get_parameters(instruction)

    # Determine Opcode
    # ----------------
    opcode = instruction[3:]
    if opcode == '01':
        add(p1, p2, pos)
        return 4

    elif opcode == '02':
        mul(p1, p2, pos)
        return 4

    elif opcode == '03':
        inp(p1)
        return 2

    elif opcode == '04':
        out(p1)
        return 2

    elif opcode == '99':
        stop()  # break

    else:
        print("uh oh stinky poo")


# Main
while IP < len(program):
    instruction = str(program[IP])
    IP += execute(instruction)
