f = open('input_24-1', 'r')
puzzle = f.readlines()
f.close()

parse_mode = 0

nodes = {}
rules = []
value = 0

'''
Parsing inputs hard to do
In the Christmas season
Slicing strings and skipping lines
Without any reason
'''

for p in puzzle:
    if parse_mode == 0:
        if p == '\n':
            parse_mode = 1
        else:
            nodes[p[0:3]] = bool(int(p[-2]))
    elif parse_mode == 1:
        if not p.strip().split()[0] in nodes.keys():
            nodes[p.strip().split()[0]] = None
        if not p.strip().split()[2] in nodes.keys():
            nodes[p.strip().split()[2]] = None
        if not p.strip().split()[4] in nodes.keys():
            nodes[p.strip().split()[4]] = None
        rules.append([p.strip().split()[0], p.strip().split()[1], p.strip().split()[2], p.strip().split()[4]])

def evaluator (x, o, y):
    if x is None or y is None:
        return None
    if o == 'OR':
        return x or y
    elif o == 'AND':
        return x and y
    elif o == 'XOR':
        return x != y

while None in nodes.values(): # Keep looping over the rules until all nodes are populated with True or False
    for r in rules:
        if nodes[r[3]] is None:
            nodes[r[3]] = evaluator(nodes[r[0]], r[1], nodes[r[2]])

for n in nodes: # Sum up z** values
    if n[0] == 'z':
        if nodes[n]:
            value += 2 ** int(n[1:3])

print(value)
