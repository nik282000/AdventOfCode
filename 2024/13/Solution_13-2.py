f = open('input_13-1', 'r')
puzzle = f.readlines()
f.close

from decimal import Decimal

# Intercept math for two y = mx + b equasions
# Starting line intercepts at 0,0, b = 0

# A line y =  ( Ay / Ax ) * x + 0

# Ending line intercetps Tx,Ty. Maked B ugly

# B line y = (( By / Bx ) * x) + (Ty - (By / Bx) * Tx)

# Thanks Wolfram Alpha, I am to tired to remember how to manipulate this shit

# At intercept x = (Ax * ((By * Tx) - (Bx * Ty))) / ((Ax * By) - (Ay * Bx)) 

                     #    0   1   2   3   4   5
machines = []        # [[Ax, Ay, Bx, By, Tx, Ty],...]
valid_maechines = [] # [[Ax, Ay, Bx, By, Tx, Ty, x_crossing, y_crossing],...]
a_cost = 3
b_cost = 1
total = 0

total_presses_a = 0
total_presses_b = 0

for p in puzzle: # Parsing input!
    if 'Button A:' in p:
        l = []
        l.append(int(p[10:].strip().split()[0][2:-1]))
        l.append(int(p[10:].strip().split()[1][2:]))
    elif 'Button B:' in p:
        l.append(int(p[10:].strip().split()[0][2:-1]))
        l.append(int(p[10:].strip().split()[1][2:]))
    elif 'Prize' in p:
        l.append(int(p[6:].strip().split()[0][2:-1]) + 10000000000000)
        l.append(int(p[6:].strip().split()[1][2:]) + 10000000000000)
        machines.append(l)

for m in machines:
    x_crossing = Decimal(m[0] * ((m[3] * m[4]) - (m[2] * m[5]))) / Decimal((m[0] * m[3]) - (m[1] * m[2]))
    y_crossing = (x_crossing * (Decimal(m[1]) / Decimal(m[0])))
    x_crossing = float(x_crossing)
    y_crossing = float(y_crossing)
    if x_crossing.is_integer() and y_crossing.is_integer():
        valid_maechines.append(m + [int(x_crossing), int(y_crossing)])

for v in valid_maechines:
    presses_a = int(v[6] / v[0])
    presses_b = int((v[4] - v[6]) / v[2])
    cost = (presses_a * a_cost) + (presses_b * b_cost)
    total += cost
print(total)
