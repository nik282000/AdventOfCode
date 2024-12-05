rules = [] # list of rule number pairs
prints = [] # list of page numbers in order
total = 0

puzzle = open('input_05-1', 'r')
#puzzle = open('example', 'r')
for line in puzzle:
    if line.find('|') > 0:
        rules.append(line.strip().split('|'))
    elif line.find(',') > 0:
        prints.append(line.strip().split(','))
puzzle.close

for p in prints: # Loop over all print jobs
    valid_print = True
    for n in range(len(p)): # Check each page against the rules
        for r in rules:
            if p[n] == r[0] and r[1] in p: # If the page number is in a look ahead rule, check the rule
                if not (n < p.index(r[1])):
                    valid_print = False
            if p[n] == r[1] and r[0] in p: # Look behind rules
                if not (n > p.index(r[0])):
                    valid_print = False
    if valid_print:
        total += int(p[int(len(p)/2)])

print(total)
