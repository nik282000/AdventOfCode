f = open('input_07-1', 'r')
lines = f.readlines()
f.close

calibrations = [] # [restult, [i1, i2, i3, ...]]
valid_total = 0

for l in lines:
    calibrations.append(l.strip().split(':'))

for c in calibrations:
    c[0] = int(c[0])
    c[1] = c[1].split()
    c[1] = list(map(int, c[1]))


def operate(n, m, o): # 0 = +, 1 = *
    match o:
        case 0:
            return m + n
        case 1:
            return m * n

def inc(num, base): # Take in an array of digits MSB, ..., ..., LSB and inc by 1
    out = []
    val = 0
    for i in range(len(num)):
        val += num[len(num) - i - 1] * (pow(base,i))
    val += 1
    for i in range(len(num)):
        out.append(int(val / (pow(base, len(num) - i - 1)) % base))
        if int(val / (pow(base, len(num) - i - 1))) > 0:
            val = val - (pow(base, len(num) - i - 1))
    return out

def test(r, n): # Take a result and number list, run all the permutations of + and *, check if any work
    o = []
    total = 0
    for i in range(len(n) - 1): # Make empty operator list
        o.append(0)
    
    for i in range(pow(2, len(o))): # Loop through all operator permutations eg. [0,0,0] - [1,1,1]
        total = n[0]
        for d in range(1, len(n)):
            total = operate(total, n[d], o[d-1])
        if total == r: # If one of the operator permuations == the result then we're done
            print(f'\n{r} : {n} {o}')
            return True
        o = inc(o, 2)
    return False # If we make it here none of the permuations were valid


for c in calibrations:
    if test(c[0], c[1]):
        valid_total += c[0]

print(valid_total)
