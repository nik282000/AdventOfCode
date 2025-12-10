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

debug = False

debug_print(corner_list)

largest = 0

for c in range(len(corner_list)):
    for d in range(c + 1, len(corner_list)):
        a = area(corner_list[c][0], corner_list[c][1], corner_list[d][0], corner_list[d][1])
        debug_print(f'{corner_list[c]}-{corner_list[d]} {a}')
        if a > largest:
            largest = a
            
print(largest)
