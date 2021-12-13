#https://adventofcode.com/2021/day/1

import copy
from bisect import bisect_left
import re, os, sys
from itertools import chain
import math
from typing import DefaultDict, final
import time
from collections import Counter, defaultdict
from threading import Thread, Lock

input2="""4472562264
8631517827
7232144146
2447163824
1235272671
5133527146
6511372417
3841841614
8621368782
3246336677"""

input1="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

class my_logger:
    def __init__(self) -> None:
        self._logfile=open('./2021/'+os.path.basename(sys.argv[0])+'.log.txt','w+')
        self._logfilemutex=Lock()

    def write(self, line):
        if not self._enable:
            return 

        self._logfilemutex.acquire()
        try:
            self._logfile.write(line)
        finally:
            self._logfilemutex.release()
    
    def __del__(self) -> None:
        self._logfile.close()
    
    def enable(self, e):
        self._enable=e

global_logger=my_logger()
global_logger.enable(False)
# global_logger.write(' '.join(['\n\t', thread_name, 'branch-end-len', str(len(main_list)), str(main_list)]))

class ThreadSafeData:
    def __init__(self, data) -> None:
        self._data=data
        self._mutex=Lock()
    
    def append(self, d):
        self._mutex.acquire()
        try:
            self._data.append(d)
        finally:
            self._mutex.release()

    def get_copy(self):
        return_data=None
        self._mutex.acquire()
        try:
            return_data=copy.deepcopy(self._data)
        finally:
            self._mutex.release()
        
        return return_data
        

class WinException(BaseException):
    pass

class ErrorException(BaseException):
    pass

class point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

class line:
    def __init__(self,coordinates) -> None:
        self.point1 = point(coordinates[0], coordinates[1])
        self.point2 = point(coordinates[2], coordinates[3])

    def get_line_points_hor_vert(self):
        # Bresenham algorithm
        number_of_points=max(abs(self.point1.x - self.point2.x), abs(self.point1.y-self.point2.y))
        number_of_points-=1 # adjust for end points
        x_spacing=(self.point2.x-self.point1.x)/(number_of_points+1)
        y_spacing=(self.point2.y-self.point1.y)/(number_of_points+1)
        return [self.point1] + [point(self.point1.x + i * x_spacing, self.point1.y + i * y_spacing) for i in range(1, number_of_points+1)] + [self.point2]


class MyThread:
    def __init__(self, t, mut) -> None:
        self._thread=t
        self._mutex=mut

def get_key(dict1, value):
    for k,v in dict1.items():
        if v==value:
            return k
    return None

def get_keys_from_len_of_key(dict1, length):
    keys=[]
    for k,v in dict1.items():
        if len(k)==length:
            keys.append(k)
    return keys

def get_keys_from_len_of_value(dict1, length):
    keys=[]
    for k,v in dict1.items():
        if len(v)==length:
            keys.append(k)
    return keys

def get_keys_from_value(dict1, value):
    keys=[]
    for k,v in dict1.items():
        if v==value:
            keys.append(k)
    return keys

def has_all_chars(input_string, string2):
    for s in string2:
        if s not in input_string:
            return False
    return True

def get_all_indices_of_element(list1,element):
    final_list=[]
    for i in range(len(list1)):
        if list1[i]==element:
            final_list.append(i)
    return final_list

#####################################################################################

lines = input1.split('\n')
lines = input2.split('\n')
lines=[list(map(int, line)) for line in lines]

def funca(lines, iter_max):
    ans=0
    for i in range(iter_max):
        # increment all values by 1
        lines=[[v+1 for v in line] for line in lines]

        flash_list=[]
        for row in range(len(lines)):
            line=lines[row]
            for col in range(len(line)):
                if line[col] == 10:
                    # flash
                    flash_list.append((row,col))
        
        index=0
        while index < len(flash_list):
            x=flash_list[index][0]
            y=flash_list[index][1]
            for xindex in [x-1, x, x+1]:
                for yindex in [y-1, y, y+1]:
                    if ((xindex == x and yindex == y) 
                            or xindex<0 or xindex>=len(lines) or yindex<0 or yindex>=len(lines[0])):
                        continue
                    
                    lines[xindex][yindex]+=1
                    if lines[xindex][yindex] == 10:
                        flash_list.append((xindex,yindex))

            index+=1
        
        ans+=len(flash_list)
        # > 9 value  becomes 0
        lines=[[0 if v > 9 else v for v in line] for line in lines]
    print('a',ans)

start=time.time()
funca(lines,100)
print('time',time.time()-start)

def funcb(lines):
    continue_itr=True
    iteration_index=0
    while continue_itr:
        # increment all values by 1
        lines=[[v+1 for v in line] for line in lines]

        flash_list=[]
        for row in range(len(lines)):
            line=lines[row]
            for col in range(len(line)):
                if line[col] == 10:
                    # flash
                    flash_list.append((row,col))
        
        index=0
        while index < len(flash_list):
            x=flash_list[index][0]
            y=flash_list[index][1]
            for xindex in [x-1, x, x+1]:
                for yindex in [y-1, y, y+1]:
                    if ((xindex == x and yindex == y) 
                            or xindex<0 or xindex>=len(lines) or yindex<0 or yindex>=len(lines[0])):
                        continue
                    
                    lines[xindex][yindex]+=1
                    if lines[xindex][yindex] == 10:
                        flash_list.append((xindex,yindex))

            index+=1
        
        # > 9 value  becomes 0
        lines=[[0 if v > 9 else v for v in line] for line in lines]
        
        # add everything to check if all octopus have flashed
        total=sum(sum(line) for line in lines)
        if total==0:
            # all flash
            print('b', iteration_index+1)
            return
        iteration_index+=1

start=time.time()
funcb(lines)
print('time',time.time()-start)