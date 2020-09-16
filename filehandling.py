file = open("File1", "r")
#print(file.readlines())
for lines in file:
    print(lines)
file.close()
