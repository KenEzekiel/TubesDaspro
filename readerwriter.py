from standard import *

# Reader = csv -> matrix of data
def reader(filename):
    with open(f"Database/{filename}", "r") as f:
        result = []
        for line in f:
            line = line.rstrip()                        # strip '\n'
            #print(line)
            line_objects = []
            word_holder = ""
            for i in range(length(line)):
                if line[i] == ";":
                    line_objects.append(word_holder)
                    word_holder = ""
                else:
                    word_holder += line[i]
                if i == length(line)-1:
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
        for i in range(length(array)):             # Looping for every line of data
            for j in range(length(array[i])):      # Looping for every item in line
                if j == length(array[i]) - 1:      # If item is the last item, doesn't use ;
                    line += str(array[i][j])
                else:
                    line += f"{array[i][j]};"   # use ;
            line += "\n"                        # end of line
        f.write(line)

# write = array -> csv
def writer(filename, data_add):
    data = reader(filename)
    data.append(data_add)
    writeline(filename, data)

    #print(data)

#add_data = ['1', 'oscta', 'action', '1990', '17000', '6']
writer("game.csv", ['5', 'mario', 'adventure', '2022', '10000', '5'])
#print(reader("game.csv"))

# csv -> array of array (reader)

# modifikasi array nya (bisa per indeks)
# game = reader("game.csv")
# game[1][0] = 3
# 3;binomo;action;1990;17000;6

# array of array -> csv