from reader import reader

def writer(filename, array):
    with open(f"Database/{filename}", "w") as f:
        line = ""
        for i in range(len(array)):
            for j in range(len(array[i])):
                if j == len(array[i]) - 1:
                    line += str(array[j])
                else:
                    line += f"{array[j]};"
            print(line)
            line += "\n"
        f.write(line)

data = reader("game.csv")
add_data = ['1', 'binomo', 'action', '1990', '17000', '6']
#data.append(add_data)

writer("game.csv", data)

print(data)
#print(add_data)
#print(final_data)
#print(reader("game.csv"))