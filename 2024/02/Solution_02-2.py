def safe(report):
    is_safe = False
    d = []
    for i in range(len(report) - 1):
        d.append(report[i] - report[i + 1])
    inc = False
    dec = False
    eq = False
    hi = False
    for i in range(len(d)):
        if d[i] == 0:
            eq = True
        elif abs(d[i]) > 3:
            hi = True
        elif d[i] > 0:
            inc = True
        elif d[i] < 0:
            dec = True   
    if inc and dec:
        is_safe = False
    elif not(eq or hi):
        is_safe = True
    return is_safe

def dampener(report):
    for e in range(len(report)):
        damp_report = [i for i in report]
        damp_report.pop(e)
        print(damp_report)
        is_safe = False
        d = []
        for i in range(len(damp_report) - 1):
            d.append(damp_report[i] - damp_report[i + 1])
        inc = False
        dec = False
        eq = False
        hi = False
        for i in range(len(d)):
            if d[i] == 0:
                eq = True
            elif abs(d[i]) > 3:
                hi = True
            elif d[i] > 0:
                inc = True
            elif d[i] < 0:
                dec = True   
        if inc and dec:
            is_safe = False
        elif not(eq or hi):
            return True
            is_safe = True
    return False

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
    elif dampener(r):
        safe_total += 1

print(safe_total)