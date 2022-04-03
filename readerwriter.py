import standard

# Reader = csv -> matrix of data
def reader(filename: str) -> list:
    """
    Function to read a csv file and outputs a matrix of data with index [line][object]
    """
    with open(f"Database/{filename}", "r") as f:
        result = []
        for line in f:
            line = line.rstrip()                        # strip '\n'
            line_objects = []
            word_holder = ""
            for i in range(standard.length(line)):
                if line[i] == ";":
                    line_objects.append(word_holder)
                    word_holder = ""
                else:
                    word_holder += line[i]
                if i == standard.length(line)-1:
                    line_objects.append(word_holder)
                    word_holder = ""
            result.append(line_objects)
    return result

# writeline -> database filename, array of data
# tidak dipakai untuk di import
def writeline(filename: str, array: list):
    """
    Procedure to write a matrix of data into a csv file
    """
    with open(f"Database/{filename}", "w") as f:
        line = ""
        for i in range(standard.length(array)):             # Looping for every line of data
            for j in range(standard.length(array[i])):      # Looping for every item in line
                if j == standard.length(array[i]) - 1:      # If item is the last item, doesn't use ;
                    line += str(array[i][j])
                else:
                    line += f"{array[i][j]};"               # use ;
            line += "\n"                                    # end of line
        f.write(line)

# write = array -> csv
def writer(filename: str, data_add: list):
    """
    Procedure to add a data into the existing matrix of data and call the writeline procedure
    """
    data = reader(filename)
    data.append(data_add)
    writeline(filename, data)


#add_data = ['1', 'oscta', 'action', '1990', '17000', '6']
writer("game.csv", ['5', 'mario', 'adventure', '2022', '10000', '5'])
#print(reader("game.csv"))
