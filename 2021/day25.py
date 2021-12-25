#https://adventofcode.com/2021/day/1

import copy
from bisect import bisect_left
import enum
import re, os, sys
from itertools import chain
import itertools
import math
import threading
from typing import DefaultDict, final
import time
from collections import Counter, defaultdict
from threading import Thread, Lock
import numpy
from numpy.lib.polynomial import poly
from typing import Callable, Iterable, List, TypeVar, Union




input1="""...>...
.......
......>
v.....>
......>
.......
..vvv.."""

input1="""v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

input_main=""".v.v.v>...>vv>v>>>.v>..v>.v.>.>v>.v.v.>>v...>.>....>.>vv>>>.....>>...v.>>v..>..vvv.>v...vv...>..>....>.>.>.>vvv....>..vv>v....>v...>>....v.
>.v>..v.>>vv.>>v...v.>.>..v.>.>.>vvv..>>>.>...>v>.>>v....>>>>...>v.v>.v>....>>>v.>>>....vv.....vvv.v.v..>.>..v>>.>.v>.>v>.vvvv.v..v>>..>>vv
.vv>>...v>..v..v>v.>vvv.v.v>>.....v>>.......>...v>.v>.v.vv.v.>v>v.v......>>......>.v...v........v.v........>.v.vv.>>.v.>>.>.>...v....v>>>..
.>.>v.>vv.v...v.>>v>.>v..vv>..v.v.>...v....>vvvvvv>>>v..vv.v.v>>.>>.>>v>v>>..>.v...v.v.>v..>...v.>.>>.v...v>..v...vv.>v.....vvv.v>.v>..>>v.
..>.....v.>>..>>.v>v.>.>>.>..vv.v>>.>..>.>..v>>...>.>>.vv>>>..>>>>.v.>....>>.>..v>>vv>.>>v>vvvv>vv..v.v.>.v>..v>.vvv>>.v.......>>.>...>>.>.
v...>..>..v>.vv.>>.>...>>....v.......v>...v.vvvvv>..v...>.v.>.>>v>v.>....v>...>...v.>.vv>......vv>.v>vv>>....v>.v>.>..>v.v..>>>.>>>..v..>vv
v>v>.v>..v..v.>..>...>v.>..>.>vvvv...v.v>v....>.>v.vvvv....>...v.v..vvvvvv..v.v..v>v....>v....>v.>>.v>.>v..>...v.vv...>v>>..>.>.....v.v..v.
.......v.....v>v.vv.>.v>.>>.>v.....>>..v.v.v>v>.....v...>v.vv>>.vv>>>>.>>.v.>v>..v.v..>v.vv....>>.vv.>v...>>v....v.v.>.vvvv.v....>v>>>>v.>.
v>.v>..v...vv.>vv.v...v.v>.>........>.vv>>..........v...>vv....>.>v>v..>..>>>v.>>..v.>.>...v.v.>..v>>>..>v.....v.>>>>...v>>v...vv>..>>.v.>>
.v>>>>>>v.>.>...>.>>.>.>>v>.........v..>.v>>>v>.....>...>>.>.v..>.vvv.>..v.v..>.>..>v>v.>v......>>...>>v.vv.....>.>...>.....>v.v..>>v.vvvv.
v......>.......>>..>.v.>..v..>>v..>>......v>v.vvv.>...>>>...v..v>vv.....v.v>v>>v..v.v..v.......v.>v>.v.v..>.>..>v.v>>>v..v.>.>.>>v.>..v.v>.
>.v..>>....>.v.>...>>>..>.v..v>v..>>>.v..v....vv>vv.v.v..v...>>..>......>>..v.....v.v>>.v....v>>....>..>v.vv.>.>..v...v>>.>.>v.v.vv>.v..v.>
..v...>...v..v.v...>...>.v..>...v...vv>..v....v>>>v.v..v.v>v..>v..v..v>>vv.v>..v..v...>.......>..>.>v>v..>...>v.....v..>v>v...v>..>.>...vvv
.vv>.>.v...>>...v.>.>v.v.>>v..v.>v.>>vv.v>.>..>....v.>v>vv>..v>v>v.>>v>v.>...v>vvv..>>.v.>v.>vv.>..v>...>.v..>.>>>v>>...v>.>>v..v....v>v..v
..>.>>>...>........>.vvv>>.>v..v.>v..v..>v.>>.>.v..>.v...v>>.>v..vv...v.v>.vvv...vv>vv>v>.>vv>.>v.vv..v.v...v.>>..v...v>...v..vv..v..>.>>>>
..>.>.>v.v.>.....>vv.vvv>.>..v>>>v.>vv.>.v.>.....v>>.....>v..vvv....v.>.v>.v.vv>v.>vv.v..>v>>...v>v....v>>v>....v..>vvvv>..>v>.v..v.....>..
.vv>.....v>.>>>.>>v>>>v>>>v>.v>>.>v..>>v.vvv...>vv.v.v.v.....>>vv..v.>>>>v.>....v>v.>..>..vv>>>....vv.vvvvv>v....v...>.>.vv...v...>vv...>..
>...v.vv.vv.vvv..>v.>.......v...v.>v.>..>.v>..v...>v..>..>v.v..>.v>.>>.v>.>v...v>>.>v.v.v.v>.>..v.>vv.v>>>.>vv.vvv.>vv>>v>..v>>.vvv>v..v.v>
>v.>...>v.vv..vv>..v.v..>..v.>v>>>..vv...>.>.v.v...>>.>v.vv..>.v.>>.>.>.v>..>.>..v>..v>>.v.v.v>.>...v.v.vv.>>>.v>...v.v>..>>..v.v>vv>vv>>vv
vv.vv>....>..>...>>..v.v..v..v....v.>.vvv>>.v.v>.>.vv.>v......>vv>>.>>.....>>....>..v.v..v.v...>>v.>>>v.....v.>......v>v>v>>.v.vv...>.v....
.>v>....vv.v>>...>>....>>>.>.v>...vv.v.>vv>.....v>v.v....v..v.>v>.....>...>v>>....v.vv.v>>.>..v>.v.v...v..>..>>v.v>....v.>....v>......>v...
..vvvv>.>.>.v.>.vv....>>>v..>..v..v>vvv.>v.>>.>v.>.vv>vv.>......v...vv>v..v.v.vv>v.v..vvv>v..>>...>..>.>....>>v>....v.>vvv>>..>>>..v..v.>..
>.....>>..v>.vv.v>..>..v.>vv>>vv>.v>v..vv......>....>.....>.>v.vv.vvv.v..>.vv..>>...>vvvv>..>..>.>>.>v.vv>...>>vvvv.>.v.v...>...>v>..>v....
.v.>v..>vv.>v...>vv.v..vv>.>>.......>v>.vv..v.vv>v..>.>vv.v>>>.>>v>.>...v...vv.>>>v...>>..v>v>v.v.v>..>.v....>.v.v.>vvv.v.vv.>.v..vv.>>v>>.
....v...vvv>>>.>>.>v>...>.>v.v.>.vv>...v...>>v.v.>.v>..>...vvv....v..vv>vv>>>..>.>.>v....>..v.vv.v..v...>>>v..v.>.....v>>v>vvvv.>.>.v.>vv..
.>.>v..v>.v.v.v>v.>.vv...vv.>.>v>....v>>v..>....>>>.v>v.v>>..>.>vv..>.>..>.>>.........>>>>..>...vvv>.>.v.>v.v>...v.>vv..>.>v.>>vv.>>>v>.vvv
>..>>..>.>>>vvv.>....>>v.>..v>v>v....vv.>.>>>v..v..v>.v....v>>...>>v...vvvv>>>>.>.....v>v.v.v..>v.v..>.v.>v>>....>>>v>.v>v.>.v...>>>.>vv.>>
...>>..>..>.>v.v..vv>.>.>vv.v>>.>....>.v>..>.v>>.....v.v.v.v..>...>>v.>.v.v.>>.>v....>..v..v>>..>>.>.v..>>..>vv..vv>v.v.v..v.vv.vv>....vv..
.v.v>..>.>.v..v>>....v>....>v>>>....>......v..v.......>vvvv.vvv.v..>.>..>.>>v.v..>...>>vv>.v..v.v..>vv>..>>.>v.>.v...vvv>>..>.vv..v.>v.v>v>
v>.>.>.v>>v.>>v>.>.vv>.>>...>..>>>.v....>>>v>.v>v.>.v.>..>vvv>.v.>>....>v....v.vvv>..>.>.vv>>..>>v...vv.>.>>.v..v>.v.>.v..>.v>.v....v...>.>
>vvv>.v>..>>..>.vv>>>...>>v.>v..>v....v>vv.>..>.v.>....vv....v....>....vv.v...vv>>>.>..>>>.v....>>vv.vv>vv>>.v...>>>v.v...v.vv..v>.vv..>v>.
v.>...>>..>>v>..v.vvvv..>>.v>.v.>.vvvvv>v..v.v>....v..>>.>>..v.>.v>..v.>.v.vv>.>.>v.v....>v.vvv>>>.v>>.vvv..v..>.>...>.>..>.>...v..>>v.....
.>v.>>v>..vv.>.vv.>>...v.v....>>>v....vvv>.v.>v.>v.vv.>.....>..>>.vv.v.v.>..v.>...>>.>.....>>.>........v>...>.>>>.>v.>.v.>>.....vvvv.v.>v>.
>..v..>.>>>..>vv..v..>.v.v....v>...v>....>>...>v.>v...v..v...>.v>.>.>.vv...v....>>....vv.v>>....v.v.v....>v.....>.v.v...v>..>>..>..>>..>>v>
.>vvv.v>.>vvv>>vv>v>v..>...>vv.>..v>.....>.vv....>>...>>.>>>v..vv.>>.....>>.v..v.v>>.vv>..v.vvv...>>.>..v.v>.v......v...>.>..>..>v....vv>.v
.>v>...>...v..v>.v..v>v.v.>>.>vvv...v.>..............vv..vvvv>.>....>.>>..v.vv.>>.>.vv>...>>v.>.>.v..v>..v..>v...>.>..v.......>.>v.....>...
..v.>v>vv....v>>.v>vv....>.v>.>v.vvv>vv>>vv>..v>.vvv>.v.>v.>....v.>..v>v........v.>>>v..>>.>v>v...>>vv.>.v.>>.>..>..>vvv>.v.>vvvv.v>v.>v..>
.vv>>v......>...v>.vv>..v>>.v>v>>v>...>.>>.>.>...v...>>>>>vv>.>v....>v..v>>.>.vv>..v>>v>.v..v.v..v>......>.vv>....>v>..v>>.>.>>.v>v>v>>>v..
>v.v>.>...vv.>..>.v.>>.vv....>.....>v.v..v.>..>...>.v>v.......vv.v>.>vvv...>..>.>....>v...>..v...>v.......vv..>....v...>v.....>>v.>vv>.v.v>
v>..vv>.vv.v...vv...>......>v..>>.v>vv.v>>v..>v>..vvvv..>.>>.v..vv>.v>.>......>......>vv.v..vv>>..>..v..>v..>..>...>...>.>.........v.vv>v.v
.v>.>.......>.v.>.v..>>.>.v>...>..vv......v.v...>..v>>v..v..v...>>vv..v.v...v.v...v>vv>..v.>>>v.v.v>v..>vv>..v..>>>>...>.>..>.>>>.>>vv>>..v
.>..vvv.v>.v..>..v>>..v>v>>.>.>..v.>vv>.v.>>v>v.vv.....v.>v.>>>>vv>>>..>>...vv>v..vvvv>>>..v.v.>...v.....>>...>>..>.>.>v..>..>...>..v.v>..>
vv..v>.v....v..v>.......>vv..>vv>...vv...v>>vvv>v...v.>v.v>v.>.v.v.>.>.>....v.>>>..>.v.......vv..v.vv>.v...v...>....vvvv>....>.v..v.>v..v..
>.vvv.>v....vv>>v.>..>.vv.>v>.v.>..>>v......vv>>>vv.v..vv.v.vvvvv>>.>>.>>v...v..v.>..>...>v>.v.v>vv>>.v.vv>>..v.>>>...>>.>v.v.>>..vv>..>.v.
..v.v>..>v>..>.......>>.>>>v..v.>....>.v..v>...>v>v.>.v.>.v...>....vv..>..v.>......v...>vvv>..v..v....v>...v.>.v......v>vv..>.vv...vvv.>vv.
vv......vvvv.>>.>v>.>.v>.vv>v>.vv>....v....v.v.>vv>vv.>>.>.v>v...v.....v.>..>....v.>..>..v.....v.v>>v>.v.>..v>..vv.v.>>...>.vv>....>v.v>>..
v>.>>.>.....vv.>v>>.v>..>v.>..>>.v..v.>.>.>>.vv>..v..vv.>>v..>.>........v....v>>v.v.>v..>.>v......>..>.>.v.>...v>..>v>..v.>v>v..>vv>..v.>>>
v..v..>...>.v..>>...>.>v..>v.v.vv.v..>..v..>.v.>>v.>..v.>..v>..>.>vvv..v.>.>>.v.v..v>.>v.>..>v..v>>v>>......vv.>.>.v.>>v......>v...>v...>>.
.>..>...>...v.....>.....vv.v.>v.>.>..v....v>>...>.>.v..>>>...>v.v..>...>vv>..>v>.v.>>.vvv>>v>v.......v.vv...>>>..v...v.>v..v.>..>vv>..>.v>.
....>vv.>..>.>>.v..>.v.>..v..>..v.>>.>v..vv.v>>>v.....>>...>v>......>.>v>.v.>.vv>.vv>.v.>>..v>..>vv.v..v...>vvvv>>..>..v......v>..v.v.v>.>.
....vv>....v....>...v>..v>.>.>.>v..>.v>.......v>..v.vvv.v.>..v.>v>.>vv.v.>vv>.>>v.v..v.v...>vvv.......>v>v.v..>.v>.v>vvvv.>.>>>.>..vv.>v..>
..>.vvv>.>vvv>>>vv.>..>v.v.vvv>..vv.....>v>>..vv>.....>...>.v>.v>>.>.>vv..v...v..>.>>..>>.>.vv>v>>>vv....v>.>>..>..vv>.>>..>v>.v.v.v..>...v
.>.v>............v>v.v......vvv>.vvv>v.v.>vv..>>....v.>.vv.vv..>..>>>>v.....>.>.>..v.>.>..>.vv.v.v......>>.>>>.>>.v..>v>v...v...v>...vv>.>.
>>.v....v..>..v>>v....>...v.v....v.>..>.v>v.>v>.>>v.....>.v.>>.>>>..>.v.v.>>vv>>.>..>>v...>.>.v.vvv>>vv.vv>.v.>.>.>vv.v..>v>.>.vv>>>v..v>.v
>v..v.v.>..>>>>..>>v.v>.v>..>>....v.....>..>.>v>...>>.v>....vvv>....>v.>.v.>.>v>.>v>>.>v>v..>.....v>.vv..v>>...>>v....>v..v>....>...vvv.v>.
.>.v.....>..>.>vvv.>v.>vv.>..v..v.v.>vv>.>..>.>>>.....>v......>v.>....v..>.>..v>v.>..>.>v..>.v.>v>v>...v.v.>.v.>vvv>vv..>.v..v>..vv..>..v>.
.v>.v>v>.v..v>.v..v.>............>v.>..>..>>.v..v>v>vv>>.>v.>>.v..v...v....>.v..>vv.>.....>.>>.vvv..>>..vv>>v>.....>>.v>...v.vvv>>..>..v.v>
v...>..>...v.>>.v...>..v>v...>vv.v..>vv>..vv>>.v..vv.v>v.>>..v>v.v..>.......v...v.v>...>v.v......v.vv>...v.>..>vv>v.v....v.v.vv.vv.vvvv.>v.
.>.v>>....>....vv..>vv>.>..vv.>>...>....>vv.vv...>.vv>v...>>..v...>..v....>v.vvv...v>>.>>>>>v>..v>>vv>vv.>vv..v...v.vv..v>v.>.v.v>..v..v.>v
.>.v.v...v.....>..v>..v>.vv.v>...vv.....>v..>..>..>v.>.v...>.vv.....>.>.v.v>v....>..>>.vv.>vvvv..>>>.v...v...>v.vv>>.v..>v..>..>>.>..v>v..>
>..vv>>v..>.v>>>v>>.v..vv>....v.>vvvv.>...vv...>.v..>v.>v>.>v>v>>v.>.>...>>>.....v.v....v>...>..>.>v.>.vv.....>.>>vv.....>......>.v..>v>.>.
v.......>>.>..v>.v.>.>v..>>.>.>vv..>v.v...>.v>..v....v..v..>.>>...v..v>.vv.>v>>.>....>vv>.v.v.>..vvv.v.>.v>.v>v..>.>>.>.>..>.>...vvvvv.v>..
>..v.v>.>>v.>>...v.>v.....>.v.>.v>v.>v>.vvv>.>>..>v..v.v.>...>v....>v.v.v>>...>.vv>.>v.vv....v>..v>>v.>.>..v>v..>v>..>.>>.v>.>..>..>..v....
.>vv.>.v>>>.>.>.v>v.>..vv>..>>>.>>...v.....>v.v..>.>.>>.v.>.>v>.>v.v..vvvv>.....v.v..vv....v.>...>.vv.>>v.....>.>vv>...v....>v..>v..vv.>>>v
v..>>>v.>..v>.v.v.>.>..>..>>..vv.vv.>.v.v..>v>v.>>>.>.>>.>>.vvv..>...>>..>.>..vvv>.>..v.>.>.v>v>.>v..>.>.v>....v..>..v.>v.>>.v.v..v>v..>v..
....>v...>....>.v>>vv.....vv>..vv.v....vvv>>...vv.v.v.>......v.v>>v..>.v>..v>v.v..>....>....v.vvvv>v..v>v>v>v.>>v....v.>vv>>v>vv>>>.>..>.v>
...>>>.v.v.....v>vv>>v>.>..v.v>v>....v>>vv..vv>v>..vv...>.>v>.>v..v...>.>vv..v.>.v..v...>...v>...v.vv>vv>..v....>.v....v.v>..>.....v..v..v.
.>vv.v..v>..vv....>.>>>>..>>>>..v....>.>v.vv.v.>>.>vvv..vv..>vv.>>v>>v.v..>.....>>v>..v..>>v>vvvv...>.>v>..v..>v>...>>.>vvv.v.>vv.>..v>>...
>>.>...>v.>vv>v>.>.....>.vv.>.vv>.>>.>.>...........v>.>..>>.>.>>..v.v>>v.vv>v>.>v.>..v>vv>.>>.v>>.>.v>v.v..>v.v>.v>v>>.v.>v.>>vv...vv.vv...
>vv>>.>...>v.>v>...>v>.v.>...vv....vv>v>.>..>.v.v.vv.v.>v......>..>.vv..v>.>>.>v>...v.vv..v...>vv.v.v...>>.>.>.v..v..>.vvvvv>>>>v>vv.v.v...
>v>>>.v>..vvvv..vv>...>.>.v>>>..v.v>>.v..v>.v.....>v>>.v..>..>.....>v....>.>..>......>v>.>.v.>..v..vvv>>v.v..v>..v.v.>>>>>>>vvvv.vv.>vv..v>
..v..vv>v>v...v...>.vvvv.v.....v..>.>..>....v.....v>.>>..v.v.vv..>....vv>vv>v>>.>>v>>.>.vv.>..>>v.v>...v>.v...vv.>v....v.>>...>v.>.vv.>.vv.
.v>v..>vvv.vv>v>>>..v..>v>.vvvv.>.>.vvv>.>..vv.>v...>...>v..>..>......v...>.v..v>>.>v...>>>>.....>>>..>vv.>>>v.>v..v>>vv.>....>..>>vv.>.>..
v.>...>vvv>...>.>.v>.v..v..v>.v.>.v>.v...vvv..>.>>v>...>.>>v>>.v.>v...>>.v.v..vv..vv.>.>v.>.v.>>>.>.vv...v.v>.v.>>>>>>..vvvv..>....>..>.v..
>v..>v....v.v....>vv.>.>.>v>.>v>v.v>>>.>v...>>>.v..v.v.v>v......>vv.v..>......>v>.v>>.vv>>>...vvv.v..>.>.........v.vv>.>vv.vv>v.v.>.>vv..v.
>.v>.v.v>v..vv.v>v>.>>....vv..>.vvv>v..>>>>vv.v>....>.vv.>...>>>...>v>.>...v..v>v...>..v...>.v..v>.v...v.....>vv........>....v>v..v.>..>v..
>...>v......v>.>v...>.v...>>v.v>..>v...v.v..v>.>.v>.>...>vv.v>vvv.>..>..>...v...>>..>.>v.>vv.v..>>.v.v.v..>.v>..v.>..v...>>v.>v>v.v.v.>..>.
..v>.>>v>>..>..vv>>..>.>>vv..>..vv....v.>v>.....>v>..v.v>.v..>...vv..v.>>vvv...v>v>.>.v.>>>.v>...v>.>v.v>v>..>...>....>>>v..v..>>...>.v....
....>...vv.>...vvv>v..>vvv>>..>>>>......>>>.v..v>vv>v>.>....>.....v.v..v.v.....v.v..v.v..v>.>v>v>.>.v.>v>....vv.v..>.vv..>..vv>.>v.>.......
vv.>.>...>vvv.>v.>v>.>.>.v..v>..>.>>.v>.v>.v.v..v>v...v..>>.>>.>.>....v.>..>>vv>....>..>>...>>v.>.v>>..>>...vv.v.v.>>..v.v...v.v>..v.v..vv.
.>v.v..v.v.>.v.....>.v...>.vv>.>....vv.v.v..v>.v>v>>>.v..vv.>vv.v....vv..vv.>>>v>.v.......>.vv.v..>v>v...v...>..>vv....>.>.>.>>v...v..v>>.v
...>v.>>.vv...>v.v.v>...v.>vv..v.v...>>>>..>.....>.>v.v.v>.v.v>.>>.>...vv..v....v>.v.vv..>.v>...>>..v.v.v.v>.v.v>v.>..v.>v..>>..>vv.......v
>....v..>..vv.>.v>..>.>.>.>>v..vv.>vv...>>v.>.vv.v.>.v..>vvv>.v...vvvv>vv.>>>.>>..v.>v>>>..>>.>.v>>>v>>>..v>>.>.v.>...v.....v..>..>>.>v>..v
>..vvvv>>..v>v>......>...v>...>>>...>.v>.>.v>.>>....vv..v>>>vv..>>>v.v>.>.v..>.v>..v>....vv>.>.v.....>v>.>.>.v>v.>.>v>v....v.>...>.v.......
.v...v.....>>v.>vv.>v.>>.>.v>>.v...>>.v..v.vv>>.v...>>>v.>v>>..>>...vv.v>v.>..>v>.>v>>..>>.v...>..>.>..vv.....>>.>.vv>v>>.>..vv>.v.>v.>.v>v
.vv>...v.>.vv.>>...v..>.vv...>.v.....>>..v..>v.>.>...v>..>v.v>.v.>v....>..>..>..>.>.>.>.>..>.>.>.>..v..v>>v.>.v>>.....v..>.v.....v>..v....v
.....v>v..vvvv...v>..>.v.vv.>.>.......v.>..v..vvv.....vvv..>...>.v.>v.>v..>....v>.>>...v>...v>..v>v....v...v.v.>.>v>...v.vv.>...v.>>v>v>..>
>v...>...>..>.v.>>>>.>v.vv>vv>.>.>.......v>>v.>vv...>>.>..v..v>vv..>.>..>v..>v>>>.v>>v.>.>..>...>>..v..v>>v.>vv>>.vvv>..v.>vvv..>..v>vv..vv
..vv.>v...>>........v.....>>..>>..>........>>vv.>.>.....vvv.vvvv>>.>..v.>v>...v.v..vv...v.v..v..>>v...v.>>>>...vvv>>>v>...>vv>v>.vvv..>v..>
..>.........vv.>....v>>.>>vv....>>vv....>..>.>...v..vv.v>..>v>.>v>>.>>>...vv>.......v..v>v>.>.>vvv.>...>.v.>>v>.v>>....v..v........vv.>>.vv
..v.>>v.v..>..>>.v..>.v>>>...>..vv>v.>...>...v.vv>.>.v>..>v.vv.......v...vv>.>vvv.>...>>.v.vv...>..vv..v>...v...>>>....>.>v.>.v...v......vv
>vvv>.vv..>>.>....v..v>>>>v.>.>v....v.v...>>>..v.>..>v..>.vvv..v>.v>.v......>.v.v>>v.v.>.v...>.v.>vv.v>v..>..>>>.>v>>.vvv>>vv>.>v.>..vv.vvv
>>>..>v.v>.vv.v>v>vv...v........v>.>.....v>v..v.>>>.>v..vv..>....vv.v>..v....>>>>vv...>v..v>.v.vv.>..>vv.vv...>>..>>.....vv..v>>..>....vvvv
v>......vv>>.vv..v>v.v>>..v...>.v.>...>>..vv.>...vvvv.>v.>...>v.vvvvv..>>.....>v.>....>....>.>.>v..>.v.vvvvv..v..>vv.v>.v.v...>v.>..v>..>..
.v>>>>..vvv>v.vv>.v>vv..vv.v.vv.>>v>.>..>.v>v....>....v>>>.>.v.vvv.>>...v..>v>...v.v>>v>>v.v...v.v...vvv>>v.>.>...>v..>....>>.>..>.vvv>.v>.
>>.v...>.v>...v>v..v.vv.v..v.v.>...v>v.>.>>.v.>.v>>>.>>.>..>....v..v>>>.v>>.>..>>.>.vv.>>.vv.>>>v>.>>.>.v....v>....>..vvvv....v....v.v.v>vv
>..v>vv>.>v.>.....v.>vvv>..>.>.vv>>>..>.....>..>v>.v...>v..>...v...vv..v>>>v.>>..vv>>..>.>>>v.>..>v...v.v..>.>..>.>>..>.v.v>....>...v...v..
>.>.v...v..vv.>>>vv.vvv..>...vv.vv>...v.v>>>>.>.>>v.>..vv...>v>>v>..>..>vv..vv>>.v>>...>.>v...>..>.>>>.......>.>>.>.>....v.v.............>v
...v>.vv..vv...>v>..>>.v..vv.>.v..v..>..>>.>vvvv.vvv.>>vv>v>.>>v>..>...v>...v...v>>.>..>.>.>v>.v..>>......>v...>v>v.>>.....v>..>.>>>>v.v.>>
.v..vv>....>>...v>.v.v.>.>>....>..v>>.v>v..>......>v...v.>.v......v..>v..>....v.vvv.v..>vv..v.>..v..>>>....>>>>v.>.....v>>.>..v..v>v.v..>..
v>......v..v..v>.....>v>>.>v>v>.>>v>v>v>>...>.....v>.v>...v...v.....>>...v...>.vv..vv..>.>>...>v.>.vv>..v.v>..vv..vvvv.>v..>....v>.>..vv.>>
>.>..v>v..>.vv>>.v>>>>>v>....v.v.>vv..>>...v>v>v.vv>.>>>..>.>v.>>v......>>.>v..v>.vv...vv.v.vv>.>....>.>v...>.v..>.>..vv>..>.vvv.>>>v.v....
>.>.vvv.v>.>vvv...v.>..>.v.>.......>.>....v..>..>...>v..>v....v..>v.v>v.v.>..v.vvvv>>v>.>>.>>>...>..>v>..>v.>v.v..v>>vv.>..v.v>vv...vv>..v.
.v>v.v..>...v>v>.>vvv.>.v.....v.>.>>..v>v>.v.>.>....>.v..v.>v.v>.>.v.vv..v>>v>vv....>>....>vv>v>v>>.v..>.vv..>>>......>>>>..v>v>v>.>>..v..v
..>v.vv..>>v>v.v.......vvvv>vv.v>.v...v>v>>.v>.>.v>..vv...>v.>...v.>v>..v>.vv>....>>..v.>.>vv.vvv.>....v...v>.>..vvv>.>>vvvv>>v....>..>>.>.
.v.v.>vv>.>...v...vv.....v...v>>.>v.>vv>.>>....>>...v.vvv..>>..v.>vvvvv>..v.>....>v.>.......v.>.v.v.>..>>v>vv>>vv.>v.>v>>..>.v>.vv..v..vv.>
...vv.v...vv....>..>..v.>>v>v.>.v...>...v>...v>>v...>v.>>.v...v>>v...>..>v..v>..v..>.v>.>.>..v...vv>v.>.vv>>>..>>>vv.>..vvv..v.>.>..vvv>.v.
.>>.v.>.>..v>..>v>..v>.v.v>>.vvv..vv.>v.>>.>.v.vv.v.vv>.>.vv>.>..v>>.>.v.>v..>>v...v..v>>.>.v>.>.>v..v.v.>>>vv.v.>...v..>v.....>vv..v>.>>>>
.>.....>v>>>>....v..>>>vv...v.>>>v..v>vv>>.>.v.>.>v>.v>v..>..v.v...v..v.>.>>...v.>>v.v>vv.v..>.v>.>>vv...v.v...>>....v.>..vv..vv....v>.....
..v>.>v..v>...v>.>..>...vv>v>vv.>...vv>>..v>.v.>....>....v..>v>.>...v>>vvv....v.v..v>.vv.v.vv.v..>v>>..>...>v>>....v.>>..v.>v.>v.>>v.v.v.v.
.>.v>>>v>.v.vvv...v>....vvvvv>>v.vv>>>>>....>.....>>...vv.>vvv..>.v..vvv.vv>vv>..vv>>vvv...>.>.>.>...vv>.>v.v.v..v>v..v.>.v>>.>vv.>...v.v.>
.>....>>vv.>>>>.>v.>.v..>.>>.vvv>..v..v>..>>.v>.>>>.v.v>>vvv>v...vv.vv..>....>.v..v.>.v>..v....v..vv>v>.>..>..>>>.>>>.v.vvv.v..v......vv.vv
.v.v>>>v.>v.>....>..>.>v.......v>>........vv.v>>>...vvv.>>.>.v.>v.v.>...>v.v.....v.v.>vv>.>>v>>..v>>>..v.v..v......>.v>.>.>>v.v.v.vvv>vv.>.
.>..>....>>.....>.>...v.v....>v>>>v.>.v>.>vv..>v>v>v.>>>>>>v.>>>>>.>.>>.v>......v.v.v.v...>.v..v...>..>>>>>.>.>..>.vv..v>.>..v>.v.v....v.>.
..v>>>>.>>>>....v>v..>>vv.>>..>..v>..vvv>.>..v.>...v>>..>.>>>..vvv.v..>.>.vv>...>vvvv>vv>>>vv..>...>v.>vv....>v.v>..>vv....>v>..v>.v.>v>>v>
.>>.>>>v.>.v>.>.v>.v.>......v...>.v.>..>.vv.>v..v>.v>.v..v...>.vv.v>>.>v.v..>v.>...>>...v.>>v.>>..>v...v.>...v>.>.v..v.>.>....v.>>>>v.>v.>.
>vvv..v.v>>..>..v.>vv.vv>..>vv.v.>...>v..v>>....>>...>>.>>....>...>v>..>>>..>...v.>v.v>.....>..v...>vvv.vv.>>.>v>v.v>v..v>...v..>>.>..v...>
>>.>>...>.>>>..v>>..>v..vv>>>>.v.>>v..vv..>.>..vv.....v.v.v.>..>>>....v.v.>v>>vv....>.....v>v..v>..vv...>..>>v..vv...v.....>vv..v>.>..>.>..
..vv>.v>.....v..>.vv>>...>v...>.v.v>>>........>vvvvv>>.>...>.v.v..v....>.>v>>.v.vv.v..v.vv.>.>v>.>v.>..vv...>>..>.....v...>>>v..v..>.v>>v>.
.vvvv>.>...>>.v..>...vvv>vvv..vv>.>v>.....vv.v..v...v.....>>>v.v>v>>.>v..>>>..>.>v..vv...>vv>.v.>.v..v.>>.....>v.>v>>.vv..v..>..>.>.v....v.
>v>>v...>..>.>>..v..vvv>...>>....>.>>....vv>...>......>..>>v...vv..>>>>>.>v.>.>.vv>>.>>vv....>.v>>..v>>...>v..>...vv..>.>..vvv...>.....>.v.
>..v>.>..vv...v.>>>.v>>.>....v.vv.>..>...>..v..>v.>vv.>..v..>.v.>...vv...v>>..>>vvv...>.>v.>.vv.>v..vv.>>vv.>>..>vv>.v.....>>...v..v.vvv.>>
v.v..vvv>...>v......v....>..>>>.....v>v>>>..v.v..vv.>.>>>>.>.v.>....v.>.>v>vv>vv>v..>.>.v.v>.....>..v>>v...v.....v...v.v.vv>>........v.>.v>
.v>>...>>v>.>...v.>>>....>v>>v.>.v.>>v.v>.>>...>.v.v...vv>v....v>v..>>.>v>.>..>vv.v>>.>..v>>v...>v>>>..v..>v>vv.vv>............>v..>vv.v.vv
>.....>vv.>...v>vvvv>vvv..vvv>.v.>...>v..vv>vv.>>>.v..v>v.>..vv.v.>>v....v...v.....>.v.>.>..>.v>..>v..>>>>>>>v..vv>.v.v>v.v>..>....>>>v>.vv
v.>.v>v.v>...>>>..v>..>>.>..v.v....>.>....v.>..>>>.>v.>.>.>vv..>.>...v.>.....>vv>.>..vv.vvv.>>.vv.>.....vvvv>..v.>.>>v..v..>.>>.>...v>>v..>
v..v>v>..vvv>...v..>.>>...v.v..v..>v..>>.>>.v..>>v...v.vv..v..>...v...v....>v.v.v.v.>.v>vvv.v.v>...>v>.>..>v.v>v>v..v..>>>>...>v.....v.>..v
v>v..v..>..v>.....>>>.v..>v>v..>..>v>...v..>....v...v>>vv.....v.vv...v>....v>..v>>.v.>.>>..>v>..>>>vv.>>>...>...v>vv>v>...>..v.v..>.....>>.
vv..>>v..>>>.>...v..v.>v>..v.>>>>>v..v>v>..>v>>>v.....v..>.>.>>vv.v....v.....>v......>.>vv..vv>.vv..vv...vv.v...>.v..>.>.v>v...v>..vv...>vv
.>...vv>>>.v.....v....>.v......vvvv>.>..>vv>v..vv..>v>>.>v.v>.v>v.vvvvv.v>v......v.>v>vv..>v..>vv.v.v.vvv..>.>.>>v.v.......>vv..v.vv>.>.v..
....v...v.>.v>>>v.>.....>>v>..v>.v.>.v.>..>v.>vv>>vv.>........v..>v>.v>>v>>v.>....>.>...>.>.v.......v....v>vvv..v>..>..v>....v...>.v.>.v...
..vvv.v>.>...>>.vvv>...v...>..>..>...v>v>..>>.vv....>.v.v.>.v>vv.>>v..v>.v.v..v.>.>>.v.....>.v...v>.....v....v.v.v.>>....v.v>>>.......>vv.v
...v>v>..v.v.v...>v>.vvv.vv..>..v.>v.>vv.>.>>..v....>.v.....>.v>..>..v>>vv..vv.>....v>>.v>...>.>vv....v>>.>>v>....>.v.v>v>>>>...>....>.>..v
.>>..v.>v..>>>v.v.v>>...>>v...v>....>.v>>...v.>.v.>...v>>vv.vvv>v....v>.v.>v......v.v.>>.>v...v...>vv.v.....>...>.>..vv.v..>..>.v>..>.v>.vv
>..>.>.>>.v.v.>.v.vvv....>.v>v.v..v.v...>...vv..>>.>..>>>...v>.>.v..v.>>.......v.....>.v>vv.>.v..vv>>>>>>v...vvv..vvv>>>.v.>.v..v.v>v>v>..>
v..>.v.vv>>vvvvv.....v>>v...vv....v>.>>v.v.>.>>v.vv....vv..v.>>.v.v.>v>....>....v.v>>>.>v.v.>v>v.v.v..>.>v>v......v.v>...>v.vvv...v>...vv..
>>vv.....v...v......>v.v..v>..v.v>..>>>.>>..>v>.v>>>.>v..>>>>v.>..vvvv.v>...v..vv.>.>v....>v.>>.....v>v....v..>.>.v>v.>.>.>v.v..>v........."""


class my_logger:
    def __init__(self) -> None:
        self._logfile=open('./2021/'+os.path.basename(sys.argv[0])+'.log.txt','w+')
        self._logfilemutex=Lock()
        self._enable=True

    def write(self, line):
        if not self._enable:
            return 

        self._logfilemutex.acquire()
        try:
            self._logfile.write(line+'\n')
        finally:
            self._logfilemutex.release()
    
    def __del__(self) -> None:
        self._logfile.close()
    
    def enable(self, e):
        self._enable=e

global_logger=my_logger()
global_logger.enable(False)
# global_logger.write(' '.join(['\n\t', thread_name, 'branch-end-len', str(len(main_list)), str(main_list)]))

class ThreadSafeData:
    def __init__(self, data) -> None:
        self._data=data
        self._mutex=Lock()
    
    def append(self, depth):
        self._mutex.acquire()
        try:
            self._data+=depth
        finally:
            self._mutex.release()

    def add(self, depth):
        self._mutex.acquire()
        try:
            self._data+=depth
        finally:
            self._mutex.release()

    def set_min(self, depth):
        self._mutex.acquire()
        try:
            if depth < self._data:
                self._data=depth
        finally:
            self._mutex.release()

    def set(self, depth):
        self._mutex.acquire()
        try:
            self._data=depth
        finally:
            self._mutex.release()

    def get_copy(self):
        return_data=None
        self._mutex.acquire()
        try:
            return_data=copy.deepcopy(self._data)
        finally:
            self._mutex.release()
        
        return return_data
        

class WinException(BaseException):
    pass

class ErrorException(BaseException):
    pass

class point:
    def __init__(self,x,y,z) -> None:
        self.x=x
        self.y=y
        self.z=z

class line:
    def __init__(self,coordinates) -> None:
        self.point1 = point(coordinates[0], coordinates[1])
        self.point2 = point(coordinates[2], coordinates[3])

    def get_line_points_hor_vert(self):
        # Bresenham algorithm
        number_of_points=max(abs(self.point1.x - self.point2.x), abs(self.point1.y-self.point2.y))
        number_of_points-=1 # adjust for end points
        x_spacing=(self.point2.x-self.point1.x)/(number_of_points+1)
        y_spacing=(self.point2.y-self.point1.y)/(number_of_points+1)
        return [self.point1] + [point(self.point1.x + i * x_spacing, self.point1.y + i * y_spacing) for i in range(1, number_of_points+1)] + [self.point2]


class MyThread(threading.Thread):
    def __init__(self, target, args=(), kwargs={}, name=None) -> None:
        def function():
            self._result=target(*args,**kwargs)
        super().__init__(target=function, name=name)


def get_key(dict1, value):
    for k,v in dict1.items():
        if v==value:
            return k
    return None

def get_keys_from_len_of_key(dict1, length):
    keys=[]
    for k,v in dict1.items():
        if len(k)==length:
            keys.append(k)
    return keys

def get_keys_from_len_of_value(dict1, length):
    keys=[]
    for k,v in dict1.items():
        if len(v)==length:
            keys.append(k)
    return keys

def get_keys_from_value(dict1, value):
    keys=[]
    for k,v in dict1.items():
        if v==value:
            keys.append(k)
    return keys

def has_all_chars(input_string, string2):
    for s in string2:
        if s not in input_string:
            return False
    return True

def get_all_indices_of_element(list1,element):
    final_list=[]
    for i in range(len(list1)):
        if list1[i]==element:
            final_list.append(i)
    return final_list

def bit_str_to_int(s:str):
    return int(s,2)

def bool_list_to_int(list1):
    # convert bool to int, then to list, then join them all as string
    # finally convert string "001010101001" to number
    return int("".join(map(str, list(map(int, list1)))), 2)

def hex_char_to_bin_str(c):
    hex=int(c,16)
    v=bin(hex)[2:] # remove leading'0b'
    v=v.zfill(4) # leading 0
    return v

def min_max_tuple_list(tuple_list):
    min_x=min_y=math.max_value
    max_x=max_y=-math.max_value
    for e in tuple_list:
        min_x=min(e[0], min_x)
        max_x=max(max_x, e[0])
        min_y=min(e[1], min_y)
        max_y=max(max_y, e[1])

    return min_x, max_x, min_y, max_y

def get_all_numbers_from_str(s):
    return list(map(lambda a: int(a.group()), re.finditer('-?\d+', s))) 
        

class Player:
    def __init__(self, index, position) -> None:
        self._index=index
        self._position=position
        self._score=0
        
#####################################################################################
        
def funca(lines):
    sea_cucumbers={}
    row_max=len(lines)
    col_max=len(lines[0])
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c=='>' or c=='v':
                sea_cucumbers[(row,col)]=c
    
    step=0
    while True:
        new_east_herd={}
        for (x,y),e in sea_cucumbers.items():
            if e=='>':
                new_y=(y+1)%col_max
                if (x,new_y) not in sea_cucumbers:
                    new_east_herd[(x,new_y)]=e
                else:
                    new_east_herd[(x,y)]=e
            else:
                new_east_herd[(x,y)]=e
        
        new_south_herd={}
        for (x,y),e in new_east_herd.items():
            if e=='v':
                new_x=(x+1)%row_max
                if (new_x,y) not in new_east_herd:
                    new_south_herd[(new_x,y)]=e
                else:
                    new_south_herd[(x,y)]=e
            else:            
                new_south_herd[(x,y)]=e
        
        step+=1
        if new_south_herd==sea_cucumbers:
            print('a',step)
            break

        sea_cucumbers=new_south_herd

try:
    start=time.time()
    print('sample data')
    lines = input1.split('\n')
    funca(lines)
    print('time',time.time()-start)

    start=time.time()
    print('puzzle input data')
    lines = input_main.split('\n')
    funca(lines)
    print('time',time.time()-start)
    
except WinException as e:
    pass