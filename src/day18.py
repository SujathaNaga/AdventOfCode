from util import *
from collections import defaultdict
from itertools import product


max_iterations=6
lines=get_file_contents("../input/day18-sample.txt", False)
lines=get_file_contents("../input/day18.txt", False)

def part1(math_list):
    a1=int(math_list.pop(0))
    while math_list:
        operator, a2, *math_list=math_list
        if operator=='+':
            a1+=int(a2)
        elif operator=='*':
            a1*=int(a2)
    return a1


def part2(math_list):
    # give priority to addition
    while '+' in math_list:
        i=math_list.index('+') # getfirst x+y
        ans=int(math_list[i - 1])+int(math_list[i+1])
        math_list=math_list[:i - 1]+[ans]+math_list[i+2:]
    return part1(math_list)


def process_paranthesis(math_str, function):
    # process paranthesis first
    while '(' in math_str:
        open_paranthesis_index=math_str.index('(')
        close_paranthesis_index=math_str.index(')')
        if close_paranthesis_index < open_paranthesis_index:
            close_paranthesis_index=math_str[open_paranthesis_index:].index(')')+open_paranthesis_index
        try:
            next_open_paranthesis_index=math_str[open_paranthesis_index+1:].index('(')+open_paranthesis_index+1
        except ValueError:
            next_open_paranthesis_index=close_paranthesis_index+1

        if close_paranthesis_index < next_open_paranthesis_index:
            # process the innermost paranthesis first
            math_array=math_str[open_paranthesis_index+1:close_paranthesis_index].split()
            ans=function(math_array)
            math_str=math_str[:open_paranthesis_index]+str(ans)+math_str[close_paranthesis_index+1:]
        else:
            ans=process_paranthesis(math_str[next_open_paranthesis_index:], function)
            math_str=math_str[:next_open_paranthesis_index]+str(ans)
    
    return math_str

total=0
for line in lines:
    math_expression_array=process_paranthesis(line,part1).split()
    total += part1(math_expression_array)
print('a)', total)

total=0
for line in lines:
    math_expression_array=process_paranthesis(line,part2).split()
    total += part2(math_expression_array)
print('b)', total)