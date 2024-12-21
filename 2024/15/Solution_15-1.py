f = open('input_15-1', 'r')
puzzle = f.readlines()
f.close

map = [] # YX grid containing status of each tile
         # . = empty, # = wall, O = box
rules = [] # List of robot rules
robot = [] # [Px, Py]

parse_mode = 0 # Start parsing map data
               # then switch to r-instructions

x = 0
y = 0

for p in puzzle:
    if len(p.strip()) == 0:
        parse_mode = 1
    if parse_mode == 0:
        row = []
        line = p.strip()
        for c in line:
            if c == "@":
                row.append(c)
                robot = [x, y]
            else:
                row.append(c)
            x += 1
        map.append(row)
        x = 0
        y += 1
    else:
        line = p.strip()
        for c in line:
            rules.append(c)

def show_map():
    for y in range(len(map)):
        row = ''
        for x in range(len(map[0])):
            row += map[y][x]
        print(row)

def direction(d): # Turn ^ > v < into useable directions
    out = []
    if d == '^':
        out = [0, -1]
    elif d == '>':
        out = [1, 0]
    elif d == 'v':
        out = [0, 1]
    elif d == '<':
        out = [-1, 0]
    return out

def box_check(d, r): # Starting at robot's position check if box in
                     # direction d has any open spaces in which to move
                     # Loop ends when an empty space '.' or wall '#' is found
                     # Return empty space [x,y] or False for no space
    #print'check for room to move boxes')
    p = [r[0] + d[0], r[1] + d[1]]
    while map[p[1]][p[0]] == 'O':
        p[0] += d[0]
        p[1] += d[1]
    if map[p[1]][p[0]] == '.':
        return p
    else:
        return False




# Load movement, if next space is empty them move
# If next space is a wall do nothing
# If next sapce is a box, begin box logic
#   If check in move direction for next available space
#       Space present -> delete box next to robot, fill space and end of line of boxes
#       No spacee -> do nothing

for s in rules:
    dir = direction(s)
    # Check for empty
    if map[robot[1] + dir[1]][robot[0] + dir[0]] == '.':
        map[robot[1]][robot[0]] = '.'
        map[robot[1] + dir[1]][robot[0] + dir[0]] = '@'
        robot[0] += dir[0]
        robot[1] += dir[1]
    # Check for boxes
    elif map[robot[1] + dir[1]][robot[0] + dir[0]] == 'O':
        box = box_check(dir, robot)
        if box: # If there is a space at the end of a line of boxes put a box there and move the robot
            map[box[1]][box[0]] = 'O'
            map[robot[1]][robot[0]] = '.'
            map[robot[1] + dir[1]][robot[0] + dir[0]] = '@'
            robot[0] += dir[0]
            robot[1] += dir[1]

gps_total = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 'O':
            gps_total += (y * 100) + (x)
print(gps_total)
