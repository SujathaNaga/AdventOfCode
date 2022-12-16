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

input="""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

input="""Sensor at x=98246, y=1908027: closest beacon is at x=1076513, y=2000000
Sensor at x=1339369, y=2083853: closest beacon is at x=1076513, y=2000000
Sensor at x=679177, y=3007305: closest beacon is at x=1076513, y=2000000
Sensor at x=20262, y=3978297: closest beacon is at x=13166, y=4136840
Sensor at x=3260165, y=2268955: closest beacon is at x=4044141, y=2290104
Sensor at x=2577675, y=3062584: closest beacon is at x=2141091, y=2828176
Sensor at x=3683313, y=2729137: closest beacon is at x=4044141, y=2290104
Sensor at x=1056412, y=370641: closest beacon is at x=1076513, y=2000000
Sensor at x=2827280, y=1827095: closest beacon is at x=2757345, y=1800840
Sensor at x=1640458, y=3954524: closest beacon is at x=2141091, y=2828176
Sensor at x=2139884, y=1162189: closest beacon is at x=2757345, y=1800840
Sensor at x=3777450, y=3714504: closest beacon is at x=3355953, y=3271922
Sensor at x=1108884, y=2426713: closest beacon is at x=1076513, y=2000000
Sensor at x=2364307, y=20668: closest beacon is at x=2972273, y=-494417
Sensor at x=3226902, y=2838842: closest beacon is at x=3355953, y=3271922
Sensor at x=22804, y=3803886: closest beacon is at x=13166, y=4136840
Sensor at x=2216477, y=2547945: closest beacon is at x=2141091, y=2828176
Sensor at x=1690953, y=2203555: closest beacon is at x=1076513, y=2000000
Sensor at x=3055156, y=3386812: closest beacon is at x=3355953, y=3271922
Sensor at x=3538996, y=719130: closest beacon is at x=2972273, y=-494417
Sensor at x=2108918, y=2669413: closest beacon is at x=2141091, y=2828176
Sensor at x=3999776, y=2044283: closest beacon is at x=4044141, y=2290104
Sensor at x=2184714, y=2763072: closest beacon is at x=2141091, y=2828176
Sensor at x=2615462, y=2273553: closest beacon is at x=2757345, y=1800840"""

@dataclass
class vec2:
    __slots__ = 'x', 'y'
    x: int
    y: int
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

lines=input.splitlines()
scanners=[]
beacons=[]
distances=[]

for line in lines:
    x1,y1,x2,y2=map(int, re.findall(r'\d+', line))
    d=abs(x2-x1) + abs(y2-y1)
    scanners.append((x1,y1))
    beacons.append((x2,y2))
    distances.append(d)

start_time=time()

row=2000000
ranges=[]
for (x1,y1), d in zip(scanners, distances):
    projected_dist=y1-row
    if projected_dist > d:
        continue
    
    ranges.append(((x1+abs(projected_dist)-d),
                    (x1-abs(projected_dist)+d +1)))
    
beacons_count= len({x2 for (x2,y2) in beacons if y2 == row})
r1,r2=zip(*ranges)
print('a', max(r2)-min(r1)-beacons_count)

# b
for row in range(4000000):
    ranges=[]
    for (x1,y1), d in zip(scanners, distances):
        projected_dist=y1-row
        if projected_dist > d:
            continue
        
        ranges.append(((x1+abs(projected_dist)-d),
                        (x1-abs(projected_dist)+d +1)))
        
    ranges=sorted(ranges)
    max_col=0
    for (start1,stop1), (start2,stop2) in pairwise(ranges):
        if start2>max_col and start2>stop1:
            print('b',(stop1*4000000+row))
            exit()
        else:
            max_col=max(stop1, max_col)

print('elapsed',(time()-start_time))