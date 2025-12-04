f = open('input', 'r')
data = f.readlines()
f.close

height = len(data)
width = len(data[0]) - 1

map = []
for y in range(height): # Translate map to array
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

to_be_removed = [] # List of rolls to be removed
loop = True

while loop == True:
    for i in range(height):
        for j in range(width):
            if map[i][j] == '@':
                if check_adj(j,i) < 4:
                    total += 1 # Count up accessible rolls (rolls to be removed)
                    to_be_removed.append([j,i]) # Add accessible roll to list

    if len(to_be_removed) > 0: # If there are accessible rolls, removed them
        for k in to_be_removed:
            debug_print(k)
            map[k[1]][k[0]] = '.'            
    else: # Else we're done
        loop = False

    to_be_removed = []

print(total)
