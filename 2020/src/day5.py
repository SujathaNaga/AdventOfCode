# advent of code
# day 5

import re

highest_seat_id_a = 0

def find_index(text, max_value, upper_half_string, lower_half_string):
    start_index = 0 
    end_index = max_value - 1

    # find the single entry index based on string with a pattern
    for r in text:
        max_value = max_value/2
        if r == upper_half_string:
            end_index = start_index + max_value - 1
        elif r == lower_half_string:
            start_index = end_index - max_value + 1
    return end_index

list_of_seat_ids = []
with open("../input/day5.txt","r") as file:
    entries = file.readlines()

    # first puzzle
    for i in range(0, len(entries)):
        e = entries[i]
        row_string = e[:7]
        seat_id = find_index(e[:7], 128, 'F', 'B') * 8 + find_index(e[7:], 8, 'L', 'R')
        list_of_seat_ids.append(seat_id)        
        highest_seat_id_a = int(seat_id) if seat_id > highest_seat_id_a else highest_seat_id_a
    
print("a) seat id " + str(int(highest_seat_id_a)))
# find your seat id which is missing from the input file
print("b) " + str([id for id in range(10, highest_seat_id_a) if id not in list_of_seat_ids]))          
    
    


