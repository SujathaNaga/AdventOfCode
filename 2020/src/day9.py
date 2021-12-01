from util import *
from collections import defaultdict

class FoundException(Exception):
    pass

rows = get_file_contents("../input/day9.txt", False)
rows =[int(r) for r in rows]

preamble = 25    
invalidnumber = 0
for i in range(len(rows)):
    if i >= preamble:
        found = False
        try:
            for k in range(i - preamble, i):
                for j in range(k + 1, i):
                    if rows[k] + rows[j] == rows[i]:
                        found = True
                        raise FoundException

        except FoundException:
            pass

        if not found:
            print("invalid number: " + str(rows[i]))
            invalidnumber = rows[i]
            break

ii = 0
k = 0
while ii < len(rows):

    total = 0
    contig_set = []
    try:
        k = ii
        while total < invalidnumber:
            total += rows[k]
            contig_set.append(rows[k])
            k += 1
            
        if total == invalidnumber:
            contig_set.sort()
            print("b) " + str(contig_set[0] + contig_set[-1]))
            break

    except FoundException:
        pass

    ii += 1


