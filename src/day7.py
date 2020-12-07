from util import *
from collections import defaultdict

# 226 right answer
# 9569


#rows = get_file_contents("../input/day7-sample.txt")
rows = get_file_contents("../input/day7.txt")

inner_to_outer_map = defaultdict(lambda : [])
my_bag_name = 'shiny gold'
unique_bag_list =[]

def find_unique_outer_bags(innerbag):
    global unique_bag_list
    outer_bag_list = inner_to_outer_map.get(innerbag)
    if outer_bag_list:
        for outer in outer_bag_list:
            if outer not in unique_bag_list:
                unique_bag_list.append(outer)
            find_unique_outer_bags(outer)

for row in rows:
    if row == '':
        continue

    outer, contains = row.split('contain ')
    outer = outer.replace(' bags ', '')
    inner_bags = contains.split(', ')
    for inner_bag in inner_bags:
        # remove dot at the end
        inner_bag = inner_bag.replace('.','')
        # remove bags/bag string for clarity
        inner_bag = inner_bag.replace(' bags','')
        inner_bag = inner_bag.replace(' bag','')

        # split string
        i_list = inner_bag.split(' ')
        inner_bag = ' '.join(i_list[1:3])
        inner_to_outer_map[inner_bag].append(outer)

find_unique_outer_bags(my_bag_name)
print("a) " + str(len(unique_bag_list)))
        
######################################
# puzzle b
outer_to_inner_map = defaultdict(lambda: defaultdict(lambda: 0))

def find_total_count(outer):
    inner_bags = outer_to_inner_map.get(outer)
    local_ans_a = 0 
    if inner_bags:
        for bag, count in inner_bags.items():
            ans = find_total_count(bag)
            if ans != 0:
                local_ans_a += (count * find_total_count(bag)) # the bags that are inside this outer bag should be calculated
            
            local_ans_a += count # add the bag count also
        return local_ans_a
    else:
        return 0

for row in rows:
    if row == '':
        continue

    outer, contains = row.split('contain ')
    outer = outer.replace(' bags ', '')
    inner_bags = contains.split(', ')
    for inner_bag in inner_bags:
        # remove dot at the end
        inner_bag = inner_bag.replace('.','')
        # remove bags/bag string for clarity
        inner_bag = inner_bag.replace(' bags','')
        inner_bag = inner_bag.replace(' bag','')

        # split string
        i_list = inner_bag.split(' ')
        inner_bag = ' '.join(i_list[1:3])

        # get number of bags
        value = 0
        if i_list[0] != 'no':
            value = int(i_list[0])

        # add to map
        outer_to_inner_map[outer][inner_bag] += int(value)

print("b) " + str(find_total_count(my_bag_name)))