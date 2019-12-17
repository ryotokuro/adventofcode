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
    assert closest_intersection() == 6, "Wrong distance"

def y_equal():
    return c1['y'] == c2['y']

def x_equal():
    return c1['x'] == c2['x']

# maybe i could store the start and end coords and then check inbetween ranges but might be slower
# sacrificing space for time may be easier
def draw_line(path, line_id):
    for instruction in path:
        direction = instruction[:1]
        magnitude = int(instruction[1:])
        
        for i in range(1, magnitude+1):
            if direction == 'L':
                if line_id:
                    c1['x'] -= 1
                    line1.append(tuple(c1.values()))
                else:
                    c2['x'] -= 1
                    line2.append(tuple(c2.values()))
                    
            elif direction == 'R':
                if line_id:
                    c1['x'] += 1
                    line1.append(tuple(c1.values()))
                else:
                    c2['x'] += 1
                    line2.append(tuple(c2.values()))

            elif direction == 'U':
                if line_id:
                    c1['y'] += 1
                    line1.append(tuple(c1.values()))
                else:
                    c2['y'] += 1
                    line2.append(tuple(c2.values()))

            else:  # assume 'D'
                if line_id:
                    c1['y'] -= 1
                    line1.append(tuple(c1.values()))
                else:
                    c2['y'] -= 1
                    line2.append(tuple(c2.values()))

def closest_intersection():
    intersections = []

    for i in line1:
        if i in line2:
            intersections.append(i)

    # find closest intersection point (min manhattan distance)
    return(sum(min(intersections, key = lambda t: t[0]+t[1])))
    

draw_line(path1, True)
draw_line(path2, False)

print(closest_intersection())
# test_paths()
