def writer(filename, array):
    with open(f"Database/{filename}", "w") as f:
        line = ""
        for i in range(len(array)):
            if i == len(array) - 1:
                line += str(array[i])
            else:
                line += f"{array[i]};"

writer("game.csv",['1', 'binomo', 'action', '1990', '17000', '4'])