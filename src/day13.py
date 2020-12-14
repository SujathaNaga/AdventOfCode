from util import *


lines = get_file_contents("../input/day13-sample.txt", False)
lines = get_file_contents("../input/day13.txt", False)
bus_id = 0
min_mins = 9999999999999999

my_wait_time = int(lines[0])
line = lines[1]

entries = line.split(',')
entries = [int(x) for x in entries if x != 'x']

for e in entries:
    i = 0
    mul = int(my_wait_time / e)
    while i < my_wait_time:
        i =  mul * e
        if i >= my_wait_time:
            bus_wait_time = i - my_wait_time
            if min_mins > bus_wait_time:
                min_mins = bus_wait_time
                bus_id = e
            break
        else:
            mul += 1

print("a) " + str(bus_id * min_mins))

### puzzle b
# all the bus ids are primes and they are coprimes since the common factor between them is 1 and 1 only
# use chinese reminder theorem

entries = lines[1].split(',')
modulo_residue_dict = {}
for i in range(len(entries)):
    if entries[i].isdigit():
        # map bus id with the final_ans % bus id value
        # this is the residue if the final ans is mod with bus id.
        modulo_residue_dict[int(entries[i])] = int(entries[i]) - i

# find product of moduli (bus ids)
prod = 1
for b in modulo_residue_dict.keys():
    prod *= b

sum = 0
for k, index in modulo_residue_dict.items():
    # find the divisor
    p = int(prod/k)

    # find the modular multiplicative inverse 
    l = pow(p, -1, k)
    assert (l * p) % k == 1

    # add up    
    sum += index * pow(p, -1, k) * p

sum %= prod
print("b) " + str(sum))