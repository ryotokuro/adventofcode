# Intcode Computer
# ----------------
# Op-codes
# 1: add numbers from position n+1 and n+2 and store in position n+3
# 2: multiply numbers from position n+1 and n+2 and store in position n+3
# 3: takes an integer input and saves it to the position from parameter
# 4: outputs the value at the position specified in the parameter n+1
# 99: program finished, halt

# EXAMPLE
# intcode = [1,9,10,3,2,3,11,0,99,30,40,50]

import os

print("Welcome to the TEST diagnostic program")
input("Please enter the ID of the system: ")

# diagnostic tests
def test_modes():
    return 0

file = open("5.txt")
contents = file.read()
init = contents.split(',')
init = list(map(int, init))

desired_out = 19690720  # magic number = 19690720
found = False

for noun in range(100):  # from 0 to 99 inclusive
    init[1] = noun
    for verb in range(100):
        init[2] = verb
        intcode = init[:]
        # print("\n",intcode)
        
        for i in range(0, len(intcode()), num_instructions):
            opcode = str(intcode[i][-2:])
            
            # mode: 0 - position, 1 - value
            p1_mode = str(intcode[i][-3:-2])
            p2_mode = str(intcode[i][-4:-3])

            if p1_mode == '1' and p2_mode == '1':
                p1 = intcode[i+1]
                p2 = intcode[i+2]
            elif p1_mode == '0' and p2_mode == '1':
                p1 = intcode[intcode[i+1]]
                p2 = intcode[i+2]
            elif p1_mode == '1' and p2_mode == '0':
                p1 = intcode[i+1]
                p2 = intcode[intcode[i+2]]
            else:  # both in position mode
                p1 = intcode[intcode[i+1]]
                p2 = intcode[intcode[i+2]]

            # OPERATIONS
            # opcode 1: add parameter 1 and parameter 2 and save at position specified in parameter 3
            if opcode == '01':
                intcode[intcode[i+3]] = p1 + p2
                num_instructions = 4
                
            # opcode 2: multiply parameter 1 and parameter 2 and save at position specified in parameter 3
            elif opcode == '02':
                intcode[intcode[i+3]] = p1 * p2
                num_instructions = 4
                
            # opcode 3: save input at position specified in parameter
            elif opcode == '03':
                intcode[intcode[i+1]] = int(input())
                num_instructions = 2
                
            # opcode 4: output value at only parameter
            elif opcode == '04':
                print(intcode[intcode[i+1]])
                num_instructions = 2
                
            # opcode 99: halt
            elif opcode == '99':
                break

        # output matches desired
        if intcode[0] == desired_out:
            found = True
            break
    if found:
        break

# print(intcode)
print(100 * intcode[1] + intcode[2])  # 100 * noun * verb (intcode[1], intcode[2])
