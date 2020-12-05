# advent of code
# day4

import re
keywords = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr',  'pid']
keywords.sort()
eye_color_list = ['amb', 'blu', 'brn', 'gry', 'grn' ,'hzl' ,'oth']

valid_passport_count_a = 0 
valid_passport_count_b = 0

with open("input.txt","r") as file:
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
            if i == len(entries) -1 :
                print(e)
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
                if key != 'cid':
                    value = value.rstrip('\r\n') # remove windows end of line
                    
                    if key == 'byr' and int(value) >= 1920 and int(value) <= 2002:
                            valid_value = True
                    elif (key == 'ecl') and (value in eye_color_list):
                        valid_value = True
                    elif key == 'iyr' and int(value) >= 2010 and int(value) <= 2020:
                            valid_value = True
                    elif key == 'eyr' and int(value) >= 2020 and int(value) <= 2030:
                            valid_value = True
                    elif key == 'hgt':
                        if 'cm' in value:
                            h = int(value.split('cm')[0])
                            if h >= 150 and h <= 193:
                                valid_value = True
                        elif 'in' in value:
                            h = int(value.split('in')[0])
                            if h >= 59 and h <=76:
                                valid_value = True
                    elif key == 'hcl' and re.search("^#[0-9a-f]{6}", value):
                        valid_value = True
                    elif key == 'pid' and re.search("^[0-9]{9}$", value):
                        valid_value = True

                    
                    if valid_value:
                        given_keywords.append(key)
                        debug_given_items.append(key+":"+value) # for debugging
                    
                        
        if (i < len(entries) - 1 and entries[i+1] == '\n') or i ==len(entries) -1:
            given_keywords.sort() # for debugging
            if len(given_keywords) == len(keywords):
                valid_passport_count_b += 1

                # for debugging
                debug_given_items.sort()
                print("b) " + str(valid_passport_count_b)+":"+str(debug_given_items))
                
           
            # reset
            given_keywords = []
            debug_given_items=[]
                               
                    
print("a) valid passports " + str(valid_passport_count_a))              
print("b) valid passports " + str(valid_passport_count_b))                    
    
    


