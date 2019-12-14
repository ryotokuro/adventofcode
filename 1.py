import os
import math

# fuel_required = floor(mass / 3) - 2
def calculate_fuel(mass):
    """Calculate fuel using input mass"""
    return math.floor(mass/3) - 2

# open input file and read
file = open('1.txt')
contents = file.read()

# configure input for calculations
modules = contents.split('\n')
modules = map(int, modules)  # make all of them integers

total = 0
for mass in modules:
    fuel = calculate_fuel(mass)
    while fuel > 0:
        total += fuel
        fuel = calculate_fuel(fuel)

print(total)
