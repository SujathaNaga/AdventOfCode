from util import *
from collections import defaultdict
import math

class GoOutException(Exception):
    pass

lines = get_file_contents("../input/day12-sample.txt", False)
lines = get_file_contents("../input/day12.txt", False)
g_dict = defaultdict(lambda: 0)

rotation_dir_list_L = ['N','W','S','E']
rotation_dir_list_R = [r for r in reversed(rotation_dir_list_L)]

# start profiling
start_profiling()

facing_dir = 'E'

wx = 0
wy = 0

def move_w(d):
    global wx, wy
    if d == 'N':
        wy += v
    elif d == 'S':
        wy -= v
    elif d == 'E':
        wx += v
    elif d == 'W':
        wx -= v

for i in range(len(lines)):
    line = lines[i]
    d = line[0]
    v = int(line[1:])
    if i == 0:
        d = 'E'
    move_w(d)
    
    if d == 'L':
        assert v % 90 == 0
        facing_dir = rotation_dir_list_L[(rotation_dir_list_L.index(facing_dir) +  v // 90) % len(rotation_dir_list_L)]
    elif d == 'R':
        assert v % 90 == 0
        facing_dir = rotation_dir_list_R[(rotation_dir_list_R.index(facing_dir) +  v // 90) % len(rotation_dir_list_R)]
    elif d == 'F':
        move_w(facing_dir)
    
print('a)',abs(wx) + abs(wy))

end_profiling()

####################################
wx = 10
wy = 1


finalx = 0
finaly = 0

start_profiling()


for i in range(len(lines)):
    line = lines[i]
    d = line[0]
    v = int(line[1:])

    if d == 'N' or  d == 'S' or  d == 'E' or d == 'W':
        if d == 'N':
            wy += v
        elif d == 'S':
            wy -= v
        elif d == 'E':
            wx += v
        elif d == 'W':
            wx -= v
    elif d == 'R' or d == 'L':
        assert v % 90 == 0
        if d  == 'R':
            while v > 0:
                v -= 90
                t = wx
                wx = wy
                wy = -t
        if d  == 'L':
            while v > 0:
                v -= 90
                t = wx
                wx = -wy
                wy = t
    elif d == 'F':
        finalx += wx * v
        finaly += wy * v
    
print('b)', abs(finalx) + abs(finaly))
end_profiling()
