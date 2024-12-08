f = open('input_08-1', 'r')
puzzle = f.readlines()
f.close

map = [] # map[y][x]

for l in puzzle:
    row = []
    l = l.strip()
    for c in l:
        row.append(c)
    map.append(row)

antennas = {} # {'antenna name':[[x0,y0], [y1,y1], ...[xn,yn]]}
width = len(map[0])
height = len(map)
valid_total = 0

a_nodes = [] # List of all discovered anti-nodes

for y in range(height): # Make a dict of all antenna types and locations
    for x in range(width):
        if not map[y][x] == '.':
            if map[y][x] in antennas:
                antennas[map[y][x]].append([x,y])
            else:
                antennas.update({map[y][x]:[[x,y]]})

'''
Check all nodes agasinst all other nodes
Start ON one node and continue out towards antoher
useing the distance to the second node as the slope.
Keep incrementing until an anti-node falls OOB
'''
def antinodes(nodes, min_y, min_x,  max_y, max_x):
    total = []
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if not i == j:
                x = nodes[j][0]
                y = nodes[j][1]
                slope_x = nodes[j][0] - nodes[i][0]
                slope_y = nodes[j][1] - nodes[i][1]
                while x >= min_x and x < max_x and y >= min_y and y < max_y:
                    total.append([x,y])
                    x += slope_x
                    y += slope_y

    return total

for t in antennas: # Check all antenna groups
    a_nodes += antinodes(antennas[t], 0, 0, height, width)

for a_n in a_nodes: # Add anti-nodes to the map
    map[a_n[1]][a_n[0]] = "#"

'''
Anti-nodes that overlap antenna are coundted but anti-nodes that
overlap other anti-nodes are not counted. Putting them on the map
and then counting them is lazy but solves the problem.
'''
for y in range(height):
    row = ''
    for x in range(width):
        row += map[y][x]
        if map[y][x] == '#':
            valid_total += 1
    print(row)

print(valid_total)
