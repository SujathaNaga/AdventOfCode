from util import *

trees_b = 0

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

def find_trees_count(slope):
    trees = 0

    # get sanitized file contents as a list
    entries = get_file_contents("../input/day3.txt")
    entries = [e for e in entries if e != '']
    
    # set first row along the slope
    row = slope[1] # y direction

    # get width of the input line which would repeat itself according to the puzzle
    width = len(entries[0])

    # set the column value
    col = slope[0] % width # x direction

    while row < len(entries):
        
        # if '#' is present then it is a tree
        if entries[row][col] == '#':
            trees += 1
        
        #update row and col
        col = (col + slope[0]) % width
        row += slope[1]
    return trees


final_value = 1
for slope in slopes:
    value = find_trees_count(slope)
    print("for slope: " + str(slope) + " = " + str(value))
    final_value *= value

print("b) " + str(final_value))
