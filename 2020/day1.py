class BreakOut(Exception): pass

entries = []

try:
    for i in range(0, len(entries)):
        for j in range(i+1, len(entries)):
            if int(entries[i]) + int(entries[j])== 2020:
                print('a)', int(entries[i])*int(entries[j]))
                raise BreakOut
except BreakOut:
    pass

try:
    for i in range(0, len(entries)):
        for j in range(i+1, len(entries)):
            for k in range(j+1, len(entries)):
                if int(entries[i]) + int(entries[j]) + int(entries[k]) == 2020:
                    print('b)',int(entries[i]) * int(entries[j]) * int(entries[k]))
                    raise BreakOut
except BreakOut:
    pass
