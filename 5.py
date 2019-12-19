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
file = open("5.txt")
contents = file.read()
init = contents.split(',')
init = list(map(int, init))

intcode = init[:]  # save copy of original input

print("Welcome to the TEST diagnostic program")

def modes_enabled(instruction):
    return len(str(instruction)) >= 3

def get_opcode(instruction):
    if modes_enabled(instruction):
        return str(instruction)[-2:]
    else:
        return instruction

def add(p1, p2):
    intcode[i+3] = p1 + p2

def mul(p1, p2):
    intcode[i+3] = p1 * p2
    

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
            p1_mode = str(intcode[i])[-3:-2] # C
            p2_mode = str(intcode[i])[-4:-3] # D
            
            # 01DE: P1(C) = value, P2(B) = position
            if len(str(intcode[i])) == 3:
                p1 = intcode[i+1]
                p2 = intcode[intcode[i+2]]
                
            # 11: Both parameters are taken as values
            elif p1_mode == '1' and p2_mode == '1':
                p1 = intcode[i+1]
                p2 = intcode[i+2]

            # 10: P1(C) = position, P2(B) = value
            elif p1_mode == '1' and p2_mode == '0':
                p1 = intcode[intcode[i+1]]  # position
                p2 = intcode[i+2]   # value

            # OPCODES
            # -------
            # OP 1: add param 1 and param 2 then save at position specified in parameter 3
            if opcode == '01':
                intcode[intcode[i+3]] = p1 + p2
                
            # OP 2: multiply param 1 and param 2 then save at position specified in parameter 3
            elif opcode == '02':
                intcode[intcode[i+3]] = p1 * p2

            num_instructions = 4


    # DEFAULT PARAMETERS: POSITION (O)
    # --------------------------------
    else:
        opcode = intcode[i]
        # Either OP 1 or OP 2
        if opcode == 1 or intcode == 2:
            p1 = intcode[intcode[i+1]]
            p2 = intcode[intcode[i+2]]
            position = intcode[i+3]

            # OP 1: Add p1 and p2 and save to position p3
            if opcode == 1:
                intcode[position] = p1 + p2
            # OP 2: Multiply p1 and p2 and save to position p3
            else:
                intcode[position] = p1 * p2
                
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
