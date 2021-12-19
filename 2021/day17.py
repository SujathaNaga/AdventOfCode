#https://adventofcode.com/2021/day/1

import copy
from bisect import bisect_left
import re, os, sys
from itertools import chain
import math
import threading
from typing import DefaultDict, final
import time
from collections import Counter, defaultdict
from threading import Thread, Lock
import numpy
from numpy.lib.polynomial import poly


class my_logger:
    def __init__(self) -> None:
        self._logfile=open('./2021/'+os.path.basename(sys.argv[0])+'.log.txt','w+')
        self._logfilemutex=Lock()
        self._enable=True

    def write(self, line):
        if not self._enable:
            return 

        self._logfilemutex.acquire()
        try:
            self._logfile.write(line+'\n')
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
            self._data+=d
        finally:
            self._mutex.release()

    def add(self, d):
        self._mutex.acquire()
        try:
            self._data+=d
        finally:
            self._mutex.release()

    def set_min(self, d):
        self._mutex.acquire()
        try:
            if d < self._data:
                self._data=d
        finally:
            self._mutex.release()

    def set(self, d):
        self._mutex.acquire()
        try:
            self._data=d
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


class MyThread(threading.Thread):
    def __init__(self, target, args=(), kwargs={}, name=None) -> None:
        def function():
            self._result=target(*args,**kwargs)
        super().__init__(target=function, name=name)


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

def bit_str_to_int(s:str):
    return int(s,2)

def hex_char_to_bin_str(c):
    hex=int(c,16)
    v=bin(hex)[2:] # remove leading'0b'
    v=v.zfill(4) # leading 0
    return v
            

#####################################################################################

debug_list=[]
def calculate(initial_x,initial_y,target):
    global debug_list
    dx=initial_x
    dy=initial_y

    max_y=0
    target_reached=False
    x=y=0
    while x<=target[1] and y>=target[2] and not target_reached:
        x+=dx
        y+=dy
        if dx!=0:
            dx=dx-1 if dx>0 else dx+1

        dy-=1

        max_y=max(y,max_y)

        if target[0] <= x <= target[1] and target[2] <= y <= target[3]:
            target_reached=True
            debug_list.append((initial_x, initial_y))


    return max_y if target_reached else None
    
def funca(lines):
    global debug_list
    for line in lines:
        # -? matches one or zero - symbol in front of integer
        # \d matches digit. \d+ matches one or more digits
        # finditer returns re.match hence group() is called to get the matched value
        target = list(map(lambda a: int(a.group()), re.finditer('-?\d+', line))) 
        ans=0
        for x in range(0, target[1]+1):
            for y in range(0, abs(target[2])):
                v=calculate(x,y,target)
                if v is not None:
                    ans=max(ans,v)
        print('a',ans)

        count_b_ans=0
        for x in range(0, target[1]+1):
            for y in range(target[2], abs(target[2])):
                v=calculate(x,y,target)
                if v is not None:
                    count_b_ans+=1
        print('b',count_b_ans)
    
    # print(len(debug_list), debug_list)

input_main="""target area: x=265..287, y=-103..-58"""
input1="""target area: x=20..30, y=-10..-5"""

try:
    start=time.time()
    print('sample data')
    lines = input1.split('\n')
    funca(lines)
    print('time',time.time()-start)

    start=time.time()
    print('puzzle input data')
    lines = input_main.split('\n')
    funca(lines)
    print('time',time.time()-start)

except WinException as e:
    pass

