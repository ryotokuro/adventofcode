"""
6.py: Universal Orbit Map
Link: https://adventofcode.com/2019/day/6
"""

from collections import defaultdict
import os

with open('6.txt') as file:
    nodes = file.read().split('\n')

graph = defaultdict(list)

for i in nodes:
    graph[i[:i.find(')')]].append(i[i.find(')')+1:])

print(graph.keys())
orbits = 0
for k in graph.keys():
    indirect = 
#print(graph)


# if not the last letter in the list
# and already exists, then find and create new list

# COM)B)C)D)E)F
# COM)B)G)H
# COM)B)C)D)I
# COM)B)C)D)E)J)K)L


# if i start from B, I need to add the length of the tree
# e.g. removing com gives me 31, to which I then need 11
# - the 11 then comes from adding the length of the tree (B->L)


# given B)C
# if self.data == orbit[:1]  # i.e. current node is the one to add onto
# else:
# reset to top node and traverse again

# algorithm:
# - define the tree structure
# - COM is head
# - going through the map, I will add the leaves respectively
# - B to C, C to D, D to E...
# - once I hit a branch that I'm not on, i'll reset (e.g. B to G)
#  >> find B first then add G and continue

