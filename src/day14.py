from util import *
from collections import defaultdict

lines = get_file_contents("../input/day14-sample.txt", False)
lines = get_file_contents("../input/day14.txt", False)

memory_dict=defaultdict(lambda:0)
for i in range(len(lines)):
    f,s = lines[i].split(' = ')
    if lines[i].find("mask") != -1:
        mask = s
        i+=1
        while i < len(lines) and lines[i].find("mask") == -1:
            f,v = lines[i].split(' = ')
            memory=f[4:-1]

            # create a list of single characters denoting 0 or 1 of the binary value of the value with leading zeros
            v= list(str(bin(int(v)).replace('0b','')))
            v = ['0'] * (len(mask)-len(v)) + v

            binindex = len(v)-1
            for maskindex in range(len(mask)-1, -1,-1):
                if mask[maskindex] != 'X':
                    v[binindex]= mask[maskindex]
                binindex-=1
            
            # convert from string list to binary string to integer before saving
            memory_dict[memory]=int('0b'+str(''.join(v)),base=2)
            i+=1


sum=0
for v in memory_dict.values():
    sum += v

print("a) " +str(sum))

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

sum=0
for v in memory_dict.values():
    sum += v

print("b) " +str(sum))









