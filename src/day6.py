from util import *
import string

rows = get_file_contents("../input/day6.txt")

ans_a = 0
group_ascii = [l for l in string.ascii_lowercase]
for i in range(len(rows)):
    if rows[i] == '':
        # reset 
        group_ascii = [l for l in string.ascii_lowercase]
    else:
        for l in rows[i]:
            if l in group_ascii:
                group_ascii.remove(l)
                ans_a += 1

print("a) " + str(ans_a))

ans_b = 0
persons_in_a_group_count= 0
ans_map = {}
for i in range(len(rows)):
    if rows[i] == '':
        # you need to identify the questions to which everyone in a group answered "yes"
        ans_b += sum(count == persons_in_a_group_count for count in ans_map.values())
        # reset
        persons_in_a_group_count= 0
        ans_map = {}
    else:
        persons_in_a_group_count += 1

        # map how many persons answers "yes" to which questions
        for l in rows[i]:
            ans_map[l] = ans_map.get(l, 0) + 1

print("b) " + str(ans_b))
