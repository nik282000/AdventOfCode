puzzle = open('input_06-1', 'r')
map = puzzle.readlines()
puzzle.close

world = []
height = len(map)
width = len(map[0]) - 1
in_bounds = True
g_x = 0
g_y = 0
g_di = 0 # guard direction index
g_dd = [[0,-1],[1,0],[0,1],[-1,0]] # guard direction...direction :/
unique_total = 0

for y in range(len(map)):
    map[y] = map[y].strip()
    row = []
    for x in range(len(map[y])):
        if not (map[y][x] == '.' or map[y][x] == '#'):
            g_x = x
            g_y = y
            row.append('X')
            match map[y][x]:
                case '^':
                    g_di = 0
                case '>':
                    g_di = 1
                case 'v':
                    g_di = 2
                case '<':
                    g_di = 3
        else:
            row.append(map[y][x])
    world.append(row)

while in_bounds:
    if world[g_y + g_dd[g_di][1]][g_x + g_dd[g_di][0]] == '.' or world[g_y + g_dd[g_di][1]][g_x + g_dd[g_di][0]] == 'X':
        g_x += g_dd[g_di][0]
        g_y += g_dd[g_di][1]
        world[g_y][g_x] = 'X'
    elif world[g_y + g_dd[g_di][1]][g_x + g_dd[g_di][0]] == '#':
        g_di = (g_di + 1) % 4

    if g_x + g_dd[g_di][0] < 0 or g_x + g_dd[g_di][0] == width or g_y + g_dd[g_di][1] < 0 or g_y + g_dd[g_di][1] == height:
        in_bounds = False

for y in world:
    for x in y:
        if x == "X":
            unique_total += 1

print(unique_total)
