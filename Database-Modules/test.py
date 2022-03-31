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