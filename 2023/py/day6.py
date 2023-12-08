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

input1="""Time:        49     78     79     80
Distance:   298   1185   1066   1181"""

input="""Time: 49787980
Distance:   298118510661181"""

input=input.split('\n')

# prep the data
time_list=list(map(int, input[0].split(': ')[1].split()))
distance_list=list(map(int, input[1].split(': ')[1].split()))

def find_distance(total, t_current_i, t_list_index):
    d=(total-t_current_i)*t_current_i
    if d > distance_list[t_list_index]:
        return t_current_i
    return None    
            
def day6():
    start_time=time()
    total=1
    for t_index,t in enumerate(time_list):
        # find min
        min_t=0
        for i in range(1, t):
            m = find_distance(t, i, t_index)
            if m:
                min_t=m
                break
            
        # find max
        max_t=0
        for i in range(t-1, 1, -1):
            m = find_distance(t, i, t_index)
            if m:
                max_t=m
                break
        
        # print(t, distance_list[t_index],min_t, max_t, max_t-min_t+1)      
        total*=(max_t-min_t+1)
    
    print(total)
    print('elapsed',(time()-start_time))    

    
day6()