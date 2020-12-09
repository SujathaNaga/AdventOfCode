from util import *
from collections import defaultdict


def find_accumulator(rows):
    accumulator = 0

    i=0
    unique_instruction_list = []

    loop_culprit = 0
    loop_found = False
    while i < len(rows):
        row = rows[i]

        if row == '':
            break

        op, value = row.split(' ')
        if i not in unique_instruction_list:
                unique_instruction_list.append(i)
        else:
            print("bad loop index: " + str(loop_culprit) + ") " + rows[loop_culprit])
            print("accumulator before loop: " + str(accumulator))
            loop_found = True
            break
    
        loop_culprit = i
        if op == 'acc':
            accumulator += int(value)
            i += 1
        elif op == 'jmp':
            i += int(value)
        elif op == 'nop':
            i += 1


    if not loop_found:
        print("program finished without loops")
        print("final accumulator " + str(accumulator))
    
    print('\n')
    
print("sample file:")
find_accumulator(get_file_contents("../input/day8-sample.txt"))
print("with loop file:")
find_accumulator(get_file_contents("../input/day8-with-loop-a.txt"))
print("fixed loop file:")
find_accumulator(get_file_contents("../input/day8-fixed-loop-b.txt"))