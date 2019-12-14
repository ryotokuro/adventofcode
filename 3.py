import os
import itertools

intersections = []

content = (open("3.txt").read()).split()

first = content[0].split(',')
second = content[1].split(',')
print(first)

# origin is [0, 0]
# intersect when c1 == c2
c1 = {'x': 0,'y': 0}
c2 = {'x': 0,'y': 0}
print(second)

def y_equal():
    return c1['y'] == c2['y']

def x_equal():
    return c1['x'] == c2['x']


for a, b in itertools.zip_longest(first, second):
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

# find smallest distance
# minimum x + y coord is closest intersection
