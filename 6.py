"""
6.py: Universal Orbit Map
Link: https://adventofcode.com/2019/day/6
"""

from collections import defaultdict
import os

with open('6.txt') as file:
    lines = file.read().split('\n')

graph = defaultdict(list)  # stores all nodes and links``


for i in lines:
    graph[i[:i.find(')')]].append(i[i.find(')')+1:])

# print(graph)

queue = []
orbits = 0
level = 1

queue.append('COM')

while queue:  # while queue is not empty
    head = queue[0]
    del queue[0]

    if graph[head]:  # if there are children
        for i in graph[head]:
            queue.append(i)
            level += 1
    orbits += level
    print(level, ':', head, "->", graph[head])

# to make 'C' the head, it's children[0]
# to make 'G' the head, it's children[1]
# level stays as 3
