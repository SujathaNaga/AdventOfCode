#https://adventofcode.com/2019
import time


class WinException(BaseException):
    pass

input1="1002,4,3,4,33"
input2="3,225,1,225,6,6,1100,1,238,225,104,0,2,218,57,224,101,-3828,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,26,25,224,1001,224,-650,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1102,44,37,225,1102,51,26,225,1102,70,94,225,1002,188,7,224,1001,224,-70,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,86,70,225,1101,80,25,224,101,-105,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,101,6,91,224,1001,224,-92,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,61,60,225,1001,139,81,224,101,-142,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,102,40,65,224,1001,224,-2800,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1102,72,10,225,1101,71,21,225,1,62,192,224,1001,224,-47,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1101,76,87,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,374,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,107,677,226,224,102,2,223,223,1006,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1107,677,677,224,1002,223,2,223,1006,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,449,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1006,224,554,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,644,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226"

input = input1.split(',')
input = input2.split(',')

def get_value(programcode, prgcounter, input):
    if programcode == 0:
        # position mode
        # print('position mode', 'pos',int(input[prgcounter]), 'value', int(input[int(input[prgcounter])]))
        return int(input[int(input[prgcounter])])
    else:
        return int(input[prgcounter])
    

def funca(input, inputvalue):
    prgcounter=0
    while prgcounter < len(input):
        a=input[prgcounter]
        if a == '3':
            input[int(input[prgcounter+1])] = inputvalue
            prgcounter+=2
        elif a == '99':
            break
        else:
            if len(a)<2:
                opcode=int(a[-2:])
                programcodes=[0]*3
            elif len(a)>2:
                opcode=int(a[-2:])
                programcodes=list(map(int,a[:-2]))
                programcodes=[0]*(3 - len(programcodes)) + programcodes
            
            # print('code',a,opcode,programcodes, [input[i] for i in range(prgcounter, prgcounter+4)])
            if opcode == 1:
                v = get_value(programcodes[2], prgcounter+1, input) + get_value(programcodes[1], prgcounter+2, input)
                input[int(input[prgcounter+3])] = str(v)
                prgcounter+=4
            elif opcode == 2:
                input[int(input[prgcounter+3])] = str(get_value(programcodes[2], prgcounter+1, input) * get_value(programcodes[1], prgcounter+2, input))
                prgcounter+=4
            elif opcode == 4:
                print('value',input[int(input[prgcounter+1])])
                prgcounter+=2

start=time.time()
funca(input, 1)
print('time',time.time()-start)

# part two

def funcb(input, inputvalue):
    prgcounter=0
    while prgcounter < len(input):
        a=input[prgcounter]
        if a == '3':
            input[int(input[prgcounter+1])] = inputvalue
            prgcounter+=2
        elif a == '99':
            break
        else:
            if len(a)<2:
                opcode=int(a[-2:])
                programcodes=[0]*3
            elif len(a)>2:
                opcode=int(a[-2:])
                programcodes=list(map(int,a[:-2]))
                programcodes=[0]*(3 - len(programcodes)) + programcodes
            
            # print('code',a,opcode,programcodes, [input[i] for i in range(prgcounter, prgcounter+4)])
            if opcode == 1:
                v = get_value(programcodes[2], prgcounter+1, input) + get_value(programcodes[1], prgcounter+2, input)
                input[int(input[prgcounter+3])] = str(v)
                prgcounter+=4
            elif opcode == 2:
                input[int(input[prgcounter+3])] = str(get_value(programcodes[2], prgcounter+1, input) * get_value(programcodes[1], prgcounter+2, input))
                prgcounter+=4
            elif opcode == 4:
                print('value',input[int(input[prgcounter+1])])
                prgcounter+=2
            elif opcode == 5:
                if get_value(programcodes[2], prgcounter+1, input):
                    prgcounter=get_value(programcodes[1], prgcounter+2, input)
                else:
                    prgcounter+=2
            elif opcode == 6:
                if get_value(programcodes[2], prgcounter+1, input)==0:
                    prgcounter=get_value(programcodes[1], prgcounter+2, input)
                else:
                    prgcounter+=2
            elif opcode == 7:
                if get_value(programcodes[2], prgcounter+1, input) < get_value(programcodes[1], prgcounter+2, input):
                    input[int(input[prgcounter+3])]=1
                else:
                    input[int(input[prgcounter+3])]=0
            elif opcode == 4:
                if get_value(programcodes[2], prgcounter+1, input) == get_value(programcodes[1], prgcounter+2, input):
                    input[int(input[prgcounter+3])]=1
                else:
                    input[int(input[prgcounter+3])]=0
   

start=time.time()
print('b')
funcb(input, 1)
print('time',time.time()-start)

# 101826684558431 wrong ans
