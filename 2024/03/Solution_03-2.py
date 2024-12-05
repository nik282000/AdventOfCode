import re

ram = open('input_03-1', 'r')
data = ram.read().replace('\n', '')
ram.close()

number_list = []
total = 0
statements = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", data)

do = True
for s in statements:
    if re.search('do\(\)' ,s):
        do = True
    elif re.search("don't\(\)", s):
        do = False
    elif do:
        number_list.append(s[4:-1])

for i in number_list:
    nums = i.split(',')
    total += int(nums[0]) * int(nums[1])

print(total)
