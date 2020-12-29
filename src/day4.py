# advent of code
# day4

import re
keywords = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr',  'pid']
keywords.sort()

valid_passport_count_a = 0 
valid_passport_count_b = 0

with open("../input/day4.txt","r") as file:
    entries = file.readlines()

    # first puzzle
    given_keywords = []
    for i in range(0, len(entries)):
        e = entries[i]
        if e == '\n' or i == len(entries) - 1:
            given_keywords.sort() # for debugging
            if len(given_keywords) == len(keywords):
                valid_passport_count_a += 1

            # reset
            given_keywords = []
            
        else:
            items = e.split(' ')
            for i in items:
                key, value = i.split(':')
                if key != 'cid':
                    given_keywords.append(key)



    # second puzzle
    given_keywords = []
    debug_given_items=[]
    for i in range(0, len(entries)):
        e = entries[i]
        if e != '\n':
            items = e.split(' ')
            for item in items:
                key, value = item.split(':')
                
                # whether the key's value is valid or not
                valid_value = False 
                
                value = value.rstrip('\r\n') # remove windows end of line
                    
                if key == 'byr' :
                        valid_value =  1920 <= int(value) <= 2002
                elif (key == 'ecl'):
                    valid_value = value in  ['amb', 'blu', 'brn', 'gry', 'grn' ,'hzl' ,'oth']
                elif key == 'iyr':
                        valid_value =  2010 <= int(value) <= 2020
                elif key == 'eyr':
                        valid_value = 2020 <= int(value) <= 2030
                elif key == 'hgt':
                    if 'cm' in value:
                            valid_value = 150 <= int(value.split('cm')[0]) <= 193
                    elif 'in' in value:
                        valid_value = 59 <= int(value.split('in')[0]) <= 76
                elif key == 'hcl' :
                    valid_value = re.search("^#[0-9a-f]{6}", value)
                elif key == 'pid' :
                    valid_value = re.search("^[0-9]{9}$", value)             
                    
                if valid_value:
                    given_keywords.append(key)
                    debug_given_items.append(key+":"+value) # for debugging
                    
                        
        if (i < len(entries) - 1 and entries[i+1] == '\n') or i ==len(entries) -1:
            given_keywords.sort() # for debugging
            if len(given_keywords) == len(keywords):
                valid_passport_count_b += 1

                # for debugging
                debug_given_items.sort()
                #print("b) " + str(valid_passport_count_b)+":"+str(debug_given_items))
                
            # reset
            given_keywords = []
            debug_given_items=[]
                               
                    
print("a) valid passports ", valid_passport_count_a+1)
print("b) valid passports ",valid_passport_count_b)          
    
    


