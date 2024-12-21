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
                row.append('@')
                row.append('.')
                robot = [x * 2, y]
            elif c == 'O':
                row.append('[')
                row.append(']')
            else:
                row.append(c)
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

def box_check(d, s): # Part 2, ha ha, nope, now its gotta be recursive!
                     # If d is L/R see if there is an empty space, if so, return list of box-halfs to move
                     # If d is L/R and shuffle is not possible report False
                     # If d is U/D start a branching search to see how many full and half overlaps exist
                     # If there are 0 blockages at the end of each branch return a list of all box halfs to move
                     # If there are any blockages return False
    p = [s[0], s[1]] # Start posision
    box_halfs = []

    if d[1] == 0: # Left/right move
        while (map[p[1] + d[1]][p[0] + d[0]] == '[') or (map[p[1] + d[1]][p[0] + d[0]] == ']'):
            p[0] += d[0]
            p[1] += d[1]
            box_halfs.append([p[0], p[1]])
        if map[p[1] + d[1]][p[0] + d[0]] == '#': # Bail, there's a wall
            return False
        if d[0] == -1:
            # sort left to right to help box shuffle
            box_halfs.sort(key = lambda row: row[0])
        elif d[0] == 1:
            # sort right to left to help bx shuffle
            box_halfs.sort(key = lambda row: row[0])
            box_halfs = box_halfs[::-1]
        return box_halfs


    else: # Up/Down move, begin the recursiveing
        p[0] += d[0] # Move up/down to the box's position
        p[1] += d[1]
        if map[p[1]][p[0]] == '.': # If this space is empty return the space that we were checking from
            return [s]
        elif map[p[1]][p[0]] == '#': # If this space is a wall nope out
            return False
        elif map[p[1]][p[0]] == '[': # Add both halfs of box to the list then check the space above/below
            box_halfs.append([p[0], p[1]])
            box_halfs.append([p[0] + 1, p[1]])
            check_l = box_check(d, [p[0], p[1]])
            check_r = box_check(d, [p[0] + 1, p[1]])
           
        elif map[p[1]][p[0]] == ']': # Ditto but for the other mirror
            box_halfs.append([p[0], p[1]])
            box_halfs.append([p[0] - 1, p[1]])
            check_r = box_check(d, [p[0], p[1]])
            check_l = box_check(d, [p[0] - 1, p[1]])
        
        if check_l and check_r: # If the checked spaces are good add them to the list
            box_halfs += check_l
            box_halfs += check_r
            # Remove duplicates
            box_halfs = [list(x) for x in set (tuple(x) for x in box_halfs)]
            # Sort according to the order they need to be moved
            box_halfs.sort(key = lambda row: row[1])
            if d[1] == 1:
                box_halfs = box_halfs[::-1]
            return box_halfs
        else: # If either half runs into a wall nope out completely, no need to check further
            return False


def box_shuffle(d, box_halfs): # Move all box halfs in direction d starting with the furthest halfs
    if d[1] == 0: # Left/Right move
        for b_h in box_halfs:
            map[b_h[1]][b_h[0]], map[b_h[1] + d[1]][b_h[0] + d[0]] = map[b_h[1] + d[1]][b_h[0] + d[0]], map[b_h[1]][b_h[0]]
    elif d[0] == 0: # Left/Right move
        for b_h in box_halfs:
            map[b_h[1]][b_h[0]], map[b_h[1] + d[1]][b_h[0] + d[0]] = map[b_h[1] + d[1]][b_h[0] + d[0]], map[b_h[1]][b_h[0]]


# Load movement, if next space is empty them move
# If next space is a wall do nothing
# If next sapce is a box, begin box logic
#   If check in move direction for next available space
#       Space present -> delete box next to robot, fill space and end of line of boxes
#       No spacee -> do nothing

for s in rules:
    dir = direction(s)
    # Check for empty space
    if map[robot[1] + dir[1]][robot[0] + dir[0]] == '.':
        map[robot[1]][robot[0]] = '.'
        map[robot[1] + dir[1]][robot[0] + dir[0]] = '@'
        robot[0] += dir[0]
        robot[1] += dir[1]
    # JFC a box
    elif (map[robot[1] + dir[1]][robot[0] + dir[0]] == '[') or map[robot[1] + dir[1]][robot[0] + dir[0]] == ']':
        check = box_check(dir, robot) # Check if there are boxes that CAN be moved
        if check: # Oh god they can move, move them, then move the robot
            box_shuffle(dir, check) # Take a sorted list of box_halfs and move them in the right direction
            map[robot[1]][robot[0]] = '.'
            map[robot[1] + dir[1]][robot[0] + dir[0]] = '@'
            robot[0] += dir[0]
            robot[1] += dir[1]

gps_total = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '[':
            gps_total += (y * 100) + (x)
print(gps_total)
