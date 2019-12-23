"""
6.py: Universal Orbit Map
Link: https://adventofcode.com/2019/day/6
"""
# if not the last letter in the list
# and already exists, then find and create new list

# COM)B)C)D)E)F
# COM)B)G)H
# COM)B)C)D)I
# COM)B)C)D)E)J)K)L

# BFT (breadth first traversel?)
# Node class for tree nodes
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:  # as long as data is not none
            # we can do comparison on ascii value
            if chr(ord(self.data)+1) == data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                find_parent(data) # reset and traverse

    def find_parent(self, data):
        # bfs or dfs
        
    def print_tree(self):
        print(self.data)

# if i start from B, I need to add the length of the tree
# e.g. removing com gives me 31, to which I then need 11
# - the 11 then comes from adding the length of the tree (B->L)
root = Node('B')
root.insert('C')
root.print_tree()
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

