puzzle = open('input', 'r')
batt_list = puzzle.readlines()
puzzle.close

for b in range(len(batt_list)):
    batt_list[b] = batt_list[b].strip()

def debug_print(msg):
    if debug:
        print(msg)

def max_jolts(num):
    batt_jolts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    last_picked = -1 # First search should include the 0th digit
    '''
    Search from the location of the last picked digit up to 12 - i digits from the end of the number
    This makes sure there are enough digits left to choose from to make a 12 digit number
    '''

    for i in range(0, 12): # Looking for a 12 digit number
        last_candidate = len(num) - (12 - i) # Don't seatch all the way to the end, leave some digits for the next guy
        debug_print(f'start: {last_picked + 1}  {num[last_picked]}\t end: {last_candidate}   {num[last_candidate]}')

        for j in range(last_picked + 1, last_candidate + 1): # Search ater the n-1th picked digit leaving room for the n+1th digit
            debug_print(j)
            if int(num[j]) > int(batt_jolts[i]): # Pick the largest digit availabe
                batt_jolts[i] = num[j] # Put it in the list
                last_picked = j # Make note of it's location, the next search will start after this digit
        debug_print(batt_jolts[i])
    
    debug_print(batt_jolts)
    return ''.join(batt_jolts)

debug = False
total = 0

debug_print(batt_list)


for b in batt_list:
    debug_print(b)
    total += int(max_jolts(b))

print(total)

#    ||||||||||||
# ||||||||||||
# 987654321111111
# 000000000011111
# 012345678901234
