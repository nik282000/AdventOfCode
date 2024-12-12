# Same solution for both puzzles

import functools # Thanks stack exchange, I have no idea how this witchcraft works

f = open('input_11-1', 'r')
input = f.readline()
f.close

input = input.strip()
stones = input.split()
results = 0

@functools.cache
def rules(n): # Take in n, apply rules, return 1 or 2 number list
    n = int(n)
    if n == 0:
        return [1]
    elif len(str(n))%2 == 0:
        n = str(n)
        return [int(n[: len(n)//2]), int(n[-1 * len(n)//2:])]
    else:
        return [n * 2024]

@functools.cache
def blink(n, s): # Take in 1 number and a step number
                 # Apply the rules get one or two new numbers
                 # If not on the last step, pass the new number(s) to blink
                 # If on the last step return a 1
    total = 0
    new_n = rules(n)
    if s == 0:
        total = 1
    else:
        for i in new_n:
            total += blink(i, s - 1)
    return total

for s in stones: # Check each stone for 75 blinks
    results += blink(s, 75) # Add up the number of descendant stones
print(results)
