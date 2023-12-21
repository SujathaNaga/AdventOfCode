import sys
import math
from dataclasses import dataclass
from typing import Callable
import operator
import copy
from collections import defaultdict
from time import time
import re
from itertools import pairwise
import threading
from copy import deepcopy
from functools import cache

input="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

input="""O.OO.#...#.O#...#...O..O.#O..O.##.....###O.O##O.O....OO.....##..##.#..O#.........O#..#..O...#O.....O
.....###.O....#.#O.....##..O##O.......##......O..#..##.#.O#...O...O.O....#.###O.OO#.#O.#.#..O..OOO..
OO......#.#..##O........O.###..#.#........O#..O....O#.#.##.OO.....O#.........###O......#..#.O..#....
..#O...O....#.#.#O#....#.O#....OO.OO.O#...O##.O........O.#O.OO.O.....O.#.O.#....O.....O..OO.OO...O.#
..#O...#.....O#O...###O......O#.##O..O#.O.O.#..#O#.O....O..O#...OO...O..#.O.......O.##OO.#...#...##.
.#......O.OO#....O#O#OO.O..O......OOO..O....O....#OO....O...#.O.O.O..O...OOOO...#......O..#O..#O....
..O.#.O.#..OO...........#..#......#.#...#...O...#...#...O##..O..#..O.#...O..#.O...#....#..OO..O..#.#
.##..O..##O......#...##....#..#..O....#..##.#.O#....O#..#...O.O....O.O.........OO.#.OO......O.......
..##O.O...O.O..O##OO..#.O..O.#...O..#..#.O...O....##...#O...O......#.....O##O#..O.#..#..O...#...#.O.
O..##...##...#.#.OO#...OO#O..O...O.#O..#.O......O##......#O..O..OOOOOO..O.##.O...#O.....O##......OO.
.........O..O#.....#...#......OO###OO.O.O#...#.O....O..##..O#.....O.#.##O.#......#.O.....OO#.#..##O.
OO#O...#...OO.O####.OO.#.#.......O......O#..O#..#...#O....#.....OO#O......#O#...O#.OO......O....O#..
.O.........#.#O#....#OO..#.........OO....O...#.O.O.O.OOO.O..O.....O.#....OOOO....OO.......#.#.O.##..
....#.....#.O.#O...O#OO#...##.#.#..O.O.O....#O.#.#.O...#O#O.O#O...O..#OO..O###.OO..#.....OOO.#......
#OOO..OO.O.O..O..O....#....O..O.#...O...O...##.O##..O...OOOOO#.........OOO##..#...OO#O#O.....O...##.
.......O#..#OO.O.O..OO.O#..O.......##....OO#.O..O..O#...#..#...O.##.....#..........#.....#.O...#...O
......O.#.O...O.......O#..O..OOO#...#........###.O..#....O.O#.OO.O..#.O#O.O.O.......O.##.OO......O.#
O....O..........#....##.###..#...O#.O..O.##.O....O..O..O..##.O.O#OO...O.#.O##..#.#.......#.O..O..O.O
..O#..O.#.##..O#..O#..O..O..O....OO...O##..#...O.OO..#.#.#.###O.O...#O.##..#.....#..#O.O.O...#O.O#..
..O.##........OO.....OO.O..#.....OO.O..#...#..OOO..#....#....#.OO.#.#........OO...O.#O....##O..OOOO#
.........#.#.OO.#O...#...O#........O..#.#........O......O#.OO..#..#....O##OO.......O..O.O.O.........
#..O..#..OO.O.O....O..O.O.#.O.O#O...O.OO..#......OO.#..O....#.....#OOO#.OO#.OO........###....O.....O
..O..O.O.O.....O..#.O..##.O..##..O###........O.O..#...O....OOO#.OO.#O...O..##....#.#O...#..O...O...#
O#...O..O.#.#......O..O.#OO.....O..#.......O.##O........#O.OO..#..O.##..O.#...O...#O.....#.#..OO##..
O.OO..O....O.#..O##O.#.O.O#O..##...O..##...#.O#.....O##.#O..O.O.....O....##..O.###......#........O..
.....##.#.......O.OO....#..##............##..O..#.......O..O..#.O...O#..O.O.##..O..OO.O.....O...O...
##.O.#....O..OO..OOO.OO.##..OO.OO.#...O#.....#...##...O#....OO..O.O...O...O.#....OO...#..#O#.##..#..
........OOO....O...#.O...O..#......O....#O#.#O...O#.O........O.O...OO#....O..#.#.#O.O...OO....O.#O..
OO...O...O..#.OO..O#.OO###..O.......#..O..O.####O....O.O.O#O.#..O..##OO..O..#....#..O#O....#..O...O.
..O....#.O.O....O...#.........#..O#.#..OO....#...##.OO..OO.O...OOO..O..O#.###.......O#...#....OO...#
.O...OO.O.O...#.......#.O.O.....O...OOOO.#O.O..O..OOO.OO...............#O...##O..OOO##....#O.O#.##..
O....O...O.#...........#..#.#OO###O.O...#.O#..O.....O...O....O...#...O.OOO.OO#..OO...#..OOOO...#..#.
....O...OO.#.O...O..#....O.O.#O..O....O..O..##O.#O....O..O.....O.......OO.......#OO#.##.O.#.O..#.##O
#OO#.#....###O#..OO..#..O.......O.O...OO#.#O.....O.O##.O...#.##O#...O#......#..#..O#O.O.....OO.O#.O.
...O#....O...O......#..O#O..OO.O#.OO.#.......#...O..O.....O.#O..O..O.....#OO#.O..#....#O.#O..#......
..O.....O.......#O....O#...##.....#..O.#....#.#.#O#.#....O....#..O.O......OO....O.#OO#OO.....O......
.#..O..#..O##...#O.#.##O#.#.#O....O#..###.OO..##..#..........O#O.#..#....O...##.......O.O.O##O#..#O.
.#.....O..O.#..#..O....O...#.....#O.O.....OO.#..#......##........O.#.#......#...OO#....O#O.....#..O#
#.....O.....O...O..##O.OO#OO......O#..O......O...O...#.....OO..#...O..#.....##.#.O...#..#O......OO.O
.#..#.#.#...O#.......#.O....O..#.#.#.....O...................#.O...OOO#.....O.O.....O..O.#.....#.O.O
O....O.....O.....O#O...O.O.O#O.#O..OO#OO..#OO.OO##.....##O#.O.O..#.....O..OO.##.#.......#...O..OO.O.
.O#..O..#....##......O....#.#.#......#........##...#....#.......#.....O......##.#.....O.O....OO#.O..
....OO.OO#...O..#O#O.#.O.#..OO...OOO...#O.#..#..#.#O...#O.#.O..##..O.##..O#.#.....#..O...#.O...O#.O#
....O#....O.O#OOO...#.#.........O.O....#..O...#...#.....O.O.O.O....#.OO.##O.....#.#.#.#O..O#.O.#.OOO
O#OO..O.#.......###..OO..O........O.##O.#O##..O...O.#OO.....#...O......O.OO...O..OO....O..O..#.#...O
.#.O.O.O.#......O......##O...OO.....O....O#.....O#....#.......#O..#...##..O..#O.O.O..O....O.........
...#.........OO..O.O#..O.#....#...OO##...O..OO.......#.#OO..#...#..##.#...OO#...#O.#...O.....O...#..
#.....#O......O....O#.....#.#O.OO..........O.O...#....#.###O.O..O...#...#..#....O..O..O#.O.........#
O.O.O...O...#.....#.#....O.O.O.....OO....#..OOO......O.O.......O#O...#.#O##O.####.........O#O.......
O.O...........O#...OO..#O.O.O......O.......##.O...O..##...O.#OO...#OO...#...#O#.##O.#......O.##....O
O..#...........O..O......OOO....#....OO.O...#O..O.O#......#...........#O...#O..O....#.#.#..#...#O...
..O.....#...#...O.#.O..##.........O#..##.....#O.........................##...#.#..#.OO#O...#OOO#O.##
OO..O.O.....O#.O....O##...O.O#.OO.#..O.....O...##.O#..O......OO..#..O.....##.....OO#OO...#O......O.O
.OO...#....#O..#.....OO..O.O.......O#...O#..O#..#.O....#.O.#.O...O.#.O.#...#..OO.......O#....OO..O..
O.OO..#.OOO.#.O#...#.#..O..O#.#.#.#.....#.O#..O....O..OO...O..#..#....OO#O.#......O#..##...O...O.#O.
....#....#...OO#...O.O#OO.#.#OOO..O...OO.O..#.O#..#..O.O..#.#........OO#O.#.#.#.....OO......##.#.O..
.#.O.OOO#OOO...##O#.#...#...##O.#...O.......###O#.##..O#..#.##...O..O.O.........O..#..O##......#.##.
O...#..#....#O..##..O.O##..O.O###O.......O...#.O#.O#..O...#.#.O..#.....#.....O..O..OOO.OOO..O..OOO..
...O#.O....O.O.#.O..#.O..####...OO......#OO....O#....O..O...O...OO..OO.OOO#....#..#.O.O..#..#.....O.
O.O##O.O.O.#.O.#........#O......#O.##...##OO.......O#..#..#.O....OO........#.#O..#O.........OO.O#..O
.......#.....O...O.O.#O##.O.OO#.....O.O#O....O.#.##.#.......##.O.O.###O...O.O#O##...#...#...O..#....
.O#...#O...#....O##.O..........O.O.#..O.O..OOOOO.......OO.O#...O...O...#O###OOO.#OOO..............O#
O.#.#.......OO..OO.#.O#.....#.O#O...#......O....O...O.O.....OO.#O.......#..O...O.....##OO#.....OO#.#
...O#...#.....#..#O.#..O..O.#O#O.#...OO#O.O....O.#...#O#O....#......O..#O...#....O..O.O........#..#.
.O.......#..O#...O....................#.##O......#.#......####..OO#...OO.##..#........#.OO..#OOO.###
......O...O..O##.......O...O##O.O....#..#.##...#OO..##..........#..............##O.......O...#O###O.
.........#..OO.#.......OO...O....#O.#.......O..##...###..O...#OO.O.O...#...#OO....##O.....#O.O..#...
..#....O..O......#.#....OO#....#...O.#.OO.O#.....O#.#......O.#O.........O....O....#..O.........O....
.OO.......#.....O.O..O#....O.#.....O..O#O...O#.....OOO....##..O.O..O#.OO...#....#...O..#..##..#..#.O
O..#..OO##.#..OOO..#...#.OOO..O..##..O..##O.......O.O..O...#.O...#..###.#.#.#...#O..O......#.O#....#
...O..#O..O..OO.#....#...##...O...#.......OOOO#...O.###.O.......#O.O#.##.##O..#...O...O.O..#....OO..
OO.........OO...O.O............O....O.O...O.O.O.......O.OOO.O#....#O.O..#.....O#...#...#....#......O
#.OO#........OO..#OO.....O.#...#..#O.O...O.....#..O.......O...O..O...O.O.O....##...O....O.OO.....#.O
..O....#..O....O#.....#..#O......O......#...#O.......O.O...##O.#...O#..O#.#O###...#.OOO.#O...O#....O
.#.#..OO.#..O###....O.#......O..OO...O.O..O.#.O....O.#..O.....O#....O....#.......O.O...O......OOO.#.
...OO#.OO#O....O....O.O.#.O.#O..#.O#...###...#......#...OO##.#.#..O#...#....#.#.#.OO....O...OOOO...O
..O.#..O...O...O#O......##.....O...O..O....#....O..#OO.#.O......#O.OOO.O.O..#........##...#O.#O...O.
..O.OO.....O...#..O..#...O...O..#O..O#..##.....#....#.#O.#.......#O##....O.OOOOOOOO#.O...O.O#..#O##.
O.OO.####..OO...OO.O........OO#.O.O...#....#..OO......O.O...O..#.##....O....O......#O........#O.O#..
.#O.#...#.#...OO#.O.#O.....O##.O.OO.O..#..#O.....O...#.O.O#.....###.....#O.O.......O.#O.O#..#.O..#..
.O......O........O...#O....##.....#O..OO.O..#.....O.#..O...#O#.#..##.#O..........O.O.O..#....#..#..#
.OOO..O...#O.O#..#....O......O.O...O#O.....#..OO......OO.#O..O..O###......O.#.#.#.O....#...O........
.##.....#OO#.##.....#....O..O.....OO..OO##...O...O#.##.OO#....#.......#...O.O.#.O........OO...OO....
......OO#.....OO#OO......#.O....##..O.O#...O....#..O.O.#O.#...#.O..#.O.O#O....O.O..O.O.O.#OO.##.OO.#
.O..OO##....O###......####.OO...O#..#..##.##.O..#..##OOO...#..#O##.#..#........#...#....O.......#.OO
..O..O.O..#....#.#O.#.#OOO....O.##.....OO....#..O...#...#O.........O....O..#..........#.O..O.OO.O##O
OO.......#...O#.#.......O...O.OO#.O.O.....O.....#...##..#....#.......O#.#O..O.O.......##...OO..#O...
#O#....#.#.O..#...OO...##.#.#.O#O#...#........O..OO..#..O#..O..O.O.#O...#.....#O.#O.O#..OOO#.O.O..#.
.#O...OO.##.#.....O...O#O................O.O..O#...#..O.#OO..O....OO...O.#...O#.#.O...O#....OO#.#...
O#...###.OO.O...O.O#O#..O.O...O.#.....O......O...#...O.O....#...O...O#.#...##....O...........#O...#.
.....#OO.#.OO...##.O....#OO#.....O..##...OO#.......O...##..#....#..#..##.#O.O##..O.#.O.#.O#OO.O.#.#O
O##.#..O.OO..O.O.OOO.O...O..O.O..O.O.O..#.........#.....OO.#.......O#....#.......#O.#.O..#...O#..OOO
.#....O.O..O##...#.OO#.O#..#OO..O.#...O....##.#O.O#O#...#.........O.#..#....OO..O.#........##O.##O..
.....#....OO#...#.OO.O.O....O..#O.#.O#.O##.O..#.#O.#..O.#.O..O#.#.O.O.O#O....OO#...O......OO#..OO#O.
O..O.#O..OOO..O...O...#.......#O.OO....O..#...O.....O.#.OO....#.O.OO...O#...OOO###.O..#.....O..O#.#.
.OO......O#O.......OOO.......O..O...........O..##.....OO..##...O.O.O...O.O.O.....O..OO..O#....#.O..#
O....#....#O.####.O...#....O....#O..#O...O.O....O.O#..O.........O#.......O....O..O...#.##..O.OO.OO..
.O###O...#OO.OO........O.O#.O.O....O.O...##.O#..###..........#..O#.O..O.OO.O..#O#OO..O#.O.##.O.OOO##
#.#O#..O.#...O#..#.......O#..#...#...#O..#.O.....O...O.......#O.#...#OO.O....OO..O...#.#....#O......
..O.#O.O.O#..#.O...#.....#..O..##..O......O.OO.O.###.....#.O..O...OO#.OO.....#...OO#O..#..#O#...O..O"""

lines = input.split('\n')
circle_rock_sets=[set()]*2
cube_rock_set1=set() # #
dir={'north':(-1,0),'south':(+1,0),'east':(0,+1),'west':(0,-1)}

def find_new_row_col(row,col,circle_rock_set, cube_rock_set,direction_name):
    new_row=row
    new_col=col
    # ----
    row+=dir[direction_name][0]
    col+=dir[direction_name][1]
    
    if direction_name=='north':
        max_row=-1        
        x_inc=dir[direction_name][0]
        max_col=col+1
        y_inc=1
    elif direction_name=='south':
        max_row=len(lines)
        x_inc=dir[direction_name][0]
        max_col=col+1
        y_inc=1
    elif direction_name=='east':
        max_row=row+1
        x_inc=1   
        max_col=len(lines[0]) 
        y_inc=dir[direction_name][1]
    elif direction_name=='west':
        max_row=row+1
        x_inc=1    
        max_col=-1
        y_inc=dir[direction_name][1]

    found=False
    for row_i in range(row, max_row, x_inc):
        for col_i in range(col, max_col, y_inc):
            if (row_i,col_i) not in circle_rock_set  and (row_i,col_i) not in cube_rock_set:
                new_row=row_i
                new_col=col_i
                continue       
            else:
                found=True
                break
        if found:
            break
        
    return new_row, new_col

def process(row,col,dir_name,old_circle,new_circle):    
    if (row,col) in old_circle:
        r,c=find_new_row_col(row,col,new_circle,cube_rock_set1,dir_name)
        new_circle.add((r,c))   

@cache
def process_a(d, old_circle):
    # circle_rock_sets[second_set_index].clear()
    new_circle=set()
    if d=='north':
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                process(row,col,d,old_circle,new_circle)
    elif d=='south':
        for row in range(len(lines)-1, -1, -1):
            for col in range(len(lines[0])):
                process(row,col,d, old_circle,new_circle)
    elif d=='west':
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                process(row,col,d,old_circle,new_circle)
    elif d=='east':
        for row in range(len(lines)):
            for col in range(len(lines[0])-1,-1,-1):
                process(row,col,d,old_circle,new_circle)
    
   
    # for row in range(len(lines)):
    #     s=''
    #     for col in range(len(lines[0])):
    #         if (row,col) in circle_rock_sets[second_set_index]:
    #             s+='O'
    #         elif (row,col) in cube_rock_set1:
    #             s+='#'
    #         else:
    #             s+='-'
    #     print(s)
    # print('---------------')
    return new_circle
    

def day14(directions_list, N):
    start_time=time()
    set_index=0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == '#':
                cube_rock_set1.add((row,col))
            elif lines[row][col] == 'O':
                circle_rock_sets[set_index].add((row,col))
    
    
    second_set_index=(set_index+1)%2
    for i in range(N):
        for d in directions_list:            
            # print('---------------',d,'---------------------')
            
            circle_rock_sets[second_set_index] = process_a(d, frozenset(circle_rock_sets[set_index]))
            
            set_index=(set_index+1)%2
            second_set_index=(set_index+1)%2
    
    total = 0
    for r,c in circle_rock_sets[set_index]:
        total+=len(lines)-r
    
    print(total, 'elapsed:',time()-start_time)

# day14(['north'],1)
day14(['north','west', 'south','east'], 1000000000)

