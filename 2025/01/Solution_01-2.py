puzzle = open('input', 'r')
doc = puzzle.readlines()
puzzle.close

for i in range(len(doc)):
    doc[i] = doc[i].rstrip()

def debug_print(msg):
    if debug:
        print(msg)

debug = True
position = 50
last_position = 50
dir = 1
mag = 0
total = 0
inc = 0

debug_print(doc)

for i in doc:
    inc = 0
    if i[0] == 'L':
        dir = -1
        mag = int(i[1:])
    else:
        dir = 1
        mag = int(i[1:])

    position = position + (dir * mag)

    if position == 0: # exactly 0
        inc = 1
    elif position % 100 == 0: # exact hit for multiple of 100
        inc = 1 + abs(mag // 100) # Number of turns to get there plus the initial crossing
    elif position < 0: # Passed zero going left at least once
        if last_position == 0: # Started at 0
            inc = mag // 100 # Number of 0 crossings = floor of magnitude / 100
        elif last_position != 0: # Started between 0 and 99
            inc = -1 * (position // 100) # Number of 0 crossings = floor of magnitude / 100 plus the first crossing
    elif position > 100: #passed zero going right
        if last_position == 0: # Started at 0
            inc = mag // 100
        elif last_position != 0: # Started between 0 and 99
            inc = (position // 100)

    total += inc

    debug_print(f'{dir * mag}  \tlast: {last_position} \tact: {position % 100}  \traw: {position}   \t{inc}   \t{total}')
    
    position = position % 100
    last_position = position

print(total)
