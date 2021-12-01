from util import *
from collections import defaultdict


def find_nth(lines, N):
    turn=1
    g_dict=defaultdict(lambda :[])
    current_number=0
    for i in range(len(lines)):
        g_dict[lines[i]].append(turn)
        current_number=lines[i]
        turn+=1


    prev_number = current_number
    while True:
        
        if len(g_dict[prev_number]) == 2:
            current_number=g_dict[prev_number][1] - g_dict[prev_number][0]
        elif len(g_dict[prev_number]) == 1:
            current_number=0
        
        g_dict[current_number].append(turn)
        if len(g_dict[current_number]) > 2:
            del g_dict[current_number][0]

        if turn == N:
            print(str(N), "th for ", str(lines), " = ", str(current_number))
            break
        prev_number=current_number    
        turn+=1
   
find_nth([0,3,1,6,7,5], 2020)
find_nth([0,3,6], 2020)
find_nth([1,3,2], 2020)
find_nth([2,1,3], 2020)
find_nth([1,2,3], 2020)
find_nth([2,3,1], 2020)
find_nth([3,2,1], 2020)
find_nth([3,1,2], 2020)

start_profiling()
find_nth([0,3,1,6,7,5], 30000000)
end_profiling()
find_nth([0,3,6], 30000000)
find_nth([1,3,2], 30000000)
find_nth([2,1,3], 30000000)
find_nth([1,2,3], 30000000)
find_nth([2,3,1], 30000000)
find_nth([3,2,1], 30000000)
find_nth([3,1,2], 30000000)


    








