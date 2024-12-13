f = open('input_12-1', 'r')
puzzle = f.readlines()
f.close

height = len(puzzle)
width = len(puzzle[0]) - 1

map = [] # Puzzle Data
info_map =[] # [y][x][lable, ID_number, perimiters]
ID_index = -1

for y in range(height): # Init map and info_map
    row = []
    info_row = []
    for x in range(width):
        row.append(puzzle[y][x])
        info_row.append(['', -1, -1])
    map.append(row)
    info_map.append(info_row)

def show_map(m):
    for i in range(height):
        row = ''
        for j in range(width):
            row += m[i][j]
        print(row)

def check_pos(x, y): # Take in a map and x, y
                     # Return perimiter length and list of like neighbours
    info = [0,[]] # [[perimiter],[[x0,y0], [x1,y1], ...]]
                  # Info contains the number of perimiter lines
                  # plus a list of adjoining blocks of the same label
    if y - 1 < 0:
        info[0] += 1
    else:
        if map[y][x] == map[y-1][x]:
            info[1].append([x, y-1])
        else:
            info[0] += 1
    if y + 1 == height:
        info[0] += 1
    else:
        if map[y][x] == map[y+1][x]:
            info[1].append([x, y+1])
        else:
            info[0] += 1
    if x - 1 < 0:
        info[0] += 1
    else:
        if map[y][x] == map[y][x-1]:
            info[1].append([x-1, y])
        else:
            info[0] += 1
    if x + 1 == width:
        info[0] += 1
    else:
        if map[y][x] == map[y][x+1]:
            info[1].append([x+1, y])
        else:
            info[0] += 1
    return info

def get_info(ID, x,y): # Take in a new ID number and x,y
                       # Apply ID to x,y then check neighbours
                       # If check returns neighbours, get_info(ID, new_x, new_y)
    info = check_pos(x,y)
    info_map[y][x][0] = map[y][x] # Apply map lable to info_map
    info_map[y][x][1] = ID # Apply region ID to info_map
    info_map[y][x][2] = info[0] # Apply perimeter to info_map
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

totals = [] # [area in region, perimeter in region]
cost = 0
for i in range(ID_index + 1): # Empty list to collect totals totals[ID] = [area, perimeter]
    totals.append([0, 0])


for y in range(height):
    for x in range(width):
        totals[info_map[y][x][1]][0] += 1
        totals[info_map[y][x][1]][1] += info_map[y][x][2]

for t in totals:
    cost += t[0] * t[1]

print(cost)
