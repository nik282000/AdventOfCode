puzzle = open('input', 'r')
raw = puzzle.readlines()
puzzle.close

ranges = []
IDs = []

for i in raw:
    if "-" in i:
        ranges.append([int(i.strip().split('-')[0]), int(i.strip().split('-')[1])])
    elif i.strip() != "":
        IDs.append(int(i.strip()))

def debug_print(msg):
    if debug:
        print(msg)

debug = False

debug_print(ranges)
debug_print(IDs)

not_spoiled = set()

for i in IDs:
    for r in ranges:
        if i >= r[0] and i <= r[1]: # If an ID appears inside a range, add it to the list
            debug_print(f"{r} {i}")
            not_spoiled.add(i)

debug_print(not_spoiled)

print(len(not_spoiled))
