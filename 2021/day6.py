#https://adventofcode.com/2021/day/1

import copy
from bisect import bisect_left
import re 
from itertools import chain
import math
from typing import DefaultDict


input2="""3,3,5,1,1,3,4,2,3,4,3,1,1,3,3,1,5,4,4,1,4,1,1,1,3,3,2,3,3,4,2,5,1,4,1,2,2,4,2,5,1,2,2,1,1,1,1,4,5,4,3,1,4,4,4,5,1,1,4,3,4,2,1,1,1,1,5,2,1,4,2,4,2,5,5,5,3,3,5,4,5,1,1,5,5,5,2,1,3,1,1,2,2,2,2,1,1,2,1,5,1,2,1,2,5,5,2,1,1,4,2,1,4,2,1,1,1,4,2,5,1,5,1,1,3,1,4,3,1,3,2,1,3,1,4,1,2,1,5,1,2,1,4,4,1,3,1,1,1,1,1,5,2,1,5,5,5,3,3,1,2,4,3,2,2,2,2,2,4,3,4,4,4,1,2,2,3,1,1,4,1,1,1,2,1,4,2,1,2,1,1,2,1,5,1,1,3,1,4,3,2,1,1,1,5,4,1,2,5,2,2,1,1,1,1,2,3,3,2,5,1,2,1,2,3,4,3,2,1,1,2,4,3,3,1,1,2,5,1,3,3,4,2,3,1,2,1,4,3,2,2,1,1,2,1,4,2,4,1,4,1,4,4,1,4,4,5,4,1,1,1,3,1,1,1,4,3,5,1,1,1,3,4,1,1,4,3,1,4,1,1,5,1,2,2,5,5,2,1,5"""
input1="""3,4,3,1,2"""

class WinException(BaseException):
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


#####################################################################################

# lanternfish = list(map(int,input1.split(',')))
lanternfish = list(map(int,input2.split(',')))

#slow
def funca(days_max, lanternfish):
    for d in range(days_max):
        for fishindex in range(len(lanternfish)):
            if lanternfish[fishindex] == 0:
                lanternfish[fishindex]=6
                lanternfish.append(8)
            else:
                lanternfish[fishindex]-=1
    
    print('ans',len(lanternfish))

# funca(80, lanternfish)
# funca(256, lanternfish)

# optimized
def func2(days_max, lanternfish):
    # for consolidated dictionary
    fishset=DefaultDict(lambda: 0)
    for fish in lanternfish:
        fishset[fish] += 1
    
    for d in range(days_max):
        resetfish=0
        for key in sorted(list(fishset)):
            value=fishset[key]
            if key==0:
                del fishset[key]
                resetfish=value
            else:
                del fishset[key]
                fishset[key-1]+=value
        
        fishset[6]+=resetfish
        fishset[8]+=resetfish
    
    print('ans2',sum([value for value in fishset.values()]))

func2(80,lanternfish)
func2(256,lanternfish)