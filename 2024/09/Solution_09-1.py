f = open('input_09-1', 'r')
disk_map = f.read().strip()
f.close

ID_number = 0
disk = [] # 00...111...2...333.44.5555.6666.777.888899
data = True
checksum = 0

for i in disk_map: # Convert disk_map data into a list of blocks on disk
    for j in range(int(i)):
        if data:
            disk.append(ID_number) # File blocks contain the file ID
        else:
            disk.append('.') # Empty blocks contain .
    if data:
        ID_number += 1
    data = not data

i = 0
rev_i = len(disk) - 1

while i < rev_i: # Move backwards, and fowards matching blocks at the end with gaps at the beginning
    defragged = False
    if disk[i] == '.': 
        while not defragged:
            if not disk[rev_i] == '.':
                disk[i], disk[rev_i] = disk[rev_i], disk[i]
                defragged = True
            rev_i -= 1     
    i += 1

for d in range(len(disk)):
    if not disk[d] == '.':
        checksum += (int(disk[d]) * d)
    
print(checksum)
