f = open('input', 'r')
data = f.readlines()
f.close

height = len(data)
width = len(data[0]) - 1

manifold = []
for y in range(height): # Translate map to array, manifold[y][x]. Y THEN X!
    row = []
    for x in range(width):
        row.append(data[y][x])
    manifold.append(row)
    
def debug_print(msg):
    if debug:
        print(msg)
        
def draw():
    for y in range(height):
        for x in range(width):
            print(manifold[y][x], end='')
        print('')

debug = False
total = 0

'''
Rules
Start Cond  if x,y == . and x,y-1 == S then x,y = |
Run Cond    if x,y == . and x,y-1 == | then x,y = |
Split Right if x,y == . and x-1,y == ^ and x-1,y-1 == | then x,y = |
Split Left  if x,y == . and x+1,y == ^ and x+1,y-1 == | then x,y = |
Count Split if x,y == ^ and x,y-1 == | then total += 1
'''

for y in range(1, height):
    for x in range(width):
        if manifold[y][x] == '.' and (manifold[y-1][x] == 'S' or manifold[y-1][x] == '|'):
            manifold[y][x] = '|'
        if x > 0 and manifold[y][x] == '.' and manifold[y][x-1] == '^' and manifold[y-1][x-1] == '|':
            manifold[y][x] = '|'
        if x < (width - 1) and manifold[y][x] == '.' and manifold[y][x+1] == '^' and manifold[y-1][x+1] == '|':
            manifold[y][x] = '|'
        if manifold[y][x] == '^' and manifold[y-1][x] == '|':
            total += 1

draw()
print(total)
