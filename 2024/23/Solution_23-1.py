f = open('input_23-1', 'r')
puzzle = f.readlines()
f.close()

connections = {}
tripples = []
valid = []

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

'''
For all keys in connections:
    check each value in the list to see if it has a connection to each other value in the list
    add tripple links to a new list

Sort Lists
Filter out duplicates
Filter for tripples that contain a t* name
'''

for c in connections:
    for i in range(len(connections[c]) - 1):
        for j in range(i + 1, len(connections[c])):
            if connections[c][j] in connections[connections[c][i]]:
                tripples.append([c, connections[c][i], connections[c][j]])

for t in tripples:
    t = t.sort()
tripples = [list(x) for x in set (tuple(x) for x in tripples)]

for t in tripples:
    if t[0][0] == 't' or t[1][0] == 't' or t[2][0] == 't':
        valid.append(t)

print(len(valid))
