puzzle = open('input', 'r')
doc = puzzle.readlines()
puzzle.close

for i in range(len(doc)):
    doc[i] = doc[i].rstrip()

position = 50
total = 0

for i in doc:
    if i[0] == 'L':
        print(f'Left {i[1:]}')
        position = position - int(i[1:])
    else:
        print(f'Right {i[1:]}')
        position = position + int(i[1:])
    position = position % 100
    print(position)
    if position == 0:
        total += 1
    
print(total)
