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

