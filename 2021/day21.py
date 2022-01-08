#https://adventofcode.com/2021/day/1

import copy
from bisect import bisect_left
import enum
import re, os, sys
from itertools import chain
import itertools
import math
import threading
from typing import DefaultDict, final
import time
from collections import Counter, defaultdict
from threading import Thread, Lock
import numpy
from numpy.lib.polynomial import poly
from typing import Callable, Iterable, List, TypeVar, Union, Tuple
import functools

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

def bool_list_to_int(list1):
    # convert bool to int, then to list, then join them all as string
    # finally convert string "001010101001" to number
    return int("".join(map(str, list(map(int, list1)))), 2)

def hex_char_to_bin_str(c):
    hex=int(c,16)
    v=bin(hex)[2:] # remove leading'0b'
    v=v.zfill(4) # leading 0
    return v

def min_max_tuple_list(tuple_list):
    min_x=min_y=math.inf
    max_x=max_y=-math.inf
    for e in tuple_list:
        min_x=min(e[0], min_x)
        max_x=max(max_x, e[0])
        min_y=min(e[1], min_y)
        max_y=max(max_y, e[1])

    return min_x, max_x, min_y, max_y

def get_all_numbers_from_str(s):
    return list(map(lambda a: int(a.group()), re.finditer('-?\d+', s))) 
        

class Player:
    def __init__(self, index, position) -> None:
        self._index=index
        self._position=position
        self._score=0
        
#####################################################################################
def funca(lines):
    p=get_all_numbers_from_str(lines[0])
    p1=Player(p[0],p[1])
    p=get_all_numbers_from_str(lines[1])
    p2=Player(p[0],p[1])

    players=[p1,p2]
    current_player_index=0

    dice=1
    dice_roll_count=0
    while True:
        dice_val=(dice+0)%100 + (dice+1)%100 + (dice+2)%100
        dice=(dice+3)%100
        dice_roll_count+=3
        v=players[current_player_index]._position + dice_val - 1
        v=(v%10)+1
        players[current_player_index]._position=v
        players[current_player_index]._score+=v
        # print(dice, players[current_player_index]._position, players[current_player_index]._score)
        if players[current_player_index]._score>=1000:
            print('a',players[(current_player_index+1)%2]._score*dice_roll_count)
            break
        current_player_index=(current_player_index+1)%2


def funcb(lines):
    roll_freq = defaultdict(int)
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                roll_freq[i + j + k] += 1

    current_player_index=0

    # dictionary lookup for the function arguments
    @functools.cache
    def get_win_universes(players, current_player_index, score):
        if score[0] >= 21:
            return (1, 0)
        if score[1] >= 21:
            return (0, 1)

        wins = [0,0]
        next_player = (current_player_index+1)%2
        for dice_val, roll_frequency in roll_freq.items():
            v=(players[current_player_index] + dice_val - 1)%10+1
            new_players=[players[0],players[1]]
            new_players[current_player_index]=v
            new_players=tuple(new_players)
            new_score=[score[0],score[1]]
            new_score[current_player_index]+=v
            new_score=tuple(new_score)
            new_wins = get_win_universes(new_players, next_player, new_score)
            for i, v in enumerate(new_wins):
                wins[i] += roll_frequency * new_wins[i]

        return wins

    players=(get_all_numbers_from_str(lines[0])[1], get_all_numbers_from_str(lines[1])[1])
    print('b',max(get_win_universes(players, current_player_index, (0, 0))))


input1="""Player 1 starting position: 4
Player 2 starting position: 8"""

input_main="""Player 1 starting position: 3
Player 2 starting position: 7"""

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

    # TODO: do part 2
    start=time.time()
    print('sample data')
    lines = input1.split('\n')
    funcb(lines)
    print('time',time.time()-start)

    start=time.time()
    print('puzzle input data')
    lines = input_main.split('\n')
    funcb(lines)
    print('time',time.time()-start)
    
except WinException as e:
    pass

