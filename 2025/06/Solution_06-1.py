f = open('input', 'r')
data = f.readlines()
f.close

problems = []

for r in data:
    problems.append(r.split())

def debug_print(msg):
    if debug:
        print(msg)

debug = False

debug_print(problems)

total = 0

for p in range(len(problems[0])):
    debug_print(f'{problems[0][p]} {problems[1][p]} {problems[2][p]} {problems[3][p]}')
    if problems[-1][p] == "+":
        total += int(problems[0][p]) + int(problems[1][p]) + int(problems[2][p]) + int(problems[3][p])
    elif problems[-1][p] == "*":
        total += int(problems[0][p]) * int(problems[1][p]) * int(problems[2][p]) * int(problems[3][p])

print(total)
