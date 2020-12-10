from util import *
from collections import defaultdict

rows = get_file_contents("../input/day10-sample.txt", False)
rows = get_file_contents("../input/day10-sample2.txt", False)
rows = get_file_contents("../input/day10.txt", False)

# make everything an int
rows = [int(r) for r in rows]

# sort
rows.sort()

# create a default dictionary that will hold the difference mapping
diff = defaultdict(lambda: 0)

# find the difference in voltage and add it to the puzzle output dictionary
def find_diffs(input_volt):
    
    next_volt =  None
    # if the connecting volt is in the input rows then use the first found value
    if input_volt + 1 in rows:
        next_volt =  input_volt + 1
    elif input_volt + 2 in rows:
        next_volt =  input_volt + 2
    elif input_volt + 3 in rows:
        next_volt =  input_volt + 3
    
    if next_volt:
        diff[next_volt - input_volt] += 1
        # end criteria to exit from the recursive function
        if next_volt == rows[-1]:
            return next_volt
    else: 
        return None

    return find_diffs(next_volt)


# start profiling
start_profiling()

end = find_diffs(0)

if end:
    diff[rows[-1] + 3 - end] += 1

print("a) " + str(diff.get(1) * diff.get(3)))

end_profiling()


#### puzzle b

# add the initial port
rows.insert(0, 0) 

# sort
rows.sort()

# add my adapter 
rows.append(rows[-1] + 3) 

# start profiling
start_profiling()

# create a list of possibilities for each entry
g_list = [0] * len(rows) 

# the last entry (my adapter) would have only one possibility: itself. There are no more possibility
g_list[-1] = 1

# go in reverse order
for index, value in reversed(list(enumerate(rows))):
    for k in range(index+1, index+4):
        if k < len(rows):
            if rows[k] <= value+3:
                # there is a possibility, add it to the list of possibilities
                g_list[index] += g_list[k]

print("b) " + str(g_list[0]))

end_profiling()



