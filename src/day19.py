
from util import *
import re

lines=get_file_contents("../input/day19-sample.txt", False)
lines=get_file_contents("../input/day19.txt", False)

dict = {}
rgx = {}

def getrules():
    global lines
    global d, rgx
    i=0
    while ':' in lines[i]:
        rule=lines[i]
        n, r = rule.split(':')
        n = int(n)
        if '"' in r:
            d[n] = eval(r)
            rgx[n] = d[n]
            i+=1
            continue
        #print(n, r)
        a = []
        for tok in r.split(' | '):
            x = tok.strip()
            a.append([int(y) for y in x.split()])
        d[n] = a
        i+=1
    print(d)
    lines=lines[i+1:]


def convert(key):
  a = []
  for pos in d[key]:
    b = []
    for x in pos:
      if x not in rgx:
        return False
      b.append('({})'.format(rgx[x]))
    a.append(''.join(b))
  rgx[key] = '|'.join(a)
  return True


## puzzle a
getrules()

flag = True
while flag:
  flag = False
  for key in d:
    if key in rgx:
      continue
    if convert(key):
      flag = True

print(len(rgx), len(d))

c = 0
for s in lines:
  if re.fullmatch(rgx[0], s):
    c += 1
print(c)