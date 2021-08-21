
from util import *
import re

lines=get_file_contents("../input/day19-sample.txt", False)
lines=get_file_contents("../input/day19.txt", False)


d = {}
rgx = {}

def getrules():
    global lines
    global d, rgx
    
    for i in range(len(lines)):
        if lines[i] == '8: 42':
            lines[i] = '8: 42 | 42 8'
        elif lines[i] == '11: 42 31':
            lines[i] = '11: 42 31 | 42 11 31'

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

for key in d:
  if key not in rgx:
    print(key, d[key])


rgx[8] = '({})+'.format(rgx[42])
a = []
for i in range(1, 20):
  a.append('(' + '({})'.format(rgx[42]) * i + '({})'.format(rgx[31]) * i + ')')
rgx[11] = '|'.join(a)
rgx[0] = '({})({})'.format(rgx[8], rgx[11])

c = 0
for s in lines:
  if re.fullmatch(rgx[0], s):
   c += 1
print(c)