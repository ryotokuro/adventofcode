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

import os

# Get input stored in file
def get_program():
    contents = (open("5.txt")).read()
    return list(map(int, contents.split(',')))

# intcode = init[:]  # save copy of original input
program = get_program()

i = 0

# FUNCTIONS
# ---------
# 1. Add
def add(p1, p2, pos):
    program[pos] = p1 + p2
    step = 4

# 2. Multiply
def mul(p1, p2, pos):
    program[pos] = p1 * p2
    step = 4

# 3. Input
def inp(p):
    print(p)
    step = 2
    
# 4. Output
def out(p):
    program[p] = int(input('Enter ID: '))
    step = 2


# Checks if instruction requires modes
def modes_enabled(instruction):
    return len(str(instruction)) >= 3

# Returns the opcode in the instruction
def get_opcode(instruction):
    if modes_enabled(instruction):
        return str(instruction)[-2:]
    else:
        return instruction

def get_parameters(instruction):
    # Modes specified in instruction
    if modes_enabled(instruction):
        # instruction is '104'
        if get_opcode == '04':
            out(program[i+1])
            
        # '01' (add) or '02' (mul)
        else:
            # pad instruction to 5
            # instruction.insert('0'*(5-len(instruction)), 0)
            # A. Position Mode
            if instruction[0] == '0':
                pos = program[i+3]
            else:
                pos = i+3

            # B. P2 Mode
            if instruction[1] == '0':
                
            else:

            # C. P1 Mode
            if instruction[2] == '0':
                
            
            # 2 Parameters in form ABCDE
            # A: pos, B: p2_mode, C: p1_mode, DE: opcode  
            if len(instruction) == 5:
                pos = i+3
            else:
                pos = program[i+3]

            if len(instruction) >= 4:
                p2_mode = instruction[-4:-3] # B
                p1_mode = instruction[-3:-2] # C
            
            # Mode 01: P2(B) = position, P1(C) = value
            if len(instruction) == 3:
                p2 = program[program[i+2]]
                p1 = program[i+1]
                
            # Mode 11: Both parameters are taken as values
            elif p1_mode == '1' and p2_mode == '1':
                p1 = intcode[i+1]
                p2 = intcode[i+2]

            # Mode 10: P2(B) = value, P1(C) = position
            elif p2_mode == '1' and p1_mode == '0':
                p2 = program[i+2]   # value
                p1 = program[program[i+1]]  # position

            # OPCODES
            # -------
            # 1: Add p1 & p2 then save at position specified in parameter 3
            if get_opcode() == '01':
                add(p1, p2, pos)
                
            # 2: Multiply p1 & p2 then save at position specified in parameter 3
            elif get_opcode() == '02':
                mul(p1, p2, pos)
                
    # No modes, default configuration
    else:
        opcode = program[i]
        # Either OP 1 or OP 2 (0001, 0002)
        if opcode == 1 or opcode == 2:
            p1 = program[program[i+1]]
            p2 = program[program[i+2]]
            pos = program[i+3]

            # OP 1: Add p1 and p2 and save to position pos
            if opcode == 1:
                add(p1, p2, pos)

            # OP 2: Multiply p1 and p2 and save to position pos
            else:
                mul(p1, p2, pos)
        
        # OP 3: Save input at position specified in only parameter
        elif opcode == 3:
            inp(program[i+1])
            
        # OP 4: Output value at position specified in only parameter
        elif opcode == 4:
            out(program[i+1])
            
        # OP 99: halt!
        elif opcode == 99:
            #break
            sys.exit()

while i < len(program):
    instruction = str(program[i])
    get_parameters(instruction)
    i += step

"""
i = 0
# Loop over input
while i < len(intcode):
    # PARAMETER MODES
    # ---------------
    print(intcode[i])
    if len(str(intcode[i])) >= 3:  # if the opcode is greater than 2 then it has param modes
        opcode = str(intcode[i])[-2:]  # XXOP
        
        # 1 Parameter: 104
        if opcode == '04':
            p1 = intcode[i+1]
            print("CODE:", p1)
            num_instructions = 2
                    
        else:
            # 2 Parameters in form ABCDE (01002)
            if len(str(intcode[i])) == 5:
                pos = i+3
            else:
                pos = intcode[i+3]

            if len(str(intcode[i])) >= 4:
                p1_mode = str(intcode[i])[-3:-2] # C
                p2_mode = str(intcode[i])[-4:-3] # D
            
            # 01: P2(B) = position, P1(C) = value
            if len(str(intcode[i])) == 3:
                p2 = intcode[intcode[i+2]]
                p1 = intcode[i+1]
                
            # 11: Both parameters are taken as values
            elif p1_mode == '1' and p2_mode == '1':
                p1 = intcode[i+1]
                p2 = intcode[i+2]

            # 10: P2(B) = value, P1(C) = position
            elif p2_mode == '1' and p1_mode == '0':
                p2 = intcode[i+2]   # value
                p1 = intcode[intcode[i+1]]  # position

            # OPCODES
            # -------
            # OP 1: add param 1 and param 2 then save at position specified in parameter 3
            if opcode == '01':
                intcode[pos] = p1 + p2
                
            # OP 2: multiply param 1 and param 2 then save at position specified in parameter 3
            elif opcode == '02':
                intcode[pos] = p1 * p2

            num_instructions = 4


    # DEFAULT PARAMETERS: POSITION (O)
    # --------------------------------
    else:
        opcode = intcode[i]
        # Either OP 1 or OP 2 (0001, 0002)
        if opcode == 1 or opcode == 2:
            p1 = intcode[intcode[i+1]]
            p2 = intcode[intcode[i+2]]
            pos = intcode[i+3]

            # OP 1: Add p1 and p2 and save to position p3
            if opcode == 1:
                intcode[pos] = p1 + p2
            # OP 2: Multiply p1 and p2 and save to position p3
            else:
                intcode[pos] = p1 * p2
                
            num_instructions = 4
        
        # OP 3: Save input at position specified in only parameter
        elif opcode == 3:
            p1 = intcode[i+1]
            intcode[p1] = int(input("Please enter the ID of the system to test: "))
            num_instructions = 2
            
        # OP 4: Output value at position specified in only parameter
        elif opcode == 4:
            p1 = intcode[i+1]
            print("CODE:", intcode[p1])
            num_instructions = 2
            
        # OP 99: halt!
        elif opcode == 99:
            break
        
    i += num_instructions

# print(intcode)
"""
