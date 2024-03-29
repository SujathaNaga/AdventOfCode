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

input="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

input=""".............................................................................................#..............................................
...#....................#............................#......................#........................#...........#................#.........
................#.....................................................#..............#.....................#................................
................................................................#.......................................................#...................
.......#........................#.........................#..............................#.....#............................................
............#............................#..................................................................................................
......................#........................#......................................................#.....................................
....................................#.....................................#.................#..........................................#....
................................................................................................................#..............#............
...................#.................................................#............................#.........................................
............................................#.........#...............................#.................#...................................
.....#.....................#..................................................#.............................................................
........................................................................#.................#.................................................
...............................................................#.....................................................#............#.........
..............#.......................#...........................................#.........................................................
.......................#.......................#...........................................................#................................
.........#........................................................#.........................................................................
.........................................................................#................................................................#.
............................#..........................#........................#.....#...............................#.....................
.....................................#..................................................................#....................#..............
#...........................................................................................................................................
..........#......................#...........#............#............#....................................................................
....................#.........................................................#.................................#...........................
.................................................#.............#.....................#..........#......................#..........#.........
....................................#.......................................................................................................
..........................................#..............................................................................................#..
......................#.....................................................................................#.....#.........#...............
...........#................#.............................#.............#.....................#.............................................
#.................#...............................................#...........#.............................................................
.......................................#.................................................#..................................................
.....#.......................................#.......................................................#..............................#......#
..............#.................#.................#..................#..............#..............................#........................
...........................................................................#................................................................
.........................#............................#....................................................#................#...............
.#..............................................................................#...........................................................
.......................................#................................#......................#............................................
................#...........#...................#.......................................................................................#...
..............................................................#..........................................................#..................
.......#......................................................................#.........#.............#.....................................
.......................................................#....................................................................................
......................#................................................#....................................#.............................#.
#.........................................#......................................................................#..........................
..................................#................#............................................#.......#...................................
.....#.....................#.............................#.............................#....................................................
................#...............................................#...........................................................................
...............................#................................................#....................#..........................#...........
......................................................#....................#................#................#..............................
..#..........................................#......................................................................#.......................
.............#..............................................................................................................................
.......................................................................................................................................#....
.......................#..............#...........................#............................#...............#............................
.........#..................#...............................................#...........#...................................................
......................................................................#........................................................#............
..............................................................#....................#...............#......#........#........................
..............#...................#.............#.....................................................................................#.....
............................................................................................................................................
.....................#.....#............#...........#......................................#................................................
..........#...................................................................................................................#...........#.
...#......................................................................#.....................#................#..........................
.............................................#...........................................................................#..................
......................................................#...........#................#................#.................................#.....
.................................#.....................................#..................#...............#......................#..........
............................................................................................................................................
.......#..............................................................................................................#.....................
.....................#..............#......#.................................................#..............................................
..............................#..................................#..............#............................#..............................
..........#...............................................#............................#..........................................#.........
#.................................................#...................#...........................#.........................................
.......................................#....................................................................................................
.......#...........................................................................#........................................................
................#............................................#............................................#.........#....................#..
.......................#........#.........#...............................................................................#.................
............................................................................................................................................
..#................#........................................................................................................................
..........#...........................................#......................................#..............................................
............................................................................................................................................
.....#.....................................#...................#....................................................................#.......
.........................#...........#............#.................................................................#....................#..
........................................................#...............#...................................................................
............#.................#.................................................#......#..............#.....................................
.............................................................................................#................#................#............
........................................#.......................#..........................................................................#
..#.................#..........................#......................#.............#..............#...................#.............#......
............................#............................#................................#......................#..........................
.............#.................................................................................#............................................
.................................#.........................................#................................................................
.........................#.........................#.................................................#........................#.............
.......#......................................................#.............................................................................
............................................................................................................................................
............................................................................................................................................
.......................#.........................................................................................#..........................
...#...........................#..................................................................#......#................#.................
...............................................#................#...........................................................................
....................#.................................#.................#.......#..........#........................................#.......
...........#.................................................................................................#.............................#
.#..................................................................................................#.......................................
.....................................#.................................................................................#....................
...............#.........#...........................................................#......................................................
................................#........................#........#.........................................................................
......#..........................................#.............................................................................#............
...............................................................................................#.......#....................................
...............................................................................................................#............................
..............................#...........#............................#.................................................#............#.....
...................#...........................#............................................................................................
...............................................................#.....................#.....#................................................
........#.................#.......................................................................................#...........#.............
...............#............................#.........#.......................#...........................#.................................
.#...................................#...................................#................................................................#.
.........................................................................................#...........................................#......
........................#...................................................................................................................
....................................................................................................................#.......................
........................................#.....#.........#.........#.........................................................................
.......................................................................................#............#.......................................
.#..............................#.............................................................#........................#.....#.....#........
............#...............................................................#.................................#.........................#...
..............................................................#.........................................#...................................
........................#..............................#...............#........#.........#.................................................
...................#........................#.......................................................................#.......................
.......................................#...................................................................#................................
..............#..................#..............#...................................................................................#.......
........#......................................................#..............#.................#.........................................#.
....................................................................#.......................................................#...............
.............................#..........................................................................#...................................
.................#..................................................................#.......................................................
............................................#..........................#............................................#..............#........
......#..............#..........................................#...........#..............................#................................
............#.....................#.................................................................#.......................................
...........................#.............#...............#..................................................................#...............
#....................................................................................................................................#......
.............................................................#.....................#........................................................
.......#..........................................#.................#....................................#........#.......................#.
..........................................................................................#.................................................
..........................#..............................................#......................#...........................................
...............................#.....................#..........................#.............................#.............................
....#......#................................................#..........................#.......................................#............
..................#.............................#...........................................................................................
...........................................#..................................................#.............................................
.......................#...........................................#...................................................#...................#
.......#......#.............#.........................#..................#..............................#...........................#.......
..#..............................................................................................................#.........................."""

# prep data

old_lines=[list(l) for l in input.split('\n')]

def calculate_b(start, end, expanded_rows, expanded_cols, expansion):
    minx=min(start[0],end[0])
    maxx=max(start[0],end[0])
    steps=0
    for x in range(minx, maxx):
        steps+=expansion if x in expanded_rows else 1
        
    for y in range(min(start[1],end[1]), max(start[1],end[1])):
        steps+=expansion if y in expanded_cols else 1
    
    return steps

def day11b(expansion):
    expanded_rows=[]
    lines=old_lines
    for row in range(len(lines)):
        if '#' not in old_lines[row]:
            expanded_rows.append(row)

    expanded_cols=[]
    for col in range(len(lines[0])):
        if '#' not in ''.join([lines[row][col] for row in range(len(lines))]):
            expanded_cols.append(col)

    galaxies_loc=[]
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == '#':
                galaxies_loc.append((row,col))

    total=0
    for a in range(len(galaxies_loc)):
        for b in range(a+1, len(galaxies_loc)):
            v=calculate_b(galaxies_loc[a], galaxies_loc[b], expanded_rows, expanded_cols, expansion)            
            total+=v
    print(total)                
    
day11b(2)
day11b(1000000)

