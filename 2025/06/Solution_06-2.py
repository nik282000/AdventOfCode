f = open('input', 'r')
data = f.readlines()
f.close

def debug_print(msg):
    if debug:
        print(msg)

'''
abc hijk
 de lmn
  f op
  g q
+   *

Each operation +/* occurs under the left most digit of a group of numbers
Numbers are read top to bottom right to left
cefg + bd + a
k * jn * imp * hloq

Find the begining of each block of numbers by looking for + or * and note the block position
Use that position to work through the blocks and decode numbers
Number of digits AND number of number is variable, be smarter

block width = problems[n][0] to problems[n+1][0] - 2
'''

debug = False

problems = [] # no kidding [[index, operation, num, num, num, ...], ...]

for i in range(len(data[-1])): # Discover and store index and operation. Last operation will be \n
    if data[-1][i] != ' ':
        problems.append([i, data[-1][i]])

debug_print(data)

debug_print(problems)

for p in range(len(problems)-1):
    debug_print('-')
    for x in range(problems[p+1][0] - 2, problems[p][0] - 1, -1): # Off by 2 and 1 in the same line! Work right to left through block
        debug_print(f'col:{x}')
        num_str = ''
        for y in range(len(data) - 1): # Work top to bottom though block
            debug_print(f'\trow:{y}\t{data[y][x]}')
            num_str = num_str + data[y][x] # Assemble string of digits from spaces and numbers
        debug_print(f'num: {num_str}')
        problems[p].append(int(num_str)) # Convert number string into a number

problems.pop(-1) # Discard /n operaton at end of problems list

debug_print(problems)

total = 0

for p in range(len(problems)): # Do the math
    if problems[p][1] == '+':
        temp = 0
        for n in range(2, len(problems[p])):
            temp += problems[p][n]
    elif problems[p][1] == '*':
        temp = 1
        for n in range(2, len(problems[p])):
            temp *= problems[p][n]
    total += temp

print(total)
