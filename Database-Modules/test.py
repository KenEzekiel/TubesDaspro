from reader import *

line = "abc;cde;efg;"
# end with ;, no space
# Jika ada space di database, tambahkan .rstrip atau .lstrip
line_objects = []
word_holder = ""
for i in range(len(line)):
    if line[i] == ";":
        line_objects.append(word_holder)
        word_holder = ""
    else:
        word_holder += line[i]
print(line_objects)

array = [[2, "binomo", 1500],[3, "octafx", 5000]]
with open(f"Database/test.csv", "w") as f:
        line = ""
        for i in range(len(array)):
            for j in range(len(array[i])):
                if j == len(array[i]) - 1:
                    line += str(array[j])
                else:
                    line += f"{array[j]};"
            
        f.write(line)