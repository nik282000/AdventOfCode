f = open('input', 'r')
data = f.readlines()
f.close

height = len(data)
width = len(data[0]) - 1

map = []
for y in range(height): # Translate map to array, map[y][x]
    row = []
    for x in range(width):
        row.append(data[y][x])
    map.append(row)


def debug_print(msg):
    if debug:
        print(msg)

def check_adj(x,y): # Check 3x3 grid
    num = 0
    xmin = -1
    xmax = 2
    ymin = -1
    ymax = 2

    if x == 0: # Boundry conditions, don't check outside of map
        xmin = 0
    elif x == width - 1:
        xmax = 1

    if y == 0:
        ymin = 0
    elif y == height - 1:
        ymax = 1

    for i in range (y + ymin, y + ymax):
        for j in range(x + xmin, x + xmax):
            if map[i][j]=='@':
                num += 1

    return num - 1 # Don't count position x,y

debug = False
total = 0

for i in range(height): # Totall up rolls with less than 4 neighbours
    for j in range(width):
        if map[i][j] == '@':
            if check_adj(j,i) < 4:
                print('x', end='')
                total += 1
            else:
                print('@', end='')
        else:
            print('.', end='')
    print('')

print(total)
