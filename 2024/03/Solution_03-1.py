import re

ram = open('input_03-1', 'r')
data = ram.read().replace('\n', '')
ram.close()

data = data.split('mul(')
number_list = []

for i in data:
    closing_bracket = i.find(')')
    if closing_bracket > 3 and closing_bracket < 8:
        candidate = i[0:closing_bracket]
        valid = re.search('[0-9]{1,3},[0-9]{1,3}', candidate)
        if valid:
            number_list.append(candidate)

total = 0

for i in number_list:
    nums = i.split(',')
    total += int(nums[0]) * int(nums[1])

print(total)