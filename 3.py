import os
import itertools

# i need to draw the first line first
# then worry about the second line
for i in first:
    += 1
    append()

# origin is [0, 0]
# intersect when c1 == c2
intersections = []
c1 = {'x': 0,'y': 0}
c2 = {'x': 0,'y': 0}

def test_paths():
    assert find_intersections(['R8','U5','L5','D3'],['U7','R6','D4','L4']) == [{'x': 3,'y': 3}], "Wrong intersection points"

def setup():
    content = (open("3.txt").read()).split()

    l1 = content[0].split(',')
    l2 = content[1].split(',')
    print(l1)
    print(l2)

def y_equal():
    return c1['y'] == c2['y']

def x_equal():
    return c1['x'] == c2['x']

def find_intersections(l1, l2):
    for a, b in itertools.zip_longest(l1, l2):
        try:
            move1 = a[:1]
            if move1 == 'L':  
                if y_equal():
                    if c2['x'] > c1['x'] - int(a[1:]):
                        intersections.append(c2)
                c1['x'] -= int(a[1:])
                
            elif move1 == 'R':
                if y_equal():
                    if c2['x'] < c1['x'] + int(a[1:]):
                        intersections.append(c2)
                c1['x'] += int(a[1:])
                
            elif move1 == 'U':
                if x_equal():
                    if c2['y'] < c1['y'] + int(a[1:]):
                        intersections.append(c2)
                c1['y'] += int(a[1:])
                
            elif move1 == 'D':
                if x_equal():
                    if c2['y'] > c1['y'] + int(a[1:]):
                        intersections.append(c2)
                c1['y'] -= int(a[1:])
            
        except TypeError:
            pass
        
        try:
            move2 = b[:1]
            if move2 == 'L':  
                if y_equal():
                    if c2['x'] > c1['x'] - int(b[1:]):
                        intersections.append(c1)
                c2['x'] -= int(b[1:])
                
            elif move2 == 'R':
                if y_equal():
                    if c2['x'] < c1['x'] + int(b[1:]):
                        intersections.append(c1)
                c2['x'] += int(b[1:])
                
            elif move2 == 'U':
                if x_equal():
                    if c2['y'] < c1['y'] + int(b[1:]):
                        intersections.append(c1)
                c2['y'] += int(b[1:])
                
            elif move2 == 'D':
                if x_equal():
                    if c2['y'] > c1['y'] + int(b[1:]):
                        intersections.append(c1)
                c2['y'] -= int(b[1:])            
        except TypeError:
            pass

    print(c1, c2)
    print(intersections)
    return intersections

setup()
# find_intersections()
test_paths()
# find smallest distance
# minimum x + y coord is closest intersection
