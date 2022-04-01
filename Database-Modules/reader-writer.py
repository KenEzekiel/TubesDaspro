def reader(filename):
    with open(f"Database/{filename}", "r") as f:
        result = []
        for line in f:
            line = line.rstrip()  # strip '\n'
            print(line)
            line_objects = []
            word_holder = ""
            for i in range(len(line)):
                if line[i] == ";":
                    line_objects.append(word_holder)
                    word_holder = ""
                else:
                    word_holder += line[i]
                if i == len(line)-1:
                    line_objects.append(word_holder)
                    word_holder = ""
            result.append(line_objects)

            #line_objects.append([line.replace('"','')])

    return result

#print(reader("test.csv"))

# writeline -> database filename, array of data
def writeline(filename, array):
    with open(f"Database/{filename}", "w") as f:
        line = ""
        for i in range(len(array)):
            for j in range(len(array[i])):
                if j == len(array[i]) - 1:
                    line += str(array[i][j])
                else:
                    line += f"{array[i][j]};"
            line += "\n"
        f.write(line)

def writer(filename, data_add):
    data = reader(filename)
    #add_data = ['1', 'oscta', 'action', '1990', '17000', '6']
    data.append(data_add)

    writeline(filename, data)

    print(data)
#print(add_data)
#print(final_data)
#print(reader("game.csv"))

writer("game.csv", ['2', 'hai', 'action', '1990', '17000', '6'])