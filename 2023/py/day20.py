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
from heapq import heappop, heappush


input="""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

input="""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

input="""%cf -> hl, qt
&bn -> rx
%nb -> vt
%hm -> jp
%vr -> qt, sl
%gq -> hm, nl
%sl -> jx, qt
&pl -> bn
%hf -> vt, ch
%kx -> dq
%fr -> qf
%rh -> vr
&vt -> lz, dh, kr, kq, lm, qk
&dq -> mz, ml, xd, fb, xs, rc, rt
%hn -> qk, vt
%bv -> nl
%jv -> rh, qt
%kq -> lm
%nd -> hp
%gj -> bv, nl
%lv -> xs, dq
%ch -> vt, kd
%sm -> qt, nd
%nt -> jv
%qk -> cb
%jx -> cf
%hl -> qt, ng
&qt -> sm, rh, nd, jx, nt, pl
%bh -> nl, fr
%kd -> vt, nb
%gx -> mh, dq
%hp -> nt, qt
%rc -> lv
broadcaster -> kr, zb, sm, xd
&mz -> bn
%qf -> rd, nl
%sk -> nl, bh
%rb -> nl, sk
%cb -> hf, vt
%fb -> rt
&lz -> bn
%mh -> dq, kx
%rt -> mt
%xd -> dq, fb
%lm -> hn
%hh -> vt, dh
%ml -> ts
%mt -> rc, dq
%ts -> gx, dq
%rd -> nl, gq
%zb -> nl, rb
%kr -> hh, vt
&nl -> fr, zb, hm, zm
&zm -> bn
%dh -> kq
%ng -> qt
%xs -> ml
%jp -> nl, gj"""

input_to_bn_iterations=[]

def process_iteration(main_input_output,all_flipflops,all_conjunctions,pulse_count,output_pulse_count,iteration,input_to_bn,part_name):
    queue=[('button', 'low', 'button')]
    
    while queue:
        label, pulse, parent = queue[0]
        new_output_list=main_input_output[label]
        
        if label=='button':
            new_pulse='low'
        elif label=='broadcaster':            
            new_pulse=pulse
        elif label in all_flipflops:
            if pulse=='low':
                all_flipflops[label]=not all_flipflops[label]
                new_pulse='high' if(all_flipflops[label]) else 'low'
            else:
                new_output_list=[]
        elif label in all_conjunctions:
            if part_name=='part2' and label in input_to_bn and pulse == 'low':
                input_to_bn.remove(label)
                print(label,iteration+1)
                input_to_bn_iterations.append(iteration+1)
                if not input_to_bn:
                    return None, None, None
                
            all_conjunctions[label][parent]=True if pulse=='high' else False
            new_pulse='low' if all(list(all_conjunctions[label].values())) else 'high'
        elif label=='rx':
            output_pulse_count[pulse]+=1
        
        for output in new_output_list:
            pulse_count[new_pulse]+=1
            # print((label,pulse, output))
            queue.append((output, new_pulse, label))
        queue.pop(0)
    
    return all_flipflops, all_conjunctions, pulse_count

def day20(part_name,input_to_bn):
    main_input_output=defaultdict(list)
    all_flipflops={}
    all_conjunctions=defaultdict(dict)
    main_input_output['button']=['broadcaster']
    #  process input
    for line in input.split('\n'):
        label,output=line.split(' -> ')
        if label=='broadcaster':
            main_input_output[label]=output.split(', ')
        elif label[0]=='%':
            main_input_output[label[1:]]=output.split(', ')
            all_flipflops[label[1:]]=False
        elif label[0]=='&':
            main_input_output[label[1:]]=output.split(', ')
            all_conjunctions[label[1:]]={}

    for k,v in main_input_output.items():
        for output in v:
            if output in all_conjunctions:
                all_conjunctions[output][k]=False
            
    pulse_count={'low':0,'high':0}
    output_pulse_count={'low':0,'high':0}
    
    i=0
    while True:       
        output_pulse_count={'low':0,'high':0}
        all_flipflops, all_conjunctions,pulse_count=process_iteration(main_input_output, all_flipflops, all_conjunctions,pulse_count,output_pulse_count,i,input_to_bn,part_name)
        if part_name=='part1':
            if i < 1000-1:
                i+=1
            else:
                print(pulse_count)
                print(part_name, pulse_count['low']*pulse_count['high'])    
                break
        else:
            if output_pulse_count['low']==1:
                print(part_name,i+1)
                break
            elif not all_flipflops:
                print('ans',math.lcm(*input_to_bn_iterations))
                break
            else:
                i+=1                
    
start_time=time()
day20('part1',[])
print('elapsed',time()-start_time)
start_time=time()
# know your data.
# rx receives only from &bn. Only if all sources of bn is high, it will send a low signal to rx.
# bn receives only from these 4 conjunctions. Only if all these conjunctions receive low pulse from all of its sources, can this send high pulse to bn.
# all of these four conjunctions has only one source.
# the first time, each of these inputs to bn receives low is calculated into input_to_bn_iterations.
# the first time, all of these would get low pulse at same time is the first time rx will receive low, which is the lcm of input_to_bn_iterations
input_to_bn = ['pl','mz','lz','zm']
day20('part2',input_to_bn)
print('elapsed',time()-start_time)