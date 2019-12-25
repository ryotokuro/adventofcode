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

# print(graph.keys())
orbits = 0
level = 1

head = 'COM'

reset = head
children = graph[head]
for c in children:
    print(c)
    orbits += level

head = children[0]

"""
while True:
    print(level, ': ', head, sep='')  # print level and head
    reset = head
    children = graph[head]  # keep head in case we need to go back (multiple children)
    print(children)  # list of children e.g. ['C', 'G']

    # into the nodes
    for child_index in range(len(children)):
        print(child_index)  # node position in children list
        
        for c in children:  # for each child node
            orbits += level  # add level

        
        # move
        for i in children:
            if not children:
                head = reset
            else:
                head = children[child_index]
 
        
    level += 1
print(orbits)
"""
"""
while True:
    print(level, ': ', curr, sep='')
    for i in curr:  # go through items in the list
        print(i)
        orbits += level * len(i)
    #curr = 
    level += 1
"""

"""
for key, val in graph.items():
    print(val)
    #for i in val:
        #orbits += level * len(graph[k])
    level += 1
#print(graph)
print(orbits)
"""


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

