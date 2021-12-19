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

input_main="""A052E04CFD9DC0249694F0A11EA2044E200E9266766AB004A525F86FFCDF4B25DFC401A20043A11C61838600FC678D51B8C0198910EA1200010B3EEA40246C974EF003331006619C26844200D414859049402D9CDA64BDEF3C4E623331FBCCA3E4DFBBFC79E4004DE96FC3B1EC6DE4298D5A1C8F98E45266745B382040191D0034539682F4E5A0B527FEB018029277C88E0039937D8ACCC6256092004165D36586CC013A008625A2D7394A5B1DE16C0E3004A8035200043220C5B838200EC4B8E315A6CEE6F3C3B9FFB8100994200CC59837108401989D056280803F1EA3C41130047003530004323DC3C860200EC4182F1CA7E452C01744A0A4FF6BBAE6A533BFCD1967A26E20124BE1920A4A6A613315511007A4A32BE9AE6B5CAD19E56BA1430053803341007E24C168A6200D46384318A6AAC8401907003EF2F7D70265EFAE04CCAB3801727C9EC94802AF92F493A8012D9EABB48BA3805D1B65756559231917B93A4B4B46009C91F600481254AF67A845BA56610400414E3090055525E849BE8010397439746400BC255EE5362136F72B4A4A7B721004A510A7370CCB37C2BA0010D3038600BE802937A429BD20C90CCC564EC40144E80213E2B3E2F3D9D6DB0803F2B005A731DC6C524A16B5F1C1D98EE006339009AB401AB0803108A12C2A00043A134228AB2DBDA00801EC061B080180057A88016404DA201206A00638014E0049801EC0309800AC20025B20080C600710058A60070003080006A4F566244012C4B204A83CB234C2244120080E6562446669025CD4802DA9A45F004658527FFEC720906008C996700397319DD7710596674004BE6A161283B09C802B0D00463AC9563C2B969F0E080182972E982F9718200D2E637DB16600341292D6D8A7F496800FD490BCDC68B33976A872E008C5F9DFD566490A14"""

input1="""D2FE28
38006F45291200
EE00D40C823060
8A004A801A8002F478
620080001611562C8802118E34
C0015000016115A2E0802F182340
A0016C880162017C3686B18A3D4780
C200B40A82
04005AC33890
880086C3E88112
CE00C43D881120
D8005AC2A8F0
F600BC2D8F
9C005AC2F8F0
9C0141080250320F1802104A08"""

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
#####################################################################################


def parse_packet(bit_line, packets_to_process=1000):
    total_version=0
    bit_ptr=0
    current_packet_count=0
    values=[]
    while bit_ptr < len(bit_line) and current_packet_count < packets_to_process and any(list(map(int, bit_line[bit_ptr:]))):
        version=bit_str_to_int(bit_line[bit_ptr:bit_ptr+3])
        total_version+=version
        bit_ptr+=3

        type_id=bit_str_to_int(bit_line[bit_ptr:bit_ptr+3])
        bit_ptr+=3

        if type_id==4:
            # literal
            literal_value=[]
            cont='1'
            while cont=='1':
                cont=bit_line[bit_ptr]
                literal_value.extend(bit_line[bit_ptr+1:bit_ptr+5])
                bit_ptr+=5
            
            values.append(bit_str_to_int(str(''.join(literal_value))))
            current_packet_count+=1
        else:
            length_type_id=bit_line[bit_ptr]
            bit_ptr+=1
            if length_type_id=='0':
                # 15 bits. length of subpackets in bits
                bits_length=bit_str_to_int(bit_line[bit_ptr:bit_ptr+15])
                bit_ptr+=15
                v,fw,list1=parse_packet(bit_line[bit_ptr:bit_ptr+bits_length])
                bit_ptr+=bits_length
            else:
                # 11 bits. number of subpackets
                subpacket_len=bit_str_to_int(bit_line[bit_ptr:bit_ptr+11])
                bit_ptr+=11
                v,fw,list1=parse_packet(bit_line[bit_ptr:], subpacket_len)
                bit_ptr+=fw
            total_version+=v
            current_packet_count+=1
            if type_id==0:
                # add
                values.append(sum(list1))
            elif type_id==1:
                # mul
                p=1
                for l in list1:
                    p*=l
                values.append(p)
            elif type_id==2:
                values.append(min(list1))
            elif type_id==3:
                values.append(max(list1))
            elif type_id==5:
                values.append(int(list1[0] > list1[1]))
            elif type_id==6:
                values.append(int(list1[0] < list1[1]))
            elif type_id==7:
                values.append(int(list1[0] == list1[1]))


    return total_version, bit_ptr, values

def funca(lines):
    bit_lines=[]

    for line in lines:
        binary_string=''
        for c in line:
            hex=int(c,16)
            v=bin(hex)[2:] # remove leading'0b'
            v=v.zfill(4) # leading 0
            binary_string+=v
        bit_lines.append(binary_string)

    for line_index in range(len(bit_lines)):
        line=bit_lines[line_index]
        v,_,values=parse_packet(line)   
        print('======', lines[line_index], 'value-a', v, 'ans-b', values)

try:
    start=time.time()
    lines = input1.split('\n')
    funca(lines)
    print('time',time.time()-start)

    start=time.time()
    lines = input_main.split('\n')
    funca(lines)
    print('time',time.time()-start)

except WinException as e:
    pass

