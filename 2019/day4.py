#https://adventofcode.com/2019


input2="125730-579381"

begin,end = list(map(int,input2.split('-')))
print(begin, end)

count = 0
for i in range(begin, end+1):
    v=list(str(i))
    for j in range(len(v) - 1):
        if v[j] == v[j+1]:
            add = True
            for k in range(len(v) - 1):
                if v[k+1] < v[k]:
                    add = False
            if add:
                count+=1
                break

print('a', count)

# 1167 too low
# 1174 too high

import re
from collections import Counter

count = 0
lower=begin
upper=end

for i in range(lower, upper + 1):
    print((s := str(i)))
    print("".join(sorted(s)))
    print('----')
    if (s := str(i)) == "".join(sorted(s)):
        c = set(Counter(s).values())
        count += bool(c & {2})

print('b', count)
# b=1411
