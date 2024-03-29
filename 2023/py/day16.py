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
from copy import deepcopy
from functools import cache
from contextlib import suppress
from functools import reduce
from threading import Thread, Lock


input=""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""

input="""\\.............\\................\\....\\..../....\\/...............................\\...-..........-.\\.-....../....
|\\......../|....\\..............-\\............./...........................-..........-......\\........\\........
.......||......../....-./.../-...|.|..-......-.|....../................\\............|...................-..|..
........./......-.............-\\......................|.\\./.......|........./......-......../..-.........|....
....../....................-............................................../...../...|.........................
....................\\....|/............................./.......-....|......../..........................\\....
.|....../|.........-......|.............\\..|..................|......../.................|.|............-.|...
.....-............\\\\............\\................/......-.........\\................\\..|../....................
............|..|.......|......../................\\.......................|../....../......./.....|............
.\\...........\\..\\.............../.........-/....|......................./.....-./-.........../-........-......
|................\\.\\-.............../..-............./........./.................\\.............|...-.....-....
.........-....|..|......................................\\.||...-../..|............../...../.../.........-.....
.....-....-\\.................|...........|../.....\\...............................|...../../|.................
.\\......\\......................\\....../.../.....-.../.........................../..|...........|..\\...........
-............|.........-.-........-.........................|...\\...-...........\\.|...-....../..........|.....
.........-.......|......\\.....\\..-...../..../.....\\.../............/..........-......./....../...........\\.../
..............\\........................|.............................-../......-..-...../..................\\..
.....\\......-.......-.......-......../../../........\\.......-..........|......./........................../...
.\\...\\...................|./\\|.-..\\...............................\\..\\.....-....|......................./.....
.................-...|....|.../...../.|.||.....-.|............................-..............\\................
........................................../.......................|........\\......../.../..............|.....\\
.......\\......./............................./........../../..........................-\\..................|...
...........-...|..\\..........-.........\\.................././................|./.......|............../.......
......./..................................\\...-.........\\........\\....../............................\\......\\-
-.|..-|...............|..........................\\..........|.-.........\\............-.|.............\\.....|..
.............................../..............-.....-.......-........................|.......-................
.........\\.........-.........|...../......../......./....-...\\...................\\........\\...................
..........\\.........\\........../...|.................|./...\\.......\\..........-...............................
./...................|........../\\......../....................|..-...........\\...\\...........|..............|
.....|...........\\-.\\.......-..........................-....-...................|....|.|...............-......
.|.././......................|.......|.......|..............\\...../.................../.\\...-.................
...........-........./....|.................|..-.....-............./...................................-..../.
...................\\/..|.....-............../-......-..........|........................./...\\....-|....|-....
........................./..-..|.\\-...............-......-/...../.......\\..|................-...\\.|.....\\.....
\\...../.........................../....................-..........|........../..-..-.......\\........../.././|.
........................../...\\|..................................................../...|.-........-.....|..\\.
....\\.............................|./.....|...../....\\.............\\...../.......-...............\\..-..../....
.........-.........................|................|........\\/.\\-...................\\..-......./../..........
...-.../............/.................-..........\\....../............../...../..........|.....................
..........\\...\\..................|...-......\\\\......./...-.............-\\.................|...../......\\......
/..\\/.............\\....\\.............\\.......................................|.....\\....-............\\........
....../..\\.|................................\\.........../.......-.......-/.....|...................-.....-....
........-....|.............................|....../...............\\.......................--..................
................/......|.........-....................-..............|.......................................|
.........\\........|...........................\\.............|.............................../.................
...|..\\....-......../.\\...-............................................................/....-...../...........
.............\\\\\\.../...../.../..........\\..............\\...........\\........................|....../.........\\
......-..............|..-..|....-\\..\\..-...-............\\.................\\...-.\\/.....\\......-.\\....--.../...
........./...................../...../..|...\\.\\/.........\\.../........................................\\.../-..
........\\.......|.......|\\..|........../..../\\........../........\\..../..............././..../.............-.\\
........................|-............|............................./.-.|...|............../....-\\............
../........-.../....................|....................-/.............../.....-...........-....\\......||....
.....\\..|.....-|../....|./....-|.......-...../..-..\\..............\\...................../.................|...
...-......../.\\...........\\.........\\../.....|............\\..................../.........\\................/.\\/
...../...|............-..\\.../............/............-..............--.-..........././............-........|
.....|...........\\.....-...\\..../.....-........-.....\\.|..............\\....-............./...../..............
....\\.....-.|....\\..../..............\\|../.........../......|....\\/.......................|............|....-.
........|..--..............|..............-........|.......|.-.........\\.............-...........\\............
./.||....\\......./....\\./........../...........././....\\.................../..................\\...../.........
.......|..\\...-.\\..\\..|.........../..................................-....|........\\......|....|..............
...|..........|.........-...............|...............................-.......|...........-..\\.......\\......
.\\.........../../............................-..|...\\.....-.........../......-|.../.....|.................-...
........|....../..\\..\\|..|......|.........|...............................\\../.....\\....-/........-...........
.................................................\\.......|........|.\\.-....../.......|.......|............\\...
.......|.......\\.......|.........|......-......|...|...\\.............\\.............|/.........................
..........|....................|..........\\..........-......./................................................
...../.......|....................|......................././.................................................
........\\.............|........--..........\\.............../......|...................../............|..\\.....
....-............|.........|....|.-.\\../-...\\....-...-................\\|..\\-.......|........-............../..
................/........\\.....\\.....././....|....................-...............\\...........-......\\........
.\\.....|......|...|\\......\\.\\/....\\.............-............\\.....\\.......-...-........-....//..../.....|..-.
..................|..|.-.................../\\...........|..../..........\\|.....-..|.../.......................
-......-......./........./../.............../..................-..\\.......\\............|...../../....../......
....../............/...........\\.............\\............./.........../.......\\......|....|.........../......
...\\........|..................|............-............-.....-..\\..-................/........../........||..
......../..|..-../..../......................../.........\\./.-................../...................-.........
.../....|....\\.......-..\\..........-....\\.............|\\........../...............-........|..................
..............\\.............\\|.........-......................-........\\|......./.......-.................|...
/..../...-||\\-...|\\...............................\\.......................\\.............-................-....
.......-..-....|..................|..............................................................///...-.../.|
......|.......-/........-.-......|....\\..-...|...........\\...........\\.....................-..../.........../.
......-...........|-..\\.......|...|.\\|.................-....\\...................\\.\\........\\.\\./.........\\....
....../............../.........|...|.......|..../.............................................................
.........../...................-./...\\..........\\-............./...........\\.../.....|......................-.
/..../..../........................................|.\\......-/......./....\\.........................-......|..
.\\./.|.-..........................|...|...........|....../....-....../|...............\\..............\\...-....
....|...\\..........|......-..................|........../..|.-...\\........./........|................|........
...\\....\\........../........../.........\\..............-...........................-.|...../..........\\.......
...|...........-...........................\\........-.........................\\...-..-.....\\.......|........-.
......\\|...........................\\.....................................-............/....\\...........|......
................../............-........................\\.................................................-...
.../....|...............|....................../\\.........|....................\\....|............\\.........|-.
.......................................|....-.........../....\\-........|......./............-..|.............\\
/.........\\..\\.........|...............\\.......\\........./................\\....................|.....|........
..................................|.....|.-..|.../......................../-\\......|..........................
.................|.....................................................-............|.....|..../.\\/..........|
.......\\....\\....-........|.|..../......-......\\...../....................-...........\\............-..........
....-.................................-..........-......-................................../.........-\\...|...
.....................|......................|.........-............../.../.....-........\\.....................
.\\./..........-.\\...\\||................./../........\\.........|...\\........\\....\\.\\...............-|......|...
..\\......//.........../.\\........\\......|......|........\\......\\.....-..........|.-..|...../|.................
/.....................\\.................-........|...................\\.....-..............-/.....\\..|../../...
...|..-.../............./.|.................../............/..\\...........-....|-............\\.......--.......
..............\\..\\/.....\\.........|.\\.........................|............|........./................./-..|-.
...........................-.................../...................|\\..........\\/..|.-........................
.....-.............................../....................\\.........|......................|..................
..................\\.........../...........\\..\\/.........|...........|..-........|....\\..........-...../.|.....
..........|.......\\..\\...........\\.../......................-...........-.....-........../\\|..................
....../.......-........................\\|...//...\\..-......\\.......|..\\....................-..........\\..-....
|./....|........-./........../.\\...\\.....|../..../.......-........../.\\.....-................................."""

# /
movement_right_mirror={'east':['north'], 'west':['south'], 'north':['east'], 'south':['west']}
# \
movement_left_mirror={'east':['south'], 'west':['north'], 'north':['west'], 'south':['east']}
# |
movement_v_splitter={'east':['north','south'], 'west':['north','south'], 'north':[], 'south':[]}
# -
movement_h_splitter={'east':[], 'west':[], 'north':['east','west'], 'south':['east','west']}

movements={'\\':movement_left_mirror, '/': movement_right_mirror, '|':movement_v_splitter,'-':movement_h_splitter}

direction={'east':(0,+1),'west':(0,-1),'north':(-1,0),'south':(+1,0)}
lines = input.split('\n')
energized_dict=defaultdict(list)

def process_thread(direction_name, loc):
    x=loc[0]
    y=loc[1]
    
    while x>=0 and x<len(lines) and y>=0 and y<len(lines[0]) :
        
        if direction_name not in energized_dict[(x,y)]:
            energized_dict[(x,y)].append(direction_name)
        else:
            return         
        
        
        if '.' == lines[x][y]:            
            x=x+direction[direction_name][0]
            y=y+direction[direction_name][1]
        else:
            l=lines[x][y]
            next_dirs=movements[l][direction_name]
            
            for n in next_dirs:
                new_x=x+direction[n][0]
                new_y=y+direction[n][1]
                process_thread(n, (new_x,new_y))
                
            if len(next_dirs)==0:
                x=x+direction[direction_name][0]
                y=y+direction[direction_name][1]
    
def day16():  
    direction_name='east'
    loc=(0,0)
    process_thread(direction_name, loc)
    print(len(energized_dict))
    

def day16_b():      
    max_y=len(lines[0])
    max_x=len(lines)
    
    locations=[((0,y),'south') for y in range(0,max_y)]
    locations.extend([((max_x-1,y),'north') for y in range(0,max_y)])
    locations.extend([((x,0),'east') for x in range(0,max_x)])
    locations.extend([((x,max_y-1),'west') for x in range(0,max_x)])
    
    max=0
    for loc,direction_name in locations:
        energized_dict.clear()
        process_thread(direction_name, loc)
        max=len(energized_dict) if len(energized_dict) > max else max       
    print(max)
            

day16()
day16_b()