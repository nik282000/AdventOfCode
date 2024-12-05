import re

puzzle = open('input_04-1', 'r')
#puzzle = open('example', 'r')
grid = puzzle.readlines()
puzzle.close

def mas_matcher(i): # Check 1x9 strings for X MASs
    # Match for M.M.A.S.S
    #           M.S.A.M.S
    #           S.S.A.M.M
    #           S.M.A.S.M
    matches = 0
    if re.search('M.M.A.S.S|M.S.A.M.S|S.S.A.M.M|S.M.A.S.M', i):
        matches = 1
    return matches

total = 0

for r in range(len(grid)):
    grid[r] = grid[r].strip()

g_width = len(grid[0])
g_height = len(grid)

for y in range(g_height - 2): # Slide a 3x3 box around the grid and make a 1x9 string
    for x in range(g_width - 2):
        segment = (grid[y][x:x+3])
        segment += (grid[y+1][x:x+3])
        segment += (grid[y+2][x:x+3])
        total += mas_matcher(segment)

print(total)