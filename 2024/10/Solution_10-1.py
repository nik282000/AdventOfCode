f = open('input_10-1', 'r')
data = f.readlines()
f.close

height = len(data)
width = len(data[0]) - 1

valid_paths = 0

map = []
for y in range(height): # Translate map to array of int
    row = []
    for x in range(width):
        row.append(int(data[y][x]))
    map.append(row)

for i in range(len(map)): # Show map of ints
    row = ''
    for j in range(len(map[0])):
        row += str(map[i][j])
    print(row)

def next(x, y): # Retrun a list of [[x0, y0], [x1, y1], ...] who's value is 1 greater than x,y or [] for dead end
    n = map[y][x]
    paths = []
    if y - 1 > -1 and (map[y - 1][x] == n + 1):
        paths.append([x, y - 1])        
    if y + 1 < height and (map[y + 1][x] == n + 1):
        paths.append([x, y + 1])        
    if x - 1 > -1 and (map[y][x - 1] == n + 1):
        paths.append([x - 1, y])        
    if x + 1 < width and (map[y][x + 1] == n + 1):
        paths.append([x + 1, y])
    return paths

def walk(l): # Take a list of 0 or more co-ord and try to walk
    paths = []
    #print(l)
    if len(l) > 0: # if the list is not empty
        for m in l:
            if map[m[1]][m[0]] == 9: # If path ends on a 9 is it valid
                paths.append(f'{m[0]}, {m[1]}') # Add the 9's location to a list (there will be dupes)
            else:
                paths += walk(next(m[0],m[1])) # Otherwise keep walking and add any returned 9 locations to the list
    return paths

for y in range(height):
    for x in range(width):
        if map[y][x] == 0:
            valid_paths += len(set(walk([[x,y]]))) # Cound up all the UNIQUE 9 coords

print(valid_paths)
