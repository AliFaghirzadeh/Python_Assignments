file = open("student.txt", 'r')
line_list = []
for line in file.readlines():
    degree = input("Enter the degree of the student : " + line)
    if line.__contains__("\n"):
        line = line.replace("\n", "")
    line_list.append(str(line + "," + degree + "\n"))
file.close()
print(line_list)
file = open("student.txt", 'w')
file.writelines(line_list)
file.close()
