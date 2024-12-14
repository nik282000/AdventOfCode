f = open('input_14-1', 'r')
puzzle = f.readlines()
f.close

width = 101
height = 103

robots = [] # Each robot has a pair of velocities and position
            #    0   1   2   3
            # [[Px, Py, Vx, Xy], ...]

lobby = [] # Grid, stores number of robots per tile

for l in puzzle:
    Px = int(l.strip().split()[0].split(',')[0][2:])
    Py = int(l.strip().split()[0].split(',')[1])
    Vx = int(l.strip().split()[1].split(',')[0][2:])
    Vy = int(l.strip().split()[1].split(',')[1])
    robots.append([Px,Py,Vx,Vy])

for y in range(height):
    row = []
    for x in range(width):
        row.append(0)
    lobby.append(row)


def show_lobby():
    for y in range(height):
        row = ''
        for x in range(width):
            row = row + str(lobby[y][x])
        print(row)

def update_lobby():
    for y in range(height): # Clear lobby
        row = []
        for x in range(width):
            row.append(0)
        lobby.append(row)
    for r in robots:
        lobby[r[1]][r[0]] += 1

def safety_factor(): # Split lobby into 4 quadrants, ignore center lines
    width_half = int(width/2)
    height_half = int(height/2)
    totals = []

    q = 0
    for y in range(0, height_half):
        for x in range(0, width_half):
            q += lobby[y][x]
    totals.append(q)

    q = 0
    for y in range(0, height_half):
        for x in range(width_half + 1, width):
            q += lobby[y][x]
    totals.append(q)

    q = 0
    for y in range(height_half + 1, height):
        for x in range(0, width_half):
            q += lobby[y][x]
    totals.append(q)

    q = 0
    for y in range(height_half + 1, height):
        for x in range(width_half + 1, width):
            q += lobby[y][x]
    totals.append(q)
    print(totals)
    print(totals[0] * totals[1] * totals[2] * totals[3])

def update_robots():
    for r in robots:
        r[0] = ((r[0] + r[2]) + width) % width
        r[1] = ((r[1] + r[3]) + height) % height

for i in range(100):
    update_robots()

update_lobby()
show_lobby()

safety_factor()
