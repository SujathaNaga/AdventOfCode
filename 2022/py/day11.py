import sys
import math
from dataclasses import dataclass
from typing import Callable
import operator
import copy

input="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

input="""Monkey 0:
  Starting items: 71, 56, 50, 73
  Operation: new = old * 11
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 7

Monkey 1:
  Starting items: 70, 89, 82
  Operation: new = old + 1
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 6

Monkey 2:
  Starting items: 52, 95
  Operation: new = old * old
  Test: divisible by 3
    If true: throw to monkey 5
    If false: throw to monkey 4

Monkey 3:
  Starting items: 94, 64, 69, 87, 70
  Operation: new = old + 2
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 6

Monkey 4:
  Starting items: 98, 72, 98, 53, 97, 51
  Operation: new = old + 6
  Test: divisible by 5
    If true: throw to monkey 0
    If false: throw to monkey 5

Monkey 5:
  Starting items: 79
  Operation: new = old + 7
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 0

Monkey 6:
  Starting items: 77, 55, 63, 93, 66, 90, 88, 71
  Operation: new = old * 7
  Test: divisible by 11
    If true: throw to monkey 2
    If false: throw to monkey 4

Monkey 7:
  Starting items: 54, 97, 87, 70, 59, 82, 59
  Operation: new = old + 8
  Test: divisible by 17
    If true: throw to monkey 1
    If false: throw to monkey 3"""

linesoriginal=input.split('\n')

@dataclass
class Monkey:
    items: list
    items_original: list
    func: Callable[[int], int]
    second_param: int
    test_val: int
    mi_true: int
    mi_false: int
    inspections: int
    part1: bool

    def __init__(self, items, func, second_param, test, mi_true, mi_false) -> None:
        self.items=items
        self.items_original=copy.deepcopy(self.items)
        self.func=func
        self.second_param=second_param
        self.test_val=test
        self.mi_true=mi_true
        self.mi_false=mi_false
        self.inspections=0
        self.part1=True
    
    def inspect(self, lcm):
        self.inspections+=1
        self.items[0]=self.func(self.items[0], self.second_param or self.items[0])
        self.items[0]=int(math.floor(self.items[0]/3)) if self.part1 else self.items[0]%lcm

    def test(self, lcm):
        self.inspect(lcm)
        return self.mi_true if self.items[0]%self.test_val==0 else self.mi_false 
    
    def reset(self):
        self.inspections=0
        self.part1=not self.part1
        self.items=copy.deepcopy(self.items_original)
        
monkeys=[]
lineindex=0
while lineindex<len(linesoriginal):
    line=linesoriginal[lineindex]
    if "Starting" in line:
        monkey_stuff=[]
        line=line.replace("Starting items: ","")
        worries=list(map(int, line.split(', ')))
        monkey_stuff.append(worries)
    elif "Operation" in line:
        line=line.replace(" Operation: new = old ","")
        line=line.lstrip()
        a,b=line.split(' ')
        if a=='*':
            if b.isdigit():
                monkey_stuff.extend([operator.mul, int(b)])
            else:
                monkey_stuff.extend([operator.mul, None])
        elif a=='+':
            if b.isdigit():
                 monkey_stuff.extend([operator.add, int(b)])
            else:
                 monkey_stuff.extend([operator.add, None])
    elif "Test" in line:
        line=line.replace("Test: divisible by ","")
        monkey_stuff.append(int(line))
    elif "If true" in line:
        line=line.replace("If true: throw to monkey ","")
        monkey_stuff.append(int(line))
    elif "If false" in line:
        line=line.replace("If false: throw to monkey ","")
        monkey_stuff.append(int(line))
        monkeys.append(Monkey(*monkey_stuff))
    lineindex+=1

lcm=math.prod([m.test_val for m in monkeys])
rounds=20
for r in range(rounds):
    for monkey in monkeys:
        for wi in range(len(monkey.items)):
            monkeyindex=monkey.test(lcm)
            monkeys[monkeyindex].items.append(monkey.items.pop(0))

monkey_inspections=[m.inspections for m in monkeys]
monkey_inspections.sort()
print('a',monkey_inspections[-1]*monkey_inspections[-2])

#b
rounds=10000
for m in monkeys:
    m.reset()

for r in range(rounds):
    for monkey in monkeys:
        for wi in range(len(monkey.items)):
            monkeyindex=monkey.test(lcm)
            monkeys[monkeyindex].items.append(monkey.items.pop(0))

monkey_inspections=[m.inspections for m in monkeys]
monkey_inspections.sort()
print('b',monkey_inspections[-1]*monkey_inspections[-2])


# a 66802
# b 21800916620