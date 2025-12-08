puzzle = open('input', 'r')
raw = puzzle.readlines()
puzzle.close

nodes = [] #[[x0, y0, z0], [x1, y1, z1], ...]

for l in raw:
    nodes.append(l.strip().split(','))
    
for n in range(len(nodes)):
    nodes[n][0] = int(nodes[n][0])
    nodes[n][1] = int(nodes[n][1])
    nodes[n][2] = int(nodes[n][2])
    
def distance(x0, y0, z0, x1, y1, z1):
    dist = ((x0 - x1)**2 + (y0 - y1)**2 + (z0 - z1)**2) #**0.5 Omit the square root, not interested in actual distance just relative distance
    return dist
    
def debug_print(msg):
    if debug:
        print(msg)

debug = False
dist_list = [] # [[distance_between_nodes, node_a, node_b], ...]
circ_list = [] # [[node_a, node_b, ...], [node_c], [node_d, node_e, ...], ...]

for a in range(len(nodes) - 1): # Calculate node distances
    for b in range(a + 1, len(nodes)):
        dist_list.append([distance(nodes[a][0], nodes[a][1], nodes[a][2], nodes[b][0], nodes[b][1], nodes[b][2]), a, b])

for n in range(len(nodes)):
    circ_list.append([n])

dist_list.sort() # I'm lazy, I just stay in bed
    
'''
Starting with a sorted list of possible node connections from shortest to longes.
Check all  connections one at a time until all nodes are in one list, check to see if both nodes are already in the same circuit:
    If no, merge the circuits
'''

i = 0 # Start with the shortest connection

while len(circ_list) > 1: # THERE CAN ONLY BE ONE
    node_a = dist_list[i][1] # Get the two nodes from the connection list
    node_b = dist_list[i][2]
    debug_print(f'node a: {node_a}\tnode b: {node_b}')
    for c in range(len(circ_list)):
        if node_a in circ_list[c]:
            debug_print(f'Node a in circ: {c}')
            if node_b in circ_list[c]: # Unecessary check for debugging
                debug_print(f'Node b in circ: {c}')
                debug_print('Nodes in same circuit')
                pass
            else: # Necessary logic for getting stars
                for d in range(len(circ_list)): # Find the list that contains node_b
                    if node_b in circ_list[d]: # Found node_b's list, merge it's contents to node_a's list then remove node_b's list
                        debug_print(f'Node b in circ: {d}')
                        debug_print('Merge Circuits')
                        circ_list[c] = circ_list[c] + circ_list[d]
                        circ_list.pop(d)
                        break # Made a conneciton, quit trying
            break # Connection made or already exists, GTFO
    i += 1 # Next largest connection

debug_print(dist_list[i-1])

total = nodes[dist_list[i-1][1]][0] * nodes[dist_list[i-1][2]][0]

print(total)
