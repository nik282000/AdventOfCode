import re

ram = open('input_03-1', 'r')
data = ram.read().replace('\n', '')
ram.close()

number_list = []
statements = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', data)

for s in statements:
    number_list.append(s[4:-1])

total = 0

for i in number_list:
    nums = i.split(',')
    total += int(nums[0]) * int(nums[1])

print(total)
