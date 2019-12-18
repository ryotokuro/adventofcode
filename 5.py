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


file = open("2.txt")
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
        
        for i in range(0, len(intcode()), 4):
            # opcode 2: add parameter 1 and parameter 2 and save at position specified in parameter 3
            if intcode[i] == 1:
                intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
                
            # opcode 2: multiply parameter 1 and parameter 2 and save at position specified in parameter 3
            elif intcode[i] == 2:
                intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
                
            # opcode 3: save input at position specified in parameter
            elif intcode[i] == 3:
                intcode[intcode[i+1]] = int(input())
                
            # opcode 4: output value at only parameter
            elif intcode[i] == 4:
                print(intcode[intcode[i+1]])
                
            # opcode 99: halt
            elif intcode[i] == 99:
                break

        # output matches desired
        if intcode[0] == desired_out:
            found = True
            break
    if found:
        break

# print(intcode)
print(100 * intcode[1] + intcode[2])  # 100 * noun * verb (intcode[1], intcode[2])
