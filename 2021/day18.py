#https://adventofcode.com/2021/day/1

import copy
from bisect import bisect_left
import enum
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
from typing import Callable, Iterable, List, TypeVar, Union

input_main="""[[2,[[1,1],9]],[[0,[3,0]],[[1,6],[4,2]]]]
[[8,[0,5]],[[[9,9],0],[[2,9],2]]]
[[[[6,4],[5,8]],[[0,9],[6,5]]],[[5,1],4]]
[[[9,[2,8]],[[0,2],[8,3]]],[[[5,6],[5,8]],[[4,8],2]]]
[[0,[[0,1],[6,0]]],[[[6,4],1],[8,6]]]
[[[[8,5],6],8],[[[9,1],[0,6]],[4,[2,4]]]]
[7,[[4,3],[8,5]]]
[[8,[1,[3,4]]],[[3,8],[0,1]]]
[[[1,1],[[2,1],[0,3]]],[[7,[1,8]],[[3,8],[5,2]]]]
[[2,[[4,6],[6,2]]],[[0,5],[3,7]]]
[[[[9,8],[4,6]],[7,[9,1]]],[[[8,7],[4,7]],[[6,6],[8,1]]]]
[[[2,[5,1]],[[0,4],3]],[[9,7],[[0,2],0]]]
[[[[5,0],2],5],[[3,[5,8]],[5,[8,9]]]]
[[6,[3,6]],[[[2,7],6],[[6,0],4]]]
[[8,8],7]
[[[[7,9],3],8],[[0,[1,7]],[[3,2],[4,5]]]]
[[[1,1],[7,2]],[3,[4,[6,4]]]]
[[[9,[6,6]],[[4,8],[1,3]]],[[[4,7],8],[[5,2],[3,8]]]]
[[[6,[6,7]],[3,4]],5]
[[[[0,0],2],9],[[[2,1],1],[5,[4,7]]]]
[[[2,[9,8]],[5,8]],[[[3,4],6],[5,0]]]
[[[7,[9,4]],[7,[7,2]]],[[1,[9,6]],1]]
[[[[9,1],1],[4,[2,6]]],3]
[[0,[8,[3,4]]],[8,[9,8]]]
[[[1,6],[6,7]],[[[0,4],1],7]]
[[6,[5,[0,0]]],[7,[[5,4],1]]]
[[2,[[9,5],[9,1]]],[[3,0],4]]
[[[5,7],[[1,0],[3,5]]],[4,[5,[4,0]]]]
[[3,3],[2,2]]
[[[[6,2],[1,7]],[1,7]],[[[6,7],6],9]]
[[[[9,8],[8,8]],[2,1]],[[8,4],8]]
[[[[1,4],1],[2,0]],[4,[[0,5],5]]]
[[[7,[6,0]],[[7,3],1]],9]
[[[[2,4],0],[[6,9],8]],[[3,[0,9]],[[4,4],[5,4]]]]
[[7,3],[0,[2,[7,2]]]]
[[[[8,8],5],9],[[8,6],6]]
[[[[9,5],7],9],0]
[[[1,4],8],[[7,[5,3]],[[6,4],6]]]
[[9,[[9,3],[3,7]]],[[[6,9],1],[[2,3],[4,4]]]]
[[4,[9,2]],[3,4]]
[[1,[[0,9],2]],[1,[1,[8,7]]]]
[[[4,1],8],[9,[9,[2,9]]]]
[[[[7,9],[9,7]],8],[[[3,0],5],[[7,8],[3,1]]]]
[[[[9,4],[9,9]],[[9,5],[8,9]]],[[2,[7,4]],[[4,6],6]]]
[[[[8,7],1],[6,8]],[[4,2],5]]
[7,[3,[3,3]]]
[[[4,9],[0,2]],[[[4,2],9],[[5,8],6]]]
[[[[1,3],1],[[7,5],[4,0]]],[[[6,3],4],[[1,2],8]]]
[[[[3,2],2],[4,7]],[[[5,6],[6,3]],3]]
[[[[4,0],6],[4,2]],[7,5]]
[[[[9,5],[2,0]],[[6,8],[0,9]]],[[[7,4],[3,6]],1]]
[[[4,[9,3]],[[9,4],8]],[[6,[1,2]],2]]
[[[[4,1],[1,1]],[[4,8],9]],[[[1,0],[0,3]],2]]
[[[3,[3,8]],[[0,6],7]],[[2,5],9]]
[[[0,[6,8]],[[2,7],[4,1]]],6]
[[6,3],0]
[[[3,[7,1]],[3,[2,0]]],[[[3,5],9],[[5,2],[7,8]]]]
[[7,8],[1,[[7,1],5]]]
[[[9,[8,9]],2],[9,[[8,8],4]]]
[[[8,[5,8]],[[9,1],[6,0]]],[[[9,1],[4,7]],8]]
[5,[[[4,9],7],[[6,0],[9,0]]]]
[[[[8,8],[6,7]],[[1,0],6]],[[5,[2,8]],[[8,0],[3,7]]]]
[[0,[6,6]],[[0,1],[3,[9,2]]]]
[[1,[0,[8,1]]],[[0,[0,0]],[8,[0,0]]]]
[[[4,[1,4]],[8,[9,5]]],7]
[7,[[[0,0],[4,3]],8]]
[[[9,1],[[7,5],[9,2]]],[5,[9,0]]]
[[[[2,0],9],[8,[3,0]]],[[9,8],[4,[0,7]]]]
[4,[5,[5,[0,3]]]]
[[6,[[6,9],8]],[1,[0,[6,0]]]]
[[7,[4,3]],[[0,6],[[5,2],[6,9]]]]
[[[[7,2],[4,6]],[[5,0],9]],6]
[[[0,1],[0,2]],[0,[5,2]]]
[[[[5,0],[5,4]],[[5,9],[9,9]]],[2,[[3,0],[8,1]]]]
[[[[9,2],[2,9]],[[5,5],2]],[[1,3],[[3,6],[1,8]]]]
[[0,[2,4]],[[[6,9],1],[[7,9],[9,8]]]]
[[[[2,1],1],[7,3]],[4,[[1,2],[2,6]]]]
[[[6,[0,1]],[[6,4],[4,2]]],[1,[[0,0],[9,7]]]]
[[[[9,2],3],[9,8]],[[6,5],[7,[1,7]]]]
[[3,9],7]
[[[6,9],[[0,2],0]],[[[8,6],2],9]]
[[[[2,2],2],[[6,7],7]],[[0,3],9]]
[[[7,[2,7]],3],4]
[[[[1,9],6],[0,7]],[[[2,2],1],2]]
[9,9]
[0,[9,[[4,1],1]]]
[[[[7,6],1],2],[[[6,9],[9,1]],0]]
[[[[4,3],[4,2]],3],[[5,[6,5]],[[2,6],0]]]
[[[0,[5,1]],[6,[1,4]]],[5,[[8,1],3]]]
[6,[9,6]]
[[8,[9,[6,8]]],[[4,9],[[2,4],[7,1]]]]
[[5,[[9,9],[3,3]]],[[[9,8],[5,0]],6]]
[[6,7],1]
[1,[4,[[9,6],0]]]
[[[[9,8],[7,8]],[5,[4,6]]],[[[5,9],6],[[4,6],4]]]
[[[2,7],4],[[[0,3],0],[[7,4],[7,4]]]]
[7,[0,4]]
[1,[3,2]]
[[3,0],8]
[[[3,2],5],8]"""

input1="""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

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
    
    def append(self, depth):
        self._mutex.acquire()
        try:
            self._data+=depth
        finally:
            self._mutex.release()

    def add(self, depth):
        self._mutex.acquire()
        try:
            self._data+=depth
        finally:
            self._mutex.release()

    def set_min(self, depth):
        self._mutex.acquire()
        try:
            if depth < self._data:
                self._data=depth
        finally:
            self._mutex.release()

    def set(self, depth):
        self._mutex.acquire()
        try:
            self._data=depth
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
def snailfish_magnitude(p):
    if isinstance(p, int):
        return p
    return 3*snailfish_magnitude(p[0]) + 2*snailfish_magnitude(p[1])

def snailfish_explode_left(pair, v):
    if isinstance(pair, int):
        return pair+v
    else:
        return [snailfish_explode_left(pair[0], v), pair[1]]


def snailfish_explode_right(pair, v):
    if isinstance(pair, int):
        return pair+v
    else:
        return [pair[0], snailfish_explode_right(pair[1], v)]

def snailfish_reduce(pair, depth=0):
    if depth == 4:
        if isinstance(pair, int):
            return ("none", ()), pair
        return ("explodeBoth", tuple(pair)), 0
    if isinstance(pair, int):
        return ("none", ()), pair

    (operator, param), left_value = snailfish_reduce(pair[0], depth + 1)
    if operator == "completed":
        return ("completed", param), [left_value, pair[1]]
    elif operator == "explodeBoth":
        return ("explode_left", param), [left_value, snailfish_explode_left(pair[1], param[1]),]
    elif operator == "explode_left":
        return ("explode_left", param), [left_value, pair[1]]
    elif operator == "explode_right":
        return ("completed", ()), [left_value, snailfish_explode_left(pair[1], param[1])]
    else:
        (op_r, params_r), right_value = snailfish_reduce(pair[1], depth + 1)
        if op_r == "completed":
            return ("completed", params_r), [pair[0], right_value]
        elif op_r == "explodeBoth":
            return ("explode_right", params_r), [snailfish_explode_right(pair[0], params_r[0]), right_value,]
        elif op_r == "explode_left":
            return ("completed", ()), [snailfish_explode_right(pair[0], params_r[0]), right_value]
        elif op_r == "explode_right":
            return ("explode_right", params_r), [pair[0], right_value]
    return ("none", ()), pair

def snailfish_split(p):
    if isinstance(p, int):
        if p>=10:
            return [math.floor(p/2), math.ceil(p/2)]
        return p
    v=snailfish_split(p[0])
    if v!=p[0]:
        return[v, p[1]]
    else:
        return[v, snailfish_split(p[1])]

def snailfish_add(a,b):
    pair=[a,b]
    prev_pair=copy.deepcopy(pair)
    while True:
        new_pair=snailfish_reduce(prev_pair)[1]
        if prev_pair != new_pair:
            prev_pair = new_pair
            continue
        x=snailfish_split(new_pair)
        if x==prev_pair:
            break
        
        prev_pair=copy.deepcopy(x)
    
    return prev_pair

def funca(lines):
    l1=eval(lines[0]) # eval=parse string and evaluate as python expression
    for line in lines[1:]:
        l1=snailfish_add(l1, eval(line))
    
    print('a', snailfish_magnitude(l1))

def funcb(lines):
    max_value=0
    lines=list(map(eval,lines))
    for i, a in enumerate(lines):
        for k, b in enumerate(lines):
            if i==k:
                continue
            max_value=max(max_value, snailfish_magnitude(snailfish_add(a,b)))
    
    print('b', max_value)

try:
    start=time.time()
    print('sample data')
    lines = input1.split('\n')
    funca(lines)
    print('time',time.time()-start)

    start=time.time()
    print('puzzle input data')
    lines = input_main.split('\n')
    funca(lines) #2501
    print('time',time.time()-start)
    
    start=time.time()
    print('sample data')
    lines = input1.split('\n')
    funcb(lines)
    print('time',time.time()-start)

    start=time.time()
    print('puzzle input data')
    lines = input_main.split('\n')
    funcb(lines) # 4935
    print('time',time.time()-start)

except WinException as e:
    pass
