# Thanks to https://github.com/Hussain-70/Baby-Step-Giant/blob/main/Q3.py
import math
import copy


# https://adventofcode.com/2019/day/1
data =[1,9,10,3,2,3,11,0,99,30,40,50]
data=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,2,119,1,9,119,0,99,2,0,14,0]

# replaced data
data=[1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,2,119,1,9,119,0,99,2,0,14,0]

# puzzle B
def compute(data_input) -> int:
        index=0
        while True:
                value=data_input[index]
                if value==99:
                        return data_input[0]
                elif value==1:
                        data_input[data_input[index+3]] =  data_input[data_input[index+1]] + data_input[data_input[index+2]]
                elif value==2:
                        data_input[data_input[index+3]] =  data_input[data_input[index+1]] * data_input[data_input[index+2]]
                else:
                        raise AssertionError(f'opcode not valid {value} {index}')
                index+=4

        return data_input[0]                        
                        
        
for noun in range(100):
        for verb in range(100):
                data_tmp = copy.deepcopy(data)
                data_tmp[1]=noun
                data_tmp[2]=verb
                if compute(data_tmp) == 19690720:
                        print('ans b)', 100*noun+verb)

# puzzle A                
dindex = 0
while data:
        if data[dindex] == 1:
                data[data[dindex+3]]  = data[data[dindex+1]] + data[data[dindex+2]]
        elif data[dindex]==2:
                data[data[dindex+3]] = data[data[dindex+1]]*data[data[dindex+2]]
        elif data[dindex]==99:
                break
        dindex+=4
        

print('ans a)', data[0])

