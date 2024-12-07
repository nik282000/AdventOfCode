import copy

puzzle = open('input_06-1', 'r')
map = puzzle.readlines()
puzzle.close

'''
world is made of steps/tiles/squares with 5 boolean values
0 - true if object present, false if clear
1 - true if guard passed by moving up (-y)
2 - true if guade passed by moving right (+x)
3 - true if guade passed by moving down (+y)
4 - true if guade passed by moving left (-x)
'''
world = [] # Used to find all the unique locations
og_world = [] # Fresh map for checking loops

'''
guard has several values
g_x and g_y are current position
g_di is the direction index, 1 up, 2 right, 3 down, 4 left
g_dd translates the direction index into an x,y movement
'''

g_x = 0
g_y = 0
g_di = 0 # guard direction index
g_dd = [[0,-1],[1,0],[0,1],[-1,0]] # guard direction...direction  ^ > v <

height = len(map)
width = len(map[0]) - 1
in_bounds = True
unique_total = 1
unique_list = []
possible_loops = 0

def show_world(w):
    print('')
    for y in range(height):
        map_row = ''
        dir_row = ''
        for x in range(width):
            if w[y][x][0]:
                map_row += '#'
            else:
                if (w[y][x][1] or w[y][x][3]) and not (w[y][x][2] or w[y][x][4]):
                    map_row += '|'
                elif (w[y][x][2] or w[y][x][4]) and not(w[y][x][1] or w[y][x][3]):
                    map_row += '-'
                elif not (w[y][x][1] or w[y][x][2] or w[y][x][3] or w[y][x][4]):
                    map_row += '.'
                elif (w[y][x][1] or w[y][x][3]) and (w[y][x][2] or w[y][x][4]):
                    map_row += '+'
        print(f'{map_row}')

def alt_world(a_world, a_y, a_x, a_di, o_y, o_x): # Spin up an alternate universe to test what happens with a new object
    solved = False
    a_world[o_y][o_x][0] = True # New object placed in path
    while not solved:
        if a_world[a_y + g_dd[a_di][1]][a_x + g_dd[a_di][0]][0]: # If next step in current direction is an object
            a_di = (a_di + 1) %4 # Rotate CW
        else: # Else move in current direction
            a_y += g_dd[a_di][1]
            a_x += g_dd[a_di][0]

            if a_world[a_y][a_x][a_di + 1]: # Check if this tile has been visited in this direction
                solved = True
                return 1

        if a_y + g_dd[a_di][1] < 0 or a_y + g_dd[a_di][1] == height or a_x + g_dd[a_di][0] < 0 or a_x + g_dd[a_di][0] == width: # Check for oob next step
            solved = True
            return 0
        a_world[a_y][a_x][a_di + 1] = True # Mark current direction at current location


for y in range(len(map)): # Import ASCII map into world array
    map[y] = map[y].strip() # Drop the trailing \n
    row = [] # Temporary list to build the worls
    for x in range(len(map[y])):
        if not (map[y][x] == '.' or map[y][x] == '#'): # Find the guard position and direction g_y, g_x, g_di
            g_x = x
            g_y = y
            match map[y][x]: # Determine direction, also set direction bool in world for starting point
                case '^':
                    g_di = 0
                    row.append([False, True, False, False, False])
                case '>':
                    g_di = 1
                    row.append([False, False, True, False, False])
                case 'v':
                    g_di = 2
                    row.append([False, False, False, True, False])
                case '<':
                    g_di = 3
                    row.append([False, False, False, False, True])
        elif map[y][x] == '.': # empty tile
            row.append([False, False, False, False, False])
        elif map[y][x] == "#": # occupied tile
            row.append([True, False, False, False, False])
    world.append(row)
    
og_world = copy.deepcopy(world)
s_x = g_x
s_y = g_y
s_i = g_di

while in_bounds:
    if world[g_y + g_dd[g_di][1]][g_x + g_dd[g_di][0]][0]: # If next step in current direction is an object rotate
        g_di = (g_di + 1) % 4
    else: # Else check for a potential loop then move in current direction
        g_y += g_dd[g_di][1]
        g_x += g_dd[g_di][0]

    if not (world[g_y][g_x][1] or world[g_y][g_x][2] or world[g_y][g_x][3] or world[g_y][g_x][4]): # Make a list of all the unique tiles that are touched
        unique_total += 1
        unique_list.append([g_x,g_y])

    if g_y + g_dd[g_di][1] < 0 or g_y + g_dd[g_di][1] == height or g_x + g_dd[g_di][0] < 0 or g_x + g_dd[g_di][0] == width: # Check if next step is out of bounds
        in_bounds = False

    world[g_y][g_x][g_di+1] = True # Mark current direction at current location
    #show_world(world)

for p in unique_list: # Test all tiles to see if a loop can be made
    print(p)
    possible_loops += alt_world(copy.deepcopy(og_world), s_y, s_x, s_i, p[1], p[0])

print(unique_total)
print(possible_loops)
