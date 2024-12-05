rules = [] # list of rule number pairs
prints = [] # list of page numbers in order
broken_prints = [] # list of pages to be fixed
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
    if not valid_print:
        broken_prints.append(p)

for p in broken_prints: # Same logic as above but swap the numbers if they violate a rule
    fixed = 1 # Gotta start somewhere :/
    while fixed > 0: # If no fixes were made on this pass then the pages are sorted
        fixed = 0 # Every time a swap is made fixed gets incremented
        for n in range(len(p)):
            for r in rules:
                if p[n] == r[0] and r[1] in p:
                    if not (n < p.index(r[1])):
                        p[n], p[p.index(r[1])] = p[p.index(r[1])], p[n]
                        fixed += 1
                if p[n] == r[1] and r[0] in p:
                    if not (n > p.index(r[0])):
                        p[n], p[p.index(r[0])] = p[p.index(r[0])], p[n]
                        fixed += 1
    total += int(p[int(len(p)/2)])

print(total)
