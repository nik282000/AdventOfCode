puzzle = open('input', 'r')
raw = puzzle.readlines()
puzzle.close

ranges = []
IDs = []

for i in raw:
    if "-" in i:
        ranges.append([int(i.strip().split('-')[0]), int(i.strip().split('-')[1]), False])
    elif i.strip() != "":
        IDs.append(int(i.strip()))

def debug_print(msg):
    if debug:
        print(msg)

debug = False

ranges.sort()

# Range list [[lower bound, upper bound, has-been-completed bit], ...]
# Ranges which have not been expanded or been added to another range are has-been-completed == False
# When a range has been expanded by adding other ranges and them moved to the new list
# OR when a range has been added to another list the has-been-completed bit == True
debug_print(len(ranges))

new_ranges = []
again = True
total = 0

while again:
    again = False # Maybe we found all the overlaps?
    for r in range(len(ranges)): # Check all ranges in source list
        if not ranges[r][2]: # If r has not been included into another range already, begin looking for overlapping ranges
            debug_print(f'r: {r}\t{ranges[r]}')
            new_ranges.append(ranges[r])
            for s in range(r+1, len(ranges)): # Check all remaining ranges to for overlap with current range
                if not ranges[s][2]: # Only check ranges that haven't been merged with another range
                    debug_print(f'\t\ts: {s}\t{ranges[s]}')
                    if ranges[s][0] >= ranges[r][0] and ranges[s][0] <= ranges[r][1]: # If first element of s falls inside r there is overlap 
                        debug_print('overlap')
                        if ranges[s][1] > ranges[r][1]: # If last element of s falls outside r then update the range of r in the new_ranges list
                            new_ranges[-1][1] = ranges[s][1]
                        ranges[s][2] = True # Mark range as included/added to another list
                        again = True # Merged two ranges, go around again to see if it causes more overlaps
        ranges[r][2] = True # Mark list as having been added to already

    for t in range(len(new_ranges)): # Reset all the has-been-completed bits
        new_ranges[t][2] = False

    if again: # If merges were made then we have to prep to check if any new merges can happen. Move the new list to the old list. Clear the new list
        ranges = list(new_ranges)        
        new_ranges = []
        debug_print('Again!')

debug_print('done')
debug_print(ranges)

for r in ranges:
    total += r[1]-r[0] + 1

print(total)
