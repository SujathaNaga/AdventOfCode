from util import *
from collections import defaultdict

class GoOutException(Exception):
    pass



lines = get_file_contents("../input/day11-sample.txt", False)
lines = get_file_contents("../input/day11.txt", False)
# start profiling
start_profiling()

def occupied_or_empty(row, col, rowinc, colinc):
    p = row
    m = col
    
    while p >=0 and p < len(rows) and m >=0 and m < len(rows[p]):
        # if valid entry
        test_row = list(rows[p])
        if m == col and p == row:
            p += rowinc
            m += colinc
            continue # ig nore
        elif test_row[m] == '#': # if any seat is occupied
            return 'o'
        elif test_row[m] == 'L': # if any seat is empty
            return 'e'
        p += rowinc
        m += colinc
    return ''

def find_seat_placement(row, col, rows):
    occupied = 0
    empty = 0

    pattern_list = [[-1,-1], [-1,0] , [-1,1],
                    [0,-1], [0,1],
                    [+1,-1], [+1,0], [+1,+1]]
    
    for p in pattern_list:
        oe = occupied_or_empty(row, col, p[0], p[1])
        if oe == 'o':
            occupied += 1
        elif oe == 'e':
            empty += 1

    
    return occupied, empty
                            

def figure_seats(rows):
    new_rows = []
    for i in range(len(rows)):
        row = list(rows[i])
        for k in range(len(row)):
            if row[k] == 'L': # empty
                o, e = find_seat_placement(i, k, rows)
                if o == 0:
                    row[k] = '#'
            elif row[k] == '#': # occupied
                # number of adjacent
                o, e = find_seat_placement(i, k, rows)
                if o >= 5:
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

o = 0
for row in rows:
    for k in range(len(row)):
        if row[k] == '#':
            o += 1

print("b) " + str(o))
end_profiling()





