puzzle = open('input', 'r')
batt_list = puzzle.readlines()
puzzle.close

for b in range(len(batt_list)):
    batt_list[b] = batt_list[b].strip()

def debug_print(msg):
    if debug:
        print(msg)

debug = True
total = 0

def max_pair(num):
    max_0 = 0
    max_0_index = 0
    max_1 = 0
    max_1_index = 0
    jolts = 0

    for j in range(len(num) - 1): # Find higest value digit that is NOT the last digit
        if int(num[j]) > int(max_0):
            max_0 = num[j]
            max_0_index = j

    for j in range(max_0_index + 1, len(num)): # Find the highest value digit AFTER max_0 digit
        if int(num[j]) > int(max_1):
            max_1 = num[j]
            max_1_index = j

    jolts = int(f'{max_0}{max_1}') # Concatenate those digits into the joltage
    return jolts

debug_print(batt_list)

for i in batt_list:
    debug_print(i)
    debug_print(max_pair(i))
    total += max_pair(i)

print(total)
