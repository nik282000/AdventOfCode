f = open('input_12-1', 'r')
puzzle = f.readlines()
f.close

height = len(puzzle)
width = len(puzzle[0]) - 1


map = [] # Puzzle Data
info_map =[] # [y][x][lable, ID_number, perimiters, sides orientations, corners]
ID_index = -1

for y in range(height): # Init map and info_map
    row = []
    info_row = []
    for x in range(width):
        row.append(puzzle[y][x])
        info_row.append(['', -1, 0, [], 0])
    map.append(row)
    info_map.append(info_row)

def show_map(m):
    for i in range(height):
        row = ''
        for j in range(width):
            row += m[i][j]
        print(row)

def check_pos(x, y): # Check each positionr, eturn perimiter length 
                     # and list of like neighbours and a list of the sides
    info = [0,[],[]] # [perimiter,[[x0,y0], [x1,y1], ...], [sides]]
                     # Info contains the number of perimiter lines
                     # plus a list of adjoining blocks of the same label
                     # Sides top, right, bottom, left = 0, 1, 2, 3
    if y - 1 < 0:
        info[0] += 1
        info[2].append(0)
    else:
        if map[y][x] == map[y-1][x]:
            info[1].append([x, y-1])
        else:
            info[0] += 1
            info[2].append(0)
    if y + 1 == height:
        info[0] += 1
        info[2].append(2)
    else:
        if map[y][x] == map[y+1][x]:
            info[1].append([x, y+1])
        else:
            info[0] += 1
            info[2].append(2)
    if x - 1 < 0:
        info[0] += 1
        info[2].append(3)
    else:
        if map[y][x] == map[y][x-1]:
            info[1].append([x-1, y])
        else:
            info[0] += 1
            info[2].append(3)
    if x + 1 == width:
        info[0] += 1
        info[2].append(1)
    else:
        if map[y][x] == map[y][x+1]:
            info[1].append([x+1, y])
        else:
            info[0] += 1
            info[2].append(1)
    return info

def get_corners(x, y): # How many god damned coners does a square have?
                       # 4 sides has 4 corners, always
                       # 3 sides has 2 corners, always
                       # 2 sides
                       #    Parallel sides have no corners
                       #    Perpendicular sides ARE a corner except when there is another
                       # 1 side has 0 corners always, HA NO IT DOESNT
                       # 0 sides has 1 inside corner for each unlike diagonal
    sides = info_map[y][x][3]
    ID = info_map[y][x][1]
    len_sides = len(sides)
    corners = 0
    if len_sides == 0:
        if not ID == info_map[y-1][x-1][1]:
            corners += 1
        if not ID == info_map[y-1][x+1][1]:
            corners += 1
        if not ID == info_map[y+1][x+1][1]:
            corners += 1
        if not ID == info_map[y+1][x-1][1]:
            corners += 1
    if len_sides == 1:
        print('godamnit')
        if 0 in sides:
            if not info_map[y][x][1] == info_map[y+1][x-1][1]:
                corners += 1
            if not info_map[y][x][1] == info_map[y+1][x+1][1]:
                corners += 1     
        elif 1 in sides:
            if not info_map[y][x][1] == info_map[y-1][x-1][1]:
                corners += 1
            if not info_map[y][x][1] == info_map[y+1][x-1][1]:
                corners += 1
        elif 2 in sides:
            if not info_map[y][x][1] == info_map[y-1][x-1][1]:
                corners += 1
            if not info_map[y][x][1] == info_map[y-1][x+1][1]:
                corners += 1
        elif 3 in sides:
            if not info_map[y][x][1] == info_map[y-1][x+1][1]:
                corners += 1
            if not info_map[y][x][1] == info_map[y+1][x+1][1]:
                corners += 1
    if len_sides == 2:
        if (0 in sides and 2 in sides) or (1 in sides and 3 in sides): # Parallel
            corners = 0
        elif (0 in sides and 1 in sides) and not (info_map[y][x][1] == info_map[y+1][x-1][1]):
            corners += 2
        elif (1 in sides and 2 in sides) and not (info_map[y][x][1] == info_map[y-1][x-1][1]):
            corners += 2
        elif (2 in sides and 3 in sides) and not (info_map[y][x][1] == info_map[y-1][x+1][1]):
            corners += 2
        elif (3 in sides and 0 in sides) and not (info_map[y][x][1] == info_map[y+1][x+1][1]):
            corners += 2
        else:
            corners = 1
    if len_sides == 3:
        corners = 2
    if len_sides == 4:
        corners = 4
    return corners # Fuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu

def get_info(ID, x,y): # Take in a new ID number and x,y
                       # Apply ID to x,y then check neighbours
                       # If check returns neighbours, get_info(ID, new_x, new_y)
    info = check_pos(x,y)
    info_map[y][x][0] = map[y][x] # Apply map lable to info_map
    info_map[y][x][1] = ID # Apply region ID to info_map
    info_map[y][x][2] = info[0] # Apply perimeter to info_map
    info_map[y][x][3] = info[2]
    if len(info[1]) > 0: # If there are neighbours of the same lable, check them
        for i in info[1]:
            if info_map[i[1]][i[0]][1] == -1: # If they have not been previously checked
                get_info(ID, i[0], i[1])

#------------------------------------------------------------------------------

show_map(map)

for y in range(height):
    info = []
    for x in range(width):
        if info_map[y][x][1] == -1:
            #print('New Region ')
            ID_index += 1 # Assign new ID number, start mapping
            get_info(ID_index, x, y)

sides_done = []
for y in range(height):
    for x in range(width):
            info_map[y][x][4] = get_corners(x,y)

totals = [] # totals per regions [Area, Perimeters, Corners]
cost = 0
for i in range(ID_index + 1): # Empty list to collect totals totals[ID] = [area, perimeter]
    totals.append([0, 0, 0])

for y in range(height):
    for x in range(width):
        totals[info_map[y][x][1]][0] += 1 # Area for region
        totals[info_map[y][x][1]][1] += info_map[y][x][2] # Perimeter for region
        totals[info_map[y][x][1]][2] += info_map[y][x][4] # Corners (segments) for region

for t in totals:
    cost += t[0] * t[2]

print(cost)
