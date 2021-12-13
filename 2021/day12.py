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

input_main="""start-YA
ps-yq
zt-mu
JS-yi
yq-VJ
QT-ps
start-yq
YA-yi
start-nf
nf-YA
nf-JS
JS-ez
yq-JS
ps-JS
ps-yi
yq-nf
QT-yi
end-QT
nf-yi
zt-QT
end-ez
yq-YA
end-JS"""

input1="""start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

input2="""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

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
lines = input_main.split('\n')

data_map=defaultdict(lambda:[])
total_path_count=ThreadSafeData(0)

def process_key(key, path_list):
    global data_map
    global total_path_count
    threads=[]

    for e in data_map[key]:
        if e.islower() and e != 'end':
            if e not in path_list:
                new_path=path_list+[e]
                threads.append(Thread(target=process_key, args=(e, new_path)))
                # global_logger.write(' '.join([key, e, str(new_path)]))
            else:
                # small cave cannot be crossed more than once
                continue
        elif e=='end':
            total_path_count.add(1)
            global_logger.write(' '.join(['end==',key, e, str(path_list+['end'])]))
        else:
            new_path=path_list+[e]
            # global_logger.write(' '.join([key, e, str(new_path)]))
            threads.append(Thread(target=process_key, args=(e, new_path)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

def funca(lines):
    global total_path_count
    for line in lines:
        a,b=line.split('-')
        if a.lower()=='start':
            data_map['start'].append(b)
        elif b.lower()=='start':
            data_map['start'].append(a)
        elif a.lower()=='end':
            data_map[b].append('end')
        elif b.lower()=='end':
            data_map[a].append('end')
        else:
            data_map[a].append(b)
            data_map[b].append(a)
    global_logger.write(str(data_map))
    path_list=['start']
    process_key('start', path_list)
    print('a',total_path_count._data)

start=time.time()
funca(lines)
print('time',time.time()-start)

def process_key_b(key, path_list):
    global data_map
    global total_path_count
    threads=[]

    for e in data_map[key]:
        if e.islower() and e != 'end':
            if e not in path_list:
                new_path=path_list+[e]
                threads.append(Thread(target=process_key_b, args=(e, new_path)))
                # global_logger.write(' '.join([key, e, str(new_path)]))
            else:
                if path_list.count(e)<2:
                    # is there already another small cave visited twice?
                    if path_list[0]!='22':
                        new_path=['22']+path_list+[e]
                        threads.append(Thread(target=process_key_b, args=(e, new_path)))
                continue
        elif e=='end':
            total_path_count.add(1)
            global_logger.write(' '.join(['end==',key, e, str(path_list+['end'])]))
        else:
            new_path=path_list+[e]
            # global_logger.write(' '.join([key, e, str(new_path)]))
            threads.append(Thread(target=process_key_b, args=(e, new_path)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

def funcb(lines):
    global total_path_count
    for line in lines:
        a,b=line.split('-')
        if a.lower()=='start':
            data_map['start'].append(b)
        elif b.lower()=='start':
            data_map['start'].append(a)
        elif a.lower()=='end':
            data_map[b].append('end')
        elif b.lower()=='end':
            data_map[a].append('end')
        else:
            data_map[a].append(b)
            data_map[b].append(a)
    global_logger.write(str(data_map))
    path_list=['start']
    process_key_b('start', path_list)
    print('b',total_path_count._data)

start=time.time()
funcb(lines)
print('time',time.time()-start)
