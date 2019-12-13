import os
import math

# open input file and read
file = open('1.txt')
contents = file.read()

# configure input for calculations
modules = contents.split('\n')
modules = map(int, modules)  # make all of them integers

# fuel_required = floor(mass / 3) - 2
modules = [(math.floor(mass/3) - 2) for mass in modules]

# answer = sum of all
print(sum(modules))
