def get_file_contents(filename):
    rows = []
    with open(filename,"r") as file:
        for line in file:
            rows.append(line.rstrip()) # remove trailing newline whitespaces etc
    
    # add empty last line so that all the entries will be processed properly
    rows.append('')
    return rows
