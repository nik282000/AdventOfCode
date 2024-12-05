def safe(report):
    d = []
    for i in range(len(report) - 1):
        d.append(report[i] - report[i + 1])
    inc = False
    dec = False
    for i in range(len(d)):
        if d[i] == 0:
            return False
        elif abs(d[i]) > 3:
            return False
        elif d[i] > 0:
            inc = True
        elif d[i] < 0:
            dec = True
    
    if inc and dec:
        return False
    else:
        return True

f = open('input_02-1', 'r')
lines = f.readlines()
f.close

reports = []
safe_total = 0

for l in lines:
    reports.append(list(map(int,l.split())))

for r in reports:
    if safe(r):
        safe_total += 1

print(safe_total)