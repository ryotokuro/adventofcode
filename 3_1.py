import os
import itertools


# origin is [0, 0]
# intersect when c1 == c2
intersections = []
c1 = {'x': 0,'y': 0}
c2 = {'x': 0,'y': 0}

content = (open("3.txt").read()).split()

path1 = content[0].split(',')
path2 = content[1].split(',')
print(path1)
print(path2)

line1 = []
line2 = []

def test_paths():
    assert find_intersections(['R8','U5','L5','D3'],['U7','R6','D4','L4']) == [{'x': 3,'y': 3}], "Wrong intersection points"

def y_equal():
    return c1['y'] == c2['y']

def x_equal():
    return c1['x'] == c2['x']

def draw_line(path, line_id):
    # maybe i could store the start and end coords and then check inbetween ranges but might be slower
    # sacrificing space for time may be easier
    for instruction in path:
        direction = instruction[:1]
        magnitude = int(instruction[1:])
        if direction == 'L':
            for i in range(1, magnitude+1):
                if line_id:
                    c1['x'] -= 1
                    line1.append(c1)
                    print("LEFT:", line1)
                else:
                    c2['x'] -= 1
                    line2.append(c2)
                    
        elif direction == 'R':
            for i in range(1, magnitude+1):
                if line_id:
                    c1['x'] += 1
                    line1.append(c1)
                else:
                    c2['x'] += 1
                    line2.append(c2)

        elif direction == 'U':
            for i in range(1, magnitude+1):
                if line_id:
                    c1['y'] += 1
                    line1.append(c1)
                else:
                    c2['y'] += 1
                    line2.append(c2)

        else:  # assume 'D'
            for i in range(1, magnitude+1):
                if line_id:
                    c1['y'] -= 1
                    line1.append(c1)
                else:
                    c2['y'] -= 1
                    line2.append(c2)
'''
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
'''

draw_line(path1, True)
draw_line(path2, False)
'''
for i in line1:
    print(i)
    if i in line2:
        print(i)
'''

# find_intersections()
#test_paths()
# find smallest distance
# minimum x + y coord is closest intersection
