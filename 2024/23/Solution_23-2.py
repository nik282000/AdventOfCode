f = open('input_23-1', 'r')
puzzle = f.readlines()
f.close()

import networkx as nx

connections = {}

'''
Looked up python graphs, found networkx references
https://stackoverflow.com/questions/71049155/generate-graph-from-a-list-of-connected-components
Checked docs for networkx and found 'cliques' -> looked for larest clique
'''

g = nx.Graph() # https://networkx.org/documentation/stable/tutorial.html

for p in puzzle:
    c = p.strip().split('-')
    if not c[0] in connections.keys():
        connections[c[0]] = [c[1]]
    else:
        connections[c[0]] += [c[1]]
    if not c[1] in connections.keys():
        connections[c[1]] = [c[0]]
    else:
        connections[c[1]] += [c[0]]

for c in connections:
    g.add_node(c)

for c in connections:
    for i in range(len(connections[c])):
        g.add_edge(c, connections[c][i])

groups = list(nx.find_cliques(g)) # https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.clique.find_cliques.html#networkx.algorithms.clique.find_cliques

max = 0
lan = []
for g in groups:
    if len(g) > max:
        max = len(g)
        lan = g

lan.sort()
for l in lan:
    print(f'{l},', end='') # Leaves a trailing , that should be removed
