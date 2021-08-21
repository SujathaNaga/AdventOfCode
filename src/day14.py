from util import *
from collections import defaultdict
from parse import *

lines = get_file_contents("../input/day14-sample.txt", False)
#lines = get_file_contents("../input/day14.txt", False)

#print(lines)
mem={}
mask_int_0 = 0
mask_int_1 = 0
for row in lines:
    p = parse('mask = {}', row)
    if p:
        # care only about 0 in the mask. flip the zeros to ones. flip everything else to 0
        mask_int_0 = int(p[0].replace('1', 'X').replace('0','1').replace('X','0'), 2)

        # care only about the 1 in the mask. flip everything else to 0
        mask_int_1 = int(p[0].replace('0', 'X').replace('X','0'), 2)
    else:
        a,b = parse('mem[{:d}] = {:d}', row)

        #  a 0 or 1 overwrites the corresponding bit in the value

        # invert the ones to zeros and zeros to ones, and & with value so that the 0 is set at the bit position
        b &= ~mask_int_0


        # set 1 at the bit position
        b |= mask_int_1
        
        mem[a] = b

print('a)',sum(mem.values()))

memory_dict=defaultdict(lambda:0)
for i in range(len(lines)):
    f,s = lines[i].split(' = ')
    if lines[i].find("mask") != -1:
        mask = s
        i+=1
        while i < len(lines) and lines[i].find("mask") == -1:
            f,v = lines[i].split(' = ')
            # create a list of single characters denoting 0 or 1 of the binary value of the memory with leading zeros
            memory = list(str(bin(int(f[4:-1])).replace('0b','')))
            memory = ['0'] * (len(mask)-len(memory)) + memory

            xcount=0
            for maskindex in range(len(mask)-1, -1,-1):
                if mask[maskindex] == '1':
                    memory[maskindex]='1'
                if mask[maskindex] == 'X':
                    memory[maskindex] = 'X'
                    xcount+=1
            
            # need all permutations of the memory for the floatin X characters
            maxx=pow(2,xcount)

            # create a list of list of binary strings
            xbinlist=[]
            for xindex in range(maxx):
                xbin = list(str(bin(xindex).replace('0b','')))
                xbinlist.append(['0'] * (len(mask)-len(xbin)) + xbin)

            # for each of the permutation, calculate memory and store value
            for xbin in xbinlist:
                m = memory.copy()
                xbinindex = len(xbin) - 1
                for mindex in range(len(m)-1,-1,-1):
                    if m[mindex] == 'X':
                        m[mindex] = xbin[xbinindex]
                        xbinindex-=1
                
                # convert from string list to binary string to integer before saving
                memory_dict[int('0b'+str(''.join(m)), base=2)] = int(v)
            i+=1

print("a) ", sum(v for v in memory_dict.values()))









