f = open('input_09-1', 'r')
disk_map = f.read().strip()
f.close

ID_number = 0
disk = []
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

def measure(start_addr, dir): # Returns first and last address of continuous block of identicle lable
    i = start_addr
    id = disk[start_addr]
    while disk[i] == id:
        i += dir
    size = [start_addr, i - dir]
    size.sort()
    return size

def swap(a, b): # Take in [first_addr1, last_addr1], [first_addr2, last_addr2] and swap 1 into 2
    size = a[1] - a[0] + 1 # A is the file and <= b in lenght
    for i in range(size):
        disk[a[0] + i], disk[b[0] + i] = disk[b[0] + i], disk[a[0] + i]
    

i = len(disk) - 1
while i > 0: # Work backwards to find files
    j = 0
    moved = False

    if not disk[i] == '.': # Find begining and end of file
        file_addr =  measure(i, - 1)
        i = file_addr[0] - 1 # Index is now block before start of file 
        while j < (len(disk) - 1) and (not moved) and (j < i): # Find gap to fit file_addr that is before that file
            if disk[j] == '.':
                gap_addr = measure(j, 1)
                if (gap_addr[1] - gap_addr[0]) >= (file_addr[1] - file_addr[0]): # Check file fits in gap
                    swap(file_addr, gap_addr) # Move the file
                    moved = True # Moved a file, GTFO
                j = gap_addr[1] + 1 # Didn't move the file, skip this gap
            else:
                j += 1 # Not in a gap, move forwards
    else:
        i -= 1 # Not in a file, move backwards

for d in range(len(disk)): # Finally
    if not disk[d] == '.':
        checksum += (int(disk[d]) * d)
    
print(checksum)
