from util import *
from collections import defaultdict

rules_dict = defaultdict(lambda : [])
categories_list_length=0
my_ticket=[]


def categorize(filename):
    global rules_dict
    global categories_list_length
    global my_ticket

    lines = get_file_contents(filename, False)

    # remove empty lines
    lines=[l for l in lines if l != ''] 
    rules_processed=False
    i=0
    iterate=True
    while iterate:
        while rules_processed == False and lines[i].find("your ticket") == -1:
            # process the rules
            category,s = lines[i].split(': ')
            s1,s2=s.split(' or ')
            rules_dict[category].extend([int(s) for s in s1.split('-')])
            rules_dict[category].extend([int(s) for s in s2.split('-')])
            i+=1
        if lines[i].find("your ticket") !=-1:
            rules_processed=True
            
            i+=1
            entries=lines[i].split(',')
            my_ticket=[int(e) for e in entries]

            i+=2
            categories_list_length = len(lines[i].split(','))
            iterate=False
    
    del lines[:i]
    return lines

def is_within_limits(e, rules):
    if ((e >= rules[0] and e <= rules[1]) or
        (e >=rules[2] and e<=rules[3])):
        return True
    return False
        
def find_error(lines):
    global rules_dict
    global categories_list_length

    categories_list=[[]]*categories_list_length

    ticket_scanning_error_rate=0

    i=0
    while i < len(lines):
            entries=lines[i].split(',')
            for e_index in range(len(entries)):
                e=int(entries[e_index])
                rlist=categories_list[e_index]

                c_local_list=[]
                for r in rlist:
                    if is_within_limits(e,rules_dict[r]):
                        c_local_list.append(r)
                
                # if not found in cached categorylist then search the complete rules list
                if len(c_local_list) == 0:
                    for r,rules in rules_dict.items():
                        if is_within_limits(e,rules):
                            c_local_list.append(r)
                    
                    # if still not found, add the value to the invalid value
                    if len(c_local_list) == 0:
                        ticket_scanning_error_rate+=e
                    else:
                        categories_list[e_index]=c_local_list
                else:
                    categories_list[e_index]=list(set(rlist).intersection(c_local_list))
            i+=1
    print("a) ticket scanning error rate: ",str(ticket_scanning_error_rate))
    
def find_departures(lines):
    global rules_dict   
    global categories_list_length
    global my_ticket

    categories_list=[[]]*categories_list_length

    i=0
    while i < len(lines):
            entries=lines[i].split(',')
            entries_categories_list=[[]]*len(entries)
            ignore=False
            for e_index in range(len(entries)):
                e=int(entries[e_index])
                c_local_list=[]
                rlist=categories_list[e_index]

                for r in rlist:
                    if is_within_limits(e,rules_dict[r]):
                        c_local_list.append(r)
                
                if len(c_local_list) == 0:
                    c_local_list=[]
                    for r,rules in rules_dict.items():
                        if is_within_limits(e,rules):
                            c_local_list.append(r)

                    if len(c_local_list) == 0:
                        ignore=True
                        break
                    elif len(rlist)==0:
                        entries_categories_list[e_index]=c_local_list
                else:
                    if len(rlist) > 0:
                        entries_categories_list[e_index]=list(set(rlist).intersection(c_local_list))
                    else:
                        entries_categories_list[e_index]=c_local_list
            
            if not ignore:
                categories_list=entries_categories_list

            i+=1

    end=False
    while not end:
        for k in rules_dict:
            count=0
            final_index=0
            for c_index in range(len(categories_list)):
                if k in categories_list[c_index]:
                    count+=1
                    final_index=c_index

            if count == 1:
                categories_list[final_index]=[k]
            else:
                final_index=0
                found_single_entry=False
                for c_index in range(len(categories_list)):
                    if len(categories_list[c_index]) == 1 and categories_list[c_index][0]==k:
                        found_single_entry=True
                        final_index=c_index
                        break
                
                if found_single_entry:
                    for c_index in range(len(categories_list)):
                        if c_index != final_index:
                            # remove that category from all other category-entries in the categories list
                            if k in categories_list[c_index]:
                                categories_list[c_index].remove(k)
        
        # if all category-rows have only one entry then consider the process as done
        iterate=False
        for c_index in range(len(categories_list)):
            if len(categories_list[c_index]) != 1:
                iterate=True
        
        end=not iterate


    final=1
    for c_index in range(len(categories_list)):
        if categories_list[c_index][0].startswith('departure'):
            final *= my_ticket[c_index]
            #print(categories_list[c_index][0],my_ticket[c_index])

    print('b)',final)


#################### puzzle a #######################

lines = categorize("../input/day16.txt")

start_profiling()
find_error(lines)
end_profiling()


#################### puzzle b #######################
start_profiling()
find_departures(lines)
end_profiling()
