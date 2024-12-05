puzzle = open('input_04-1', 'r')
#puzzle = open('example', 'r')
grid = puzzle.readlines()
puzzle.close

total = 0

v_grid = []  # 90 degree rotated
da_grid = [] # 45 degree rotated
db_grid = [] # -45 degree rotated

# Check H
for r in range(len(grid)):
    grid[r] = grid[r].strip()
    total += grid[r].count('XMAS')
    total += grid[r].count('SAMX')

g_width = len(grid[0])
g_height = len(grid)

# Check V
# Start at 0,0 and move down to build rows for the v_grid
for x in range(g_width):
    v_grid.append('')
    for y in range(g_height):
        v_grid[x] += grid[y][x]
    total += v_grid[x].count('XMAS')
    total += v_grid[x].count('SAMX')

# Check Da
# Use an algo I borrowed online to make diagonal slices of a recangular array
for l in range(1, (g_height + g_width)):
    da_grid.append('')
    y_start = max(0, l - g_height)
    line_len = min(l, (g_width - y_start), g_height)
    for e in range(0, line_len):
        da_grid[l-1] += grid[min(g_height, l) - e - 1][y_start + e]
    total += da_grid[l-1].count('XMAS')
    total += da_grid[l-1].count('SAMX')

grid = list(reversed(grid))

# Check Db
for l in range(1, (g_height + g_width)):
    db_grid.append('')
    y_start = max(0, l - g_height)
    line_len = min(l, (g_width - y_start), g_height)
    for e in range(0, line_len):
        db_grid[l-1] += grid[min(g_height, l) - e - 1][y_start + e]
    total += db_grid[l-1].count('XMAS')
    total += db_grid[l-1].count('SAMX')

print(total)