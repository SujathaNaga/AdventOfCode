def get_sanitized_file_contents(filename):
    rows = []
    with open(filename,"r") as file:
        for line in file:
            rows.append(line.rstrip()) # remove trailing newline whitespaces etc
    return rows
