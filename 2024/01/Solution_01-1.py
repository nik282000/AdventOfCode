f = open('input_01-1', 'r')
lines = f.readlines()
f.close

left = []
right = []

for l in lines:
    left.append(int(l.split()[0]))
    right.append(int(l.split()[1]))

left.sort()
right.sort()

total = 0

for i in (range(len(left))):
    total += abs(left[i] - right[i])

print(total)
