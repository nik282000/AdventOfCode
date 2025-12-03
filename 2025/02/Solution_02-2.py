puzzle = open('input', 'r')
raw = puzzle.readline().rstrip()
puzzle.close
raw = raw.split(',')
id_list = [] # List of pairs of numbers [[start1, end1], [start2, end2], ...]
for i in raw:
    id_list.append(i.split('-'))

def debug_print(msg):
    if debug:
        print(msg)

def is_even_digits(num):
    if len(num)%2 == 0:
        return True
    else:
        return False

def check_repeats(num):
    for i in range(1, 1 + len(num)//2): # Check all patterns of length 1 to  1 + number of digits // 2
        if len(num)%i == 0: # If patter length i divides evenly then check for repeats
            repeat_count = num.count(num[:i]) # Count up repeats
            debug_print(f'i: {i} possible pattern: {num[:i]} repeats: {repeat_count} needed: {len(num)//i}')
            if repeat_count == len(num)//i: # If number of repeats == lenght of number // size of pattern
                debug_print(f'REPEATS {num}')
                return True
    return False

def check_range(id_range): # Take in ['start', 'end'] and go through the list looking for repeat numbers
    repeats = []
    start = int(id_range[0])
    end = int(id_range[1]) + 1
    for n in range(start, end):
        debug_print(f'{n}')
        if check_repeats(str(n)): # Add repeat numbers to the repeat list
            repeats.append(n)
    return repeats

debug = False
debug_print(id_list)

total = 0
repeat_list = []

for i in id_list:
    debug_print(f'\n{i}')
    repeat_list += check_range(i)

debug_print(repeat_list)

for i in repeat_list:
    total += i

print(total)
