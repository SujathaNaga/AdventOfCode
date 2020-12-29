final_valid_count_a = 0
final_valid_count_b = 0

with open("../input/day2.txt","r") as file:
    entries = file.readlines()
    
    for e in entries:
        items = e.split(' ')
        min_value,max_value = items[0].split('-')
        letter = items[1][0]
        password = items[2]

        # first puzzle
        # the letter should be present between min and max times in the password string
        count = 0
        for p in password:
            if p == letter:
                count +=1

        if count >= int(min_value) and count <= int(max_value):
            final_valid_count_a += 1

        # second puzzle
        # the letter should be present either in pos1 of the password or pos2 of the password
        # with index starting from 1
        pos1,pos2 = items[0].split('-')
        pos1 = int(pos1)
        pos2 = int(pos2)
        if password[pos1-1] == letter:
            if password[pos2-1] != letter:
                final_valid_count_b += 1
        elif password[pos2-1] == letter:
            final_valid_count_b += 1
        

    print("a)", final_valid_count_a)
    print("b)", final_valid_count_b)
    
    


