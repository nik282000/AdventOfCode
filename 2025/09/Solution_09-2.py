'''
This does not work, like it gets the answer but it takes between 2 and 20 hours because I am bad at math
'''
puzzle = open('input', 'r')
raw = puzzle.readlines()
puzzle.close

corner_list = []

for r in raw:
    x,y = (r.strip().split(','))
    corner_list.append([int(x),int(y)])

def debug_print(msg):
    if debug:
        print(msg)

def area(x0, y0, x1, y1): # Calculate area, add 1 to include the exterior row/col of tile
    return (abs(x1 - x0) + 1) * (abs(y1 - y0) + 1)

def inside(rx0, ry0, rx1, ry1, px0, py0): # Check if a point falls inside a rectangle, on the edge is ignored
    x_min = min(rx0, rx1)
    x_max = max(rx0, rx1)
    y_min = min(ry0, ry1)
    y_max = max(ry0, ry1)
    if (px0 > x_min) and (px0 < x_max) and (py0 > y_min) and (py0 < y_max):
        debug_print(f'{px0},{py0} Inside {x_min},{y_min} {x_max},{y_max}')
        return True 
    return False

def check_edge(rx0, ry0, rx1, ry1, ex0, ey0, ex1, ey1): # Walk along edge, check if it falls inside the rect
    if ex0 == ex1: # Vertical line
        debug_print('vert')
        for i in range(min(ey0, ey1), max(ey0, ey1)):
            debug_print(f'{ex0},{i}')
            if inside(rx0, ry0, rx1, ry1, ex0, i):
                return True
    elif ey0 == ey1: # Horizontal line
        debug_print('horz')
        for i in range(min(ex0, ex1), max(ex0, ex1)):
            debug_print(f'{i},{ey0}')
            if inside(rx0, ry0, rx1, ry1, i, ey0):
                return True
    return False

debug = False
#debug = True

'''
Gonna find all rectangles, sort from biggest to smallest
Gonna find all the edges of the all-point-polygon
'''

rect_list = [] # [[area, x0, y0, x1, y1], ...] List of all posible rectangles
edge_list = [] # [[x0, x1, y0, y1], ...] List of edges between list of corners in order

for c in range(len(corner_list)):
    for d in range(c + 1, len(corner_list)):
        a = area(corner_list[c][0], corner_list[c][1], corner_list[d][0], corner_list[d][1])
        rect_list.append([a, corner_list[c][0], corner_list[c][1], corner_list[d][0], corner_list[d][1]])

rect_list.sort()
rect_list = list(reversed(rect_list))

for c in range(len(corner_list) - 1):
    edge_list.append([corner_list[c][0], corner_list[c][1], corner_list[c+1][0], corner_list[c + 1][1]])
edge_list.append([corner_list[-1][0], corner_list[-1][1], corner_list[0][0], corner_list[0][1]])

# K, now we have a list of rectangles sorted from large to small
# check if any of the all-gon edges pass through the rect

debug_print(check_edge(11, 1, 2, 5, 2, 3, 7, 3))

i = 0

for r in rect_list: # Check all rectangles from largest to smallest
    edge_intersect = False
    debug_print('')
    print(i / 250000) # Because it takes so long I need a progress meter
    i += 1
    for e in edge_list: # Check al edges to see if they pass into the rectangle
        edge_intersect = check_edge(r[1], r[2], r[3], r[4], e[0], e[1], e[2], e[3])
        debug_print(f'Edge {e} inside {r}: {edge_intersect}')
        if edge_intersect: # If an edge intersects the rectange then stop checking, dont care
            break
    if edge_intersect == False: # If no edges intersect with the rect then we found the one, only took 2 hours
        print(f'Edge {e} inside {r}: {edge_intersect}')
        print('This one ^')
        break
