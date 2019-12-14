# Opcodes
# 1: add numbers from position n+1 and n+2 and store in position n+3
# 2: multiply numbers from position n+1 and n+2 and store in position n+3
# 99: program finished, halt
# else: something went wrong

# example case

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
        # not 185500
        
        i = 0
        while i < len(intcode):
            if intcode[i] == 1:
                intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]                    
            elif intcode[i] == 2:
                intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
            elif intcode[i] == 99:
                break

            i += 4  # process 4 at a time

        # output matches desired
        if intcode[0] == desired_out:
            found = True
            break
    if found:
        break

# print(intcode)
print(100 * intcode[1] + intcode[2])  # 100 * noun * verb (intcode[1], intcode[2])
