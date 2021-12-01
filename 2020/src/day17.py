from util import *
from collections import defaultdict
from itertools import product


max_iterations = 6
lines = get_file_contents("../input/day17-sample.txt", False)
lines = get_file_contents("../input/day17.txt", False)

active_cubes=set() # set of 3d points that have active cubes.
offsets=set() # offset set for each point

#################### puzzle a #######################
def energize():
    global active_cubes
    global offsets

    # calculate the number of active cubes in the neighbours as a dictionary of 3d point and active cubes count
    neighbour_dict=defaultdict(lambda : 0)
    local_active_cubes=set()
    for avec in active_cubes:
        for ovec in offsets:
            # zip = x1,x2/y1,y2/z1,z2 from x1,y1,z1 and x2,y2,z2
            nvec = tuple(x+y for x,y in zip(avec,ovec))
            neighbour_dict[nvec]+=1

    # if 2 or 3 neighbouring cubes are active, then current cube is active
    for avec in active_cubes:
        if 2 <= neighbour_dict[avec]  <= 3:
            local_active_cubes.add(avec)

    # for the coordinates that are not active, if 3 of neighbouring cubes are active, then it is active
    for avec in set(neighbour_dict.keys()) - active_cubes:
        if neighbour_dict[avec]==3:
            local_active_cubes.add(avec)
 
    # update active cubes
    active_cubes=local_active_cubes

def run(dimension):
    global active_cubes
    global offsets
    
    start_profiling()

    # init active cubes set.
    for y,line in enumerate(lines):
        for x,c in enumerate(lines[y]):
            if c=='#':
                active_cubes.add((y,x) + (0,) * (dimension-2))

    # init offsets 
    # product() -> cross product
    offsets=set(product(*(range(-1,2) for k in range(dimension))))
    offsets.discard((0,) * dimension) # remove 0,0,0

    for i in range(max_iterations):
        energize()

    print(len(active_cubes))
    end_profiling()

# puzzle a 
run(3)

# puzzle b
active_cubes=set()
offsets=set()
run(4)
