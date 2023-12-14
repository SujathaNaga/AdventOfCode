import sys
import math
from dataclasses import dataclass
from typing import Callable
import operator
import copy
from collections import defaultdict
from time import time
import re
from itertools import pairwise
import threading
from copy import deepcopy
from functools import cache

input="""#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1"""


input="""??#.????#???.#?# 1,5,1,1,1
?##?##??#? 7,1
??????#???. 1,7
??#?#??#.?#.??#? 5,1,1,2
???????.??? 1,3
?#..##?##??###??#? 2,13
?.????????.???????? 1,5,1,6
?.???#???. 2,2
??#..#???#? 1,1,4
?.?##?????#??? 1,5,2,1
.???#?????##??#.? 3,8
?????????????.#.. 4,3,1
..#???????.? 4,3,1
????#??.?.#??? 7,3
#??#???##??.?? 4,1,3,2
??#?#?##?.???#??. 6,5
???.#??.??###?.#?? 3,1,5,2
?.????##??#?? 6,3
???..?##????.? 2,3,1
?.?#????.??#?#.? 1,2,1,3,1
?.?###.???? 4,2
?#???..??##? 4,3
???#????#?. 1,2,3
#???#???#??#???.? 1,10,1
???????????????????? 1,5,6,3
???????#??? 2,6
??.??.????.?#?????# 1,1,2,1,4,3
???#???.??#? 1,4,1,1
???#???##??##? 3,2,3
????.??????#?.#? 1,1,1,4,2
?.#??#???? 1,1,5
??##???#?.##??..? 4,2,4
??????#.????.# 4,2,1,1
??????#??#?.??? 2,7,1
.????????##.?.?.##? 5,2,1,1,2
.??????????#?#. 3,1,2,1
?????????????. 2,1,5
?##????#?.?????.#??? 2,1,2,3,3
?????????#?.?????#? 1,2,1,3,4,2
..?.#???.?##.? 1,3,2
.??????????????? 10,2
?.?#????#?.??? 1,1,2,2
??????.#??.?.? 1,1,1
#???#?#??#????? 1,2,1,5
???.?.??#????.? 3,6
.#.???###???.#?..??? 1,8,2,2
.???.??#????# 2,4,1
.????#?#?? 3,3,1
?###??#??## 4,2,2
??#?#???#???.??. 3,5,1
???####??##..?#.#.?? 9,2,1,1
??#?#???#.?. 5,1
???#????#???##?# 2,3,3,1
?#???????#???#??? 1,3,3,3,1
#???#????#.##..? 8,1,2
?????.?#?#??? 1,5
.??#.??#?.? 1,1,1
?#?#???#???.??? 1,1,4,1,3
.????#.?.#??? 1,1,2,1
.??#?.??#? 4,2
#????????. 1,4,1
??.#?#????#?...?? 1,8,2
?#.#?#.??##? 2,3,1,2
...??.?#?? 1,1
?.?.????#..? 1,2,1
?##????????.??.?#??? 6,1,1,4
?.??#.??.?.???? 3,2
.????.?????.???.?? 4,1,1,3,1
?????????##???????#? 2,1,1,2,2,2
???.?????.????? 2,3,5
???#??????.??#??.? 1,6,1,1,1
??##??????###??? 12,1
?.??.?????? 1,1,2
??#??????#?.. 2,5
???#####????. 1,8
.?#?##??????#??.???? 6,2,1
?.#??#???????#????? 1,1,12,1
??????????#.?..?##? 1,1,1,1,3,3
???????#???.??## 10,4
.?#????.?.???..? 1,1,2
.???#?#????? 2,2,1
#????#?.????##?#?# 1,5,1,5,1
???.##??????##??#? 1,2,8,2
??#????????????#? 6,7
????.??.#.?#?#? 1,1,1,1,4
??##?#??.#???? 6,1,4
?#?.?#????????#?. 3,2,4,3
..??????##?# 2,1,2,1
?????????.???? 4,1,1,1
.??#?????.?.?. 1,6,1
#.?#?#??????#??# 1,6,2,1,1
.#?.#.##??# 1,1,5
??#?????#?????? 5,4
.#??.?.?.? 2,1
.?#???##.????##?? 7,2
?#?.??????#??????# 1,8,3
?.#??#??.?#.. 4,1,1
?#?#?#??????? 7,1,1
?#???????? 6,1
????#..?#???##? 1,1,2,3
..?????#?###??.? 1,9,1
?##???.???#?# 4,4
??.??#???..??#? 1,2,1,3
#?#??????.??#?? 8,1,3
???#?##?#?? 2,6
.?.???#???.#?????? 1,3,1,5,1
?#.???????# 2,2,1
?.???.??.? 1,1,1
?#?#?#??????#??#??? 1,5,2,4,2
?#??.?#?????.?#. 4,6,2
#???.?#?#??#?.??#? 2,7,1
.??#...???????. 3,1,1
?..???##??. 1,6
??#??#?#??? 2,4
?.?.??.??????#?. 1,7
?.?????????.??. 2,2,2
???.?????? 2,1
???.??????????? 1,3,4,1
?#????#???#??? 10,1
??#???.?????#???# 6,3,1
????.?##??#??# 3,8
?????????????. 1,7,1
?..?????.#???.. 1,4,2
?.???#???#? 1,5,1
#???.????? 2,1,1
?#.??#?.???? 1,1,1,1
????.?#???.???. 1,1,4,2
.?#??#??.??????? 2,4,6
.??.?##.??#?#.??? 2,3,2,1,1
..??????#?.?? 2,2
???#?#??.##. 3,2,2
?..?????????##?#??? 1,13,1
??#?????#?.??#?????? 6,2,5,2
???.???#???# 1,1,3,1
??##????.?. 4,1
??#??#??#?. 3,6
.??????#????#.#.?? 1,1,8,1,1
?#?#?.?.?.###??#???? 5,1,1,3,1,1
???.#?#???.?? 1,1,5,1
?????####??????? 2,5,2,1
????.??#??#? 1,1,2,1
??.?????#?#.????? 2,3,3
?#??#?#?.????.??? 2,3,2,2
?????????#??.??????. 1,6,1,1,1,1
???.##?##??#? 1,6,1
????#?.??.. 4,1
?#??#?#???.????#?# 4,4,6
?????#??#.#? 1,2,2,1
?#?#?#??###??? 1,1,7
.##?.????? 3,3
??#???###????? 1,6
.?###????????##?#?? 7,1,5
..?#????????#? 3,5
#?#???.??? 1,1,1
#???????????#??.??? 10,3,1
???##??#??#?.?????. 10,3
?#?????.???????## 3,2,5,3
??.??#####???. 2,8
???.?????? 1,1,3
???#???????????. 6,4
#???#?????##???.?#? 2,1,1,5,2
?#?..???#??????. 2,7,2
?????##?#? 2,3,2
.#?..????# 2,3
???????#??#.?..??.. 3,1,1,2,1,1
?.#??#????? 1,3,2
???..?.?.? 1,1,1
?#.?#??#???.##.? 1,1,4,2
???#?#.??#??? 4,1
??????#????.???? 6,1,1,1,2
???..??.#???? 1,1,1,2
????????.? 1,1,1
?..#??.??. 3,1
?##.??#??? 2,1,1
?????#?????#?#?? 2,12
?#??????#???.?? 1,6,2,1
#??.???.??##???.#? 2,3,7,2
???????..????#????? 2,1,1,7,1
????#??.?????? 1,2,4
?###?#?##?##??.??. 12,1
?#??#.?.??#?... 3,1,1,1,2
??#??#??#????#? 9,2
???????##????? 1,1,5
?.?#????#?.??.?? 3,3,1,1
???..??????#..??#? 1,1,7,1,1
??.???###???#..? 1,1,5,1,1
??.??.#????#????# 2,1,7,2
??????#?#??????# 1,6,1
#?.?...??.??????? 1,1,1,6
??#?##??#?..## 7,2
?#?###..?.#?##??.?.# 5,6,1
.??.?.???. 2,1,1
?.???..?.?#?.??.???? 1,3
.#?.??????.?.?#??? 2,6,4
???##...??. 3,1
????????????#?????. 4,6
????#.??#? 1,1,1
?.?#.??..??#?????..? 1,2,1,8
?????.??.? 1,2,1
??????##?.?? 1,4
???.????#??? 1,1,5
.??#???.#.#??#??. 6,1,2,1,1
?.????#??##?????? 1,1,1,7
??????##.??? 3,2,1
?.????#?????.?.? 1,4,2,1
?????????????## 1,1,2,4
.?##??#??.??# 4,1,3
??#?##??#?? 2,5,1
?????.###??.?.#??# 1,1,4,1,1,1
.????????##?#? 1,7
??????????.? 7,1
.?????###????..#. 12,1
????.????? 3,1,1
#.??#????#????#????? 1,5,1,7,1
.##??????.??##? 7,3
?..?.???#?????###? 1,1,5,5
??????#???. 1,1,3
??.#???????##????. 1,2,3,6
?.?.?.?.#???????#?. 1,1,1,1,2,7
?????#????????. 1,1,1,4,1
?.??#??#?? 1,1,2
??#???.#.?#?#?? 1,1,1,1,5
?????????.? 4,1
??.?????#?.?.#?? 7,1
??.?#.?????#??. 2,7
?????##..? 1,4
?????????. 4,1
??.?..?#???? 2,3,2
????.####??###? 2,4,4
?####???##??????? 10,1,1
???#?#???# 1,5,1
????###.??.?????#??. 6,1,6
#???????#?. 2,1,4
?#?.???##???????#? 3,1,2,1,6
???#??#?.?.?????? 1,5,1,1,4
?.#???##???.?.## 1,3,2,2
???..##?.?.? 2,2,1
?.#?#?????. 3,1
????.##?#?#??##?? 3,12
#?##???????? 1,3,3,1
???.#?.????##? 1,2,1,4
???.??#???? 1,3
.???###??.???????# 7,5,1
?#.??.?#???##?. 1,1,1,4
.????###????? 2,6
???#???.???????#?? 1,2,1,3,4,1
.?.?????????? 3,5
??#???#?.###????.?? 7,3,1,1,1
#??###??#?#.????? 11,1
#.?????#??#.##???.? 1,1,7,5
??????.????#???? 1,1,4,1,1
?.?#?#?#??###?? 7,4
????#???#?#?###????? 1,2,10,1
????#????? 1,4,2
???.#??#????.?#??.?. 3,2,1,1,4,1
?????.?#??????. 1,2,1,1,1
?#???????#?#?#???.? 2,12
?#??..??.???###?? 4,2,1,5
##????????#.? 5,2
#?#?.?.??###??#?. 4,8
??##?.???? 3,4
?.????##???????? 8,1,1
#????#??#???#?#.??? 15,1
?.?????.#? 4,2
?.##???..?? 1,3,1
#????#??????????#?? 2,7,2,3
???.????#? 1,1,2
??..#?????### 1,3
????????.?? 2,4,1
#??##??#.?????.??? 1,5,2,1,1,1
???#.?#?#?. 3,1,2
?##?#??????#?#.# 3,3,3,1,1
??.#?..??? 1,1,1
?#??.???#? 1,1,3
???#???????.??##?? 8,3
??.#.?#???#??.? 2,1,7
??????.####?.?#?# 4,4,4
??????????? 2,2,1
?#?.??.???.? 2,2
????#?#?## 6,2
.??###??????.? 5,3
.???#.#????? 3,5
?##?#?.?#?#??. 6,2,1,1
#.???.??#?####?..? 1,1,1,8,1
????#???#???# 1,1,2,3
?????.??.#???#? 3,5
?#??..?????????#?. 1,1,3,1,4
#?????????????.?? 6,1,1,1
?#?????..?????#??# 3,1,1,5
???????.???????????? 1,4,1,9
.????????????.. 2,1,6
.?#??????. 2,4
??#??#???#.???#? 1,5,2,1,2
.?.???????.?.#??? 4,1,2
##?.??##?..???. 3,4,3
??..??#??#?. 1,6
??#??????????##???? 2,6,4,1
??..????##?????? 1,5
##????????.??.#??? 2,6,4
?#??#...?????# 2,2,1,2
?..??????.???.?# 1,1,3,1,1
.?###??#???#???? 7,4,1
?#?.?????. 2,2
??..????.?????# 1,1,2,2
??##.#??????.##??#?? 1,2,1,1,1,5
??.##??????#???#??? 4,8
??#?????????. 4,3,2
#????.???? 1,1,1
?..??.?????? 2,3
??????#??###???? 1,1,9,1
?????#?#???????.. 1,6,3
?#??.???#?##. 3,3,2
?..##?#???????#?? 9,1
???.?#?#?#?. 1,5
???##?#???#?# 8,3
?##??#??.??.???????? 2,3,1,6
.??...?????????#.#? 1,6,2,2
????.#??#?#.##?. 1,1,1,3,3
?#?#?????.??????. 5,3
??.????##???. 1,5
????#?.???? 2,1
????..??#???. 4,2,1
???????.?# 2,1
????????????? 1,1,3
???##??????###.?#? 2,2,2,3,1
??????#?#?#?#?## 3,10
?????#??..????????? 8,5
??##???????.??? 6,1,1,2
?.???.????.??? 3,1,1,3
.?.???.??? 1,2
.???###???#??.?? 5,1,1,1
????#?.##?###.# 1,3,2,3,1
.?#???????? 1,4
?#?#?????????### 8,6
?????..???.???? 4,3,1,1
..?#?.?#??? 1,5
.????.??#? 3,3
?##????.?#??????..?? 7,3,3,1
?????##??.?.??...?? 9,2,2
??..#??####??.?.?#? 8,2
??????##????? 1,1,6
??????#??.???#? 7,5
???#..??.????. 4,1,2
.#?.?###??? 1,4
????###?...?#?#? 8,4
?????#???#??????? 1,1,6,1,1
.??#?#?##??????? 7,1,1
.#.?????#.?#### 1,2,1,1,5
?#??..#??.#?? 3,1,1,1
????#??.???. 3,1,3
#.???#???. 1,2
???.???##.???.? 1,1,2,2
?#?#..?#????##?.?. 3,9
.?.??.????? 2,2
??????.?.##?#?.? 5,4
???#???.????? 7,1
??####?????.???#?? 6,3,4
?.?...?#.#?#??? 1,2,5
??.??#??#?#?#??.?? 2,3,7,1
?#?.???????? 1,1,1
????????#?##?#??? 1,2,9,1
#???.???#????.??#??? 3,1,1,1,4,1
.??#?.?.#??? 2,1,2,1
.?##?###.###?#?.??. 6,5,2
.?.???????#????##? 3,10
?.##???..#? 5,2
????????????#??.???? 1,1,10,1
??##??#.??#??#?? 5,3,2,1
?#???#.??????..# 6,4,1,1
????????.? 1,2,2
?????#??#??#????#??? 14,2,1
???#??.???#?#???? 4,7,1
.?.##?.???#??..????? 1,3,4,2
??????#??????? 1,1
..#?##??.????. 5,3
??????????#.? 4,1
#????.???.? 1,1
.?..?#.??? 2,1
?#.??##??.##?.?? 2,4,2,2
??#????#??????? 9,1
.#?.##?##.#???? 1,5,1,1
?#?###???#??#?.??? 11,1,1
???#??..?? 3,1
#?#??????#?????#? 12,2
??#?#?.???.? 2,2,3,1
?#???.?.??#?#???? 5,1,8
.???#?#??#?????. 10,1
??????.?????.? 5,1,1,1
.?.??????????# 3,7
.#?.??..##??.?#..#? 1,1,4,2,1
?##?#??.??###?????# 2,1,1,1,7,1
?##?.???.? 2,1,1
?????#.#?##.?#? 1,1,4,1
?#?.??.?#.#.##.? 2,1,1,1,2
???????.#.??##??.?. 6,1,3,1,1
.?#??#???????#???.#. 3,1,1,2,4,1
?????#?.##??##??.?? 1,2,2,3,2
#??.???????? 1,1,1,1
????#?.##?.?#?#?# 5,2,5
.?.??.#?????????..?# 1,1,6,1,2
???#?#?????. 7,2
???????##??#?.?#?.? 1,8,3
.?..?#?#???? 4,1
??.?#??.????. 1,1,3
????##???##???#??? 12,4
?###?#??..#?.??? 6,1,2,1
##??..##?#????# 3,2,1,1
?????#?##??##???#?? 2,13
#?..???##???##?#???? 2,6,4,1,1
.????.?....#????. 1,3
?.?.??#??#.?# 1,2,1,2
???#??.??#.? 1,1,1,2
.????#?#???#??????? 12,1,1
?..#??#?##??#???? 1,1,2,3,5
.#??##?##??????.?# 2,11,2
.?.#?#?.?#???#.? 1,4,6
?#.##??.????? 2,4,4
???.??????.??. 2,1,1,2
???????.?##.#???.? 1,1,1,2,3,1
??..???????#?.? 5,2
?????#????? 3,2,2
.##????..#??.. 6,2
????.??????.???###? 3,3,1,5
??????#?.???# 1,3,1,1
????#????. 6,1
??.?#????. 1,4
??????#???##???. 6,1,3,1
?.?#.????. 1,1,4
?##??.#?#??.#?? 3,1,1,1,1
?.?#??????. 1,5,1
???????#?. 1,4
???#????#?##?#?????? 2,2,1,1,6,1
??##.?????##??#.? 1,2,7,1
????????.# 4,1
.???#????? 1,1,1
?.?#??.????.?#?? 1,4,2,2,1
.?##?#???.??..?#? 3,3,3
?#??.?.?#??? 1,1,4
????..#????#.?? 1,1,1,3,2
???#?..??? 5,1
?##???##.?. 3,2,1
??#???.???### 2,1,1,3
????.?#??##?. 2,2,2
?#???##??#?????#.??? 2,11,1
???#??..?##??# 5,6
????.??#???.#?#.?#?# 2,5,1,1,1,1
?.??????#??? 2,3,2
#.#???..????????. 1,1,2,6,1
?.?..?.#??????##?? 1,1,1,1,3,5
.??.?.???? 1,1,4
#??#.?#?#???#??????# 1,1,2,1,1,8
?????.?#..#. 3,1,1
????##???.?????.. 5,3
.????#???????? 1,5,1,1
##?..#.???#?????? 3,1,1,2,1
#??##???????????. 1,11,1
????????#. 2,1,2
.#?#?????????. 1,4,2,1
#??#??.????????????. 5,5,2
..?#?#???#???????.?. 9,1,1,1
?#?.?????????... 1,6
??###??#?#?.? 5,2,1,1
.?????????.??... 6,1
?.?.#??#??????#?#. 1,2,7
??.?#?.#??.??. 1,2,2,2
?##?#.?#?. 3,1,1
??.??####???... 2,6
.?????#????..?..??## 7,1,3
.#?##???.? 5,1
?.?.???#.???. 1,1,2,1
?????.???## 1,3,2
.????#??.??.?. 5,1
.?#??.???? 2,4
??#?.??#?? 2,2
?.??.??????.?????? 1,1,2,1,1,5
?????#??????.??? 1,5,2
#..?#??.?# 1,2,1
???????#???#?#???.? 5,8
??.?#??#?? 1,2
????#.#??#? 3,1,1
#?#?..?..?????#??? 4,1,2
??????.?##?##.??? 1,4,6,1
?.????###??? 1,8
??##???????##?????. 8,4,1
?#.?#.?.?????? 1,1,1,6
???#?.?.#??##???##? 2,10
.?????#?.?##????#?# 1,3,2,5
#?.?.?#?..???#? 2,1,1,2,2
..???#??.??#?? 5,3
.????##??? 7,1
??#?###???# 7,1
?????????????????. 10,5
??#?#?????????###?? 3,1,1,1,4,1
????##???.#??? 1,6,1,1
.##??????##?..??#?## 11,2,2
?#.????????? 2,1,1,2
??????#?.??#??..???. 3,1,5,3
.?##??????????#???? 3,1,1,1,2,1
?#?...?#?????#?.? 2,8
###?#.#?#?????.#???? 5,1,2,2,4
?.???#?#.?????#?.? 6,5
#????#???#???#?#? 2,2,3,3
??#??.??#.?#? 2,1,1,2
##.?...????????#?#? 2,9
??#?#???#???? 4,1,1,1
.???#?.?????.?#?.#. 4,1,1,1,1
??#.?????#?????##? 1,1,1,7
#???????#?????#? 1,1,8
????##?#?#??##???#?. 1,8,6
#.???.?????.#?? 1,1,2,3
##?????#??.????#? 2,1,3,6
#???###?##.? 1,4,2
#..??????#???.. 1,10
?????#???.?#?#??# 7,7
???.#????#?????.#? 1,1,1,6,1,1
??.#?#?????????.?# 1,4,2,2,1
?#?#?..?#? 1,2,2
?.?##.???###?? 3,5
.?#????#??..?? 2,5
???#.#??.?.????..#?? 2,3,4,1,1
???#..?????.? 1,1,5,1
?##?#??????##? 4,1,5
??#.#?###?##?????#? 1,1,8,1,1
.#?#??#.#?.? 1,1,1,1
????????#?#?##??# 5,1,1,5
.??#?.?#?????.?????? 3,7,4
?#?????#.?#? 2,5,2
????.?#????#?????#? 1,9,2
?#????#???.??.??.. 7,2,2
?#.##???????.?#.? 2,5,1,2,1
?.##?#?.????#?#??. 2,1,6
?###??#.#????##.?? 5,1,1,1,3,1
.??#?????#???#?.# 3,1,2,2,1
?.????.??.#?????? 1,3,1,5,1
????##?##?? 6,3
.?#???.?.????? 2,1,4
?????...??.. 1,1
??#????..??# 1,2,2,3
?###.?????#.???#? 4,3,1,2
???##????.?#.?#??? 1,2,2,2,5
?#.?????.?###?##??.? 2,5,6,1,1
.????.??.?????????? 3,10
??.?#?#.#..??? 1,3,1,1
?.?#?#??.?. 5,1
???#.?????##???#??? 2,13
??#???#.#???#???#?? 2,2,11
?#???????? 4,1
??????##???##????# 2,10,1
???#????#?? 3,1
##????#.?.? 3,2
.????#?????? 6,1
?.??.????#? 1,4
?????????.? 1,4
#?#??#?##????#????#? 14,3
#..#????#??? 1,1,4,1
.?.##????.?? 1,2,1,2
???.#??#?#?.?????? 1,1,7,1,1,1
..?#????.#???##????? 3,2,7
?????.??.? 3,1
.?#??#?#..?#?.?##.?? 2,4,2,3,1
???#?????.# 8,1
????..##?.??#? 1,2,3
.?????.?#? 1,1,1
??#?.#?#?#?.###?. 1,5,4
???.#????##.???##? 1,3,3,5
?????????#?#?????? 7,2,1,1,1
#.?##.???.?#?..?.#. 1,2,1,2,1,1
???#.???.?? 1,1,3
??.?.??###??.????.? 1,1,7,1,1,1
.?.#.?#?##?.???# 1,1,5,1,1
???###?#???# 8,2
?.????.#..##??? 1,1,2,1,4
??#????####???#?. 3,8
#..?#????##?#?. 1,3,3,2
###.??.##.? 3,1,2
???##?.????#?#??? 4,5
?.??.?.?.??? 1,1,1,1
.#???##??#???##???? 1,1,5,4,1,1
?..##..??#...?.?.?? 2,1
?#..#???.?.??# 2,2,1,1
????#?.#??.? 1,3,1,1
?#?????#???.????? 3,3,1,2
#.????###???.?#???? 1,7,2,2,2
?????.?????? 3,1
.??#???????. 3,1
?.?#??.?#???##?#?? 1,1,1,11
?#????#?#. 4,1,1
..#?###???#.??? 1,7,2
#....????? 1,1,1
?.????????.? 4,1
##?.??????.#??? 3,2,1,1,1
?????.?#.?????#??.. 2,3
?#??##?#?#?.??##? 7,2,3
.?.?????##.??? 1,2
.#?##?##?.?????.?#.. 7,1,1,2
???..???#?. 1,1,2
...?.???#?#? 1,4
?????#????#.? 7,2
??#????##???##. 3,2,4
???.???????. 2,1,1,1
###?..?????.. 3,4
.???????????..?. 4,2,1
?.?.#??.?? 1,1,1
?????????????#?? 6,6
..#?????.??? 4,1
???#??#?##.?#?.?? 7,3
#???###??????#?? 1,1,3,2,3
?##??.??#??????#???# 3,9,1
???#??#??.??????#??? 7,3,1
.???###??##?#.?.??? 6,2,1,2
?.?#?#?.?.?#? 3,2
.??#.?###???##?? 2,5,3
????.?????#??###?? 3,12
?#?##?#..#??#?? 5,1,1,2
??#??...???#?#???. 1,7
???##???.???#.?. 7,3
??.#???#.# 1,5,1
??###???????????# 5,4,3
#??..#??##.?????.? 1,1,5,2,1,1
????#.???#????.. 3,4
#?????.#??? 3,2,3
?#?.???????. 2,2,2
?.?????????## 1,1,4,3
#????????..#?#????? 3,1,1,3,4
???#??#??????????.. 7,1,1,2
?##.??###???#?#??# 2,1,3,1,3,1
?#?.???#?#?#?.??# 3,5,2
??#????.??#?#? 3,3,4
###?##???#?#??.?.# 8,3,1,1
.??.?#???#??? 2,1,3
.???#??###?? 1,6
???????.???????? 7,1,2,1
.??###?.??#.? 5,3
?#???#???????#?#???? 2,5,1,4,2
????.?????#?????? 1,1,7
.??.?.?#?##?#???#?? 1,11
?????#???? 5,2
?.??.???.#?? 1,1,3
????#???????? 5,3,1
#?##????#???#?.?#.# 4,3,1,1,1
??#??????#?? 1,1,1,4
.????.#?????#?? 1,2,1,1,3
????????????????? 1,4,3,2
????.#?.##?##?#?#?? 3,1,5,3
??#?###??? 1,3,1
????#???....? 8,1
.????.???.???..???. 2,3
?????.??#? 4,2
#??.#.????#.???###? 2,1,1,1,1,4
.???????.??????# 6,5,1
??#??#?????.??#. 1,4,1,2
??#?.??.??????#?#??? 4,1,3,1,5
?#??#???????#..??? 4,7,1
???#?##?????.?? 5,2,1
.?###?????#?##??. 6,7
#??#..??????#?? 1,1,7
.??#?#??????# 4,1,2
.###??####????#???# 4,13
????#?????.?. 6,1
#?##???#????? 5,1,2
??#?.##??????????? 4,4,5,1
.????#???? 2,1,3
?.?#.???????#?.????. 2,4,1,1,3
?.?#?????##??????? 2,10,2
?????..???##? 2,3
?#.#.???#???.? 1,1,1,4
.?##???##?????###??? 15,2
?#.#?.????.??.?#?.? 1,2,3,1,1,1
????#??????. 5,1
?.#.????##??.?. 1,7
??.?#?..??#?????.? 2,6
???##?.#?.?#? 3,2,2
?#?.???.?? 1,2
?????????..?#??? 1,1,2,2,1
?#.??..??? 1,1,2
??.????##???? 1,1,3,1
??####??????#.?.??? 5,1,1,1,1,1
.??#????.?# 2,1,2
..#?#???##???.?.??# 1,1,4,1,3
??.##..??. 1,2,2
?#???#?????? 2,5
????##?#?.???.? 5,1
.?#?..????#??.??? 1,4,1
.#####??????#??. 7,5
???.?.?.##?#???. 1,5
????###??.????#?? 8,5
?????#.???#?.?.?# 4,4,1,1
????????.?###????#? 1,3,4,1,3
?.?????.?#?????# 1,3,1,2,1
??.??????????? 1,3,1,1
???.?????#??? 1,6
?##???#?#????#????#. 3,3,3,2
??#?.?.???### 2,1,3
#??..?##??????.??? 1,1,3,1,1,1
???#??.?.#???#? 6,1,2
?#?..????? 3,2
?##??#???? 5,2
??.??????.?#? 1,4,2
.#?##???.???#??????? 7,4,1
?.#???..????? 4,3
.???..?#??##?? 1,7
.#???????.??? 1,1,1,2
?#?#???????##. 6,3
#.?.#?????#??#?#???. 1,1,1,6,4,1
.???????.?#?#??????? 2,5
??.?.?????? 2,3
???.????..#? 1,1,1,2
??#??.?#?..???##??## 2,3,8
#??.?.?#??#?. 2,5
?.????.????????? 1,2,3,1,1
???.??.??????????#. 1,1,1,3,3
???????.??? 1,1
##??#????????.?????# 2,2,6,1,3
??.?????##????## 2,1,1,8
???.??#?????#??.. 1,3,6
??#?#??#???????.? 7,1
.?#.????#??#? 2,4,2
?????.??#.??? 1,2,2,1
??##???.????????. 6,6
..???..?.?.? 3,1
??#?.??????.. 2,1
???????##?????. 1,1,4,2,1
??##..??#???. 2,4
?????#??????#? 1,2,4
..??#???#?????#?? 3,2,5
???.??#??.???#?#??? 2,5,6,1
?#?#.??##.?. 3,3
#??#.?????.?? 4,2,1
?#???.?#???#???.. 4,9
????.??????#?#??# 2,7
??#.??????????????? 3,7,5
??#????###? 1,4
???#????#.#.??.. 1,3,2,1,1
???#?.???? 1,2
?.??.?#??? 1,3
??.????#??#.?.? 1,2,1,1,1
..??????.?? 4,1
??#?.???.???? 3,1,1,2
?.????#????#? 4,3
?#?????????????? 5,4,1,1
?..?????#? 1,1,1
?.?#???.?? 4,1
#??#.????? 4,4
#??.?????????????? 2,1,1,3,2,2
.???#????.?? 1,1,2,1
??.?##?.??#??#?#??.. 4,10
????##????#???#.???? 2,3,2,1,1,1
????????.??###?????? 7,5,2
????.?.#??? 2,1,1
.#?..?#????#???## 1,12
#???##??.???????? 1,5,2,1,3
???#???#?.#??..? 7,1
?#????.???.?#? 6,2,1
.#?????????#???. 6,1,3
???###????????#?#?#? 8,2,1,4
?#?#..??#???. 4,1,3
.???##?#.??? 1,4,1
??????????? 5,1,1
??.#?#.???? 1,3,3
.#.###??????.#? 1,4,1,1,1
???#??.?.????? 1,3,4
?#.#????????????# 1,1,1,8,1
.??????###? 3,3
.#???????#???? 3,1,4,1
??#??.?#???#...? 3,6
?#???????.?#???.???? 9,4,1,2
???#.??#??? 4,3
??#????#?#.??.?# 1,3,4,2
????#?##?.??????? 6,1,2
.??##?#?###..#??.?? 3,5,2
??###???##?#?.??. 12,1
?..#?????#????#?# 2,1,2,4
????###?.?#??#??#. 8,6,1
????##?#????# 10,1
#?##?..?##?? 5,3
?#.?#??#???????? 1,7,2,2
.#?..?#?#??#. 2,6
#??#????.??#?#. 7,3,1
.?.??.????. 1,1,3
?????.???#?#??.?? 1,3,4,1,2
????????????#??#?? 4,8
????####?#? 1,7
?.#????.????#?.?? 1,6
?#?????#?##?? 3,4
?#????#????# 9,1
?##?#?????.??? 6,1,1,1
???..?##?..?????? 2,2,3
#.??.??????? 1,1,2,1
?##???##.?###? 3,2,4
#?##????#.? 6,1,1
.????.??###???#? 1,2,5,2
?.#??.??#???? 1,3,4
??##????#???#?#??? 4,7
?#?.???#??##???#?? 1,1,2,8
???.?#?##????.? 1,7
#.?##?#?.#.????# 1,5,1,1,3
#???..??#????#????? 4,5,2,1,1
???????.???????#? 1,3,1,2,1
##???????? 3,1
?#..?.???? 1,1,1
..??.#???##???#. 1,10
.?????##?????#????. 7,4,1
??..#?..#.#.#?. 1,2,1,1,2
????.?###?#??. 2,8
????.#?????? 3,6
??#??#????#.?.?#.??. 10,2,2
???#??????????? 8,2
???.????#??..?. 1,5
.?.??..?#. 1,1,1
#??###..???#???? 6,1,1
???###?..#?#??????? 5,7,1
????#??#??#?#?.??#? 1,1,2,5,3
????#??.?.?#???#. 7,1,1,1,1
?##?#?#?.??#?. 6,1
???????#?#???.# 1,4,1,1,1
???????##.?# 9,1
.?????#.???. 1,2,1,2
#.?#.??#?? 1,1,1
?##?#?????? 5,4
?.?##??.#? 4,1
?????##???.#?.##? 1,5,1,2
??????.??? 1,1,2
?.??.?#?#?#.?##??#?? 6,8
??#???????????.?? 8,1
#????????###??#??#? 1,2,8,1,2
#.#???#?#?#.?????#? 1,9,1,1,1
#.??#???##? 1,7
?????##?????????#??? 6,1,2,4
????#?##??????#?#?# 2,4,3,3
?#?.##????#???? 1,3,2,1
?.?.??#?.? 1,1,1
???????#?#???..??? 1,4
???.?#??##?#?##.#? 2,10,2
??#?#???..???.??.? 7,1,1
?????????.#.??????.? 6,2,1,1,3,1
?#???##????# 2,6,1
#?###?#??.#??..#.? 7,1,3,1,1
???.???#???#?? 1,5,1
??????#??????.???#? 7,4
#?????#??.???#.? 3,3,1,1
?.?..??.?##????.? 1,1,3,3
?##????.???? 7,1,1
?.?##.?#?#?????? 3,3,2
?.??.?.??? 2,3
?##?..????? 3,5
??####?..?? 4,2
???.???????????????. 1,7,6
#???####???.# 8,1,1
.#.???#?.????.? 1,2,3
????????????#?????? 2,3,9,1
#?#??#????????? 1,5,1,1,1
.?.????.?#.?. 2,1
????..#??? 1,1,1
??##?????#???? 4,7
?##?????.?#? 5,2
???????###????##?# 3,1,6,2,1
##?????.???. 4,2,2
??#??.??#?..# 1,3,1
????.#???????#?.. 1,10
####??###????#.???. 5,3,3,3
?#.?#???.?#? 1,4,3
#.?#?#???#.#??????? 1,4,2,1,1,1
??#????#?###???#?# 5,11
??.???#???#????????? 1,5,3,1,2
.??????#???####?.#?? 13,3
.??????#?#?.??.?#? 10,1,2
??..??##?#??????.??? 10,3
????#???#####?????.. 10,2
????#?#??#???###? 3,7
????.#?.?????#.? 1,2,6
???????????..? 1,4
?.???#?????.? 1,2,1,1
#??#??#?#???#?#.?? 1,8,3,2
?????###????.???? 1,5,3
???###?#?##????.??.? 1,9,1,1
.?#?##???#????##??.. 9,3
.?.?.?#????????##?. 1,1,1,1,1,4
?.??.??#????##??##?? 3,6
??????#?????.#?? 6,1,3
?#?#???????.?#?.???. 11,3,1,1
?.?#..#??????.??. 1,1,6,1
??????#???### 3,8
???#?#??.??##????#?? 8,1,8
.#?.??.??#? 1,3
?????.??????#?????. 2,1,1,10
??.#????#.? 1,2,1
???#?????????#?#?? 4,8
..??..?????.### 1,2,3
??.???#???.??# 1,7,1,1
?###??..?.??#??#???? 5,4
????????#?..?? 2,5,1
???##?#?????#### 2,2,1,7
?????#???#? 5,1,1
??#.?#???####??#??.? 1,11,1
?#?????##?#?? 5,5
??.??.?####?. 1,6
.???????#?????. 1,6,1
????#.?????.??.?#? 1,1,1,2,1,2
???.?#?????#.?#?.??? 1,4,1,1,2,3
.#??????.#?? 1,1,1,1
..#?.??????????? 2,5
.??##???????. 3,4
??#????#??????????.. 1,4,9
.??#??.#.?# 2,1,1
??.??????.?#????? 1,4
#.?#??#???##? 1,2,7
?###??.#.??. 4,1,1
???#???#???. 7,1
?????????#??? 4,4
???.???????#.? 1,3,2
?#??????##? 4,1,3
?#.??.??#?.# 2,2,2,1
?.#?????.????? 2,1,5
?.#???#.?#?## 1,1,2,5
#?#.?##???????#??.# 3,3,1,2,1
#?#???.?.#.#??# 5,1,1,1,2
??##?.##?????? 2,7
.??###?#??#???? 5,1,6
?.???#?????.?#??? 1,6,2
??.?.?#??.???.???? 1,1,1,1,3,1
???.???.###?##???## 1,1,1,6,3
#???#??##??# 6,2,1
??##??.##????? 3,7
?#?#?#?.???##???.?#? 4,1,7,2
.??#?#????.?##.? 8,2
.???#???.. 1,1,1
.????#??.#?#?. 2,4
#?.?????????..?? 1,1,1,4,1
?#???#??.? 1,2,1
#???????????.???.? 4,3,1,1
????#?#???#???#.?. 12,1
???.??#.?#???#? 2,1,7
??#?.#??.?#?. 1,1,2,1
??#.???#.?? 2,2
?????#??.????? 7,4
?#?????????###?????. 1,1,1,1,5,2
.?#?.#???? 2,3
???###?#?..??.#?# 2,6,1,1,1
..#?.???#?#???#??? 1,12
????##.???? 3,2
?#?????##?????? 1,2,5,1
??????#???# 3,1,3
.##??.???.? 3,1
???##????...??..??? 6,2
???????#???. 1,4,1
?#??#???##?.??.# 10,2,1
?.?.???#??? 1,1,3
?#?#?#??..?? 8,1
??#?.???????#?? 1,10
?.#???#?#??????? 1,2,4,1,3
#?#?.?##?????. 4,6
#?#??.???#? 3,4
?.?????#?#??. 1,8
?.?.?.#.??.??#? 1,1,1,1,3
?#???##??????##???.? 9,4,1
?#???????????.? 5,1,1
#???.??#?#????#?#? 2,1,11
??#???????#???????? 6,1,7,1
?#???#???????#?. 1,4,1,2
????#??.???#.?? 6,2,1,1
???.?#????.# 2,2,1,1
#???#..??#?#????.? 5,7
##?#..???.??.#?# 4,1,1,3
.?..???????.????.?.. 2,3
.???????.?? 4,1,1
.?####??#?? 4,1
??????#????#???? 1,1,6,3
??#???#.????#??. 6,2,4
?????????.#?? 5,2,2
??#??..??????? 3,3
.#?.??????#???. 1,2,1,1,1
????????.?#????? 1,1,1,2,2
?.??.??#??#?? 1,5
.???#??????# 1,1,5
?#?????.#?#?????? 2,1,1,3,5
???#????#????#??#?## 1,1,4,2,5
?.??.#.????..? 1,3
??????#?#??? 8,1
??#??.????#??.? 3,5
?????#.?????#?#???.. 2,2,6
????#.???. 1,1,1
???#?.???#????# 1,2,9
??#?#???###????#? 1,3,1,8
#.???##??##? 1,1,2,2
????#?????.#?.. 5,2
..????.?????? 3,4
????.??????? 2,1,2
.?#??????????.? 7,2
???#??????#?? 2,2,4,1
???##?????#??#?. 1,9,2
#????????.#??.? 1,3,1,1,1
.??.#???#?##??.?? 1,2,2,4,2
???.?????#. 1,2,2
????#????.??? 5,1,1
.????.??#?#?#???.? 3,5,3,1
??????##??#.??? 1,2,5,1
??????##.??.????.? 8,2,1
?.?.?.?#?#?.????#?. 4,6
..?????.?#??? 1,1,5
???#?????????# 1,6,4"""

# prep data
@cache
def calculate(record,groups):
    if len(groups)==0:
        return 1 if '#' not in record else 0
    if sum(groups) + len(groups) - 1 > len(record):
        return 0
    
    if record[0]=='.':
        #  move to next
        return calculate(record[1:], groups)

    n=0
    if record[0]=='?':
        # calculate possibilities
        n+=calculate(record[1:],groups)

    # calculate possibilities
    if '.' not in record[:groups[0]]:
        if(len(record) <= groups[0] or len(record) > groups[0] and record[groups[0]] != '#'):
            n+=calculate(record[groups[0]+1:], groups[1:])

    return n

def day12():
    total=0
    for line in input.split('\n'):
        record,groups=line.split(' ')
        groups=[int(x) for x in groups.split(',')]
        total+=calculate(tuple(record),tuple(groups))
    print('a',total)

def day12_b():
    total=0
    for line in input.split('\n'):
        record,groups=line.split(' ')
        record=(5*(record+'?'))[:-1]
        groups=5*[int(x) for x in groups.split(',')]
        total+=calculate(tuple(record),tuple(groups))
    print('b',total)
        

day12()
day12_b()

