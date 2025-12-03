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

debug = False

debug_print(id_list)

def is_even_digits(num):
    if len(num)%2 == 0:
        return True
    else:
        return False

def check_range(id_range): # Take in ['start', 'end'] and go through the list looking for repeat numbers
    repeats = []
    start = int(id_range[0])
    end = int(id_range[1]) + 1
    for n in range(start, end): # Search range of numbers
        debug_print(f'{n} even len: {is_even_digits(str(n))}')
        if is_even_digits(str(n)): # Only check number with an even number of digits
            if is_repeat(str(n)):
                debug_print(f'Repeat: {n}')
                repeats.append(n) # Add numbers with repeats to the list
    return repeats

def is_repeat(num):
    l = len(num)//2 # Find half the lenghth of the number
    debug_print(f'{num[0:l]} {num[l:]}')
    if num[0:l] == num[l:]: # If first half is the same as the second half, it;s a repeat
        return True
    else:
        return False

total = 0
repeat_list = []

for i in id_list:
    debug_print(f'\n{i}')
    repeat_list += check_range(i)

debug_print(repeat_list)

for i in repeat_list:
    total += i

print(total)
