from util import *
from collections import defaultdict

class GoOutException(Exception):
    pass



lines = get_file_contents("../input/day11-sample.txt", False)
lines = get_file_contents("../input/day11.txt", False)
col_max=len(lines[0])
row_max=len(lines)

# start profiling
start_profiling()

def find_seat_placement(row, col, rows):
    occupied = 0
    empty = 0
    for p in range(row-1, row+2):
        if p >= 0 and p < len(rows):# prev row
            for m in range(col-1,col+2):
                if m >= 0 and m < len(rows[p]):
                   
                    if m == col and p == row:
                        continue # ignore
                    test_row = rows[p]
                    if test_row[m] == '#': # if any seat is occupied
                        occupied += 1
                    elif test_row[m] == 'L': # if any seat is empty
                        empty += 1
            
    return occupied, empty
                            

def figure_seats(rows):
    new_rows = []
    
    for i in range(row_max):
        row = list(rows[i])
        for k in range(col_max):
            if row[k] == 'L': # empty
                o, e = find_seat_placement(i, k, rows)
                if o == 0:
                    row[k] = '#'
            elif row[k] == '#': # occupied
                o, e = find_seat_placement(i, k, rows)
                if o >= 4:
                    row[k] = 'L'

        row = ''.join(row)
        new_rows.append(row)
    return new_rows


rows = lines
old_rows = []
index = 0
while old_rows != rows:
    old_rows = rows
    rows = figure_seats(rows)
    index += 1

occupied = sum(sum(r=='#' for r in row) for row in rows)
print("a) ",occupied)
end_profiling()





