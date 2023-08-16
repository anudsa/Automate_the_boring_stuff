# Reading the file and storing data in a list
with open('./inputFile.txt','r') as files:
    data=files.readlines()

with open('newTestFile.txt', 'w') as file:
    file.write("This will create a new file.\n")
    file.write("Full list of students: \n")
    for i in range(0,len(data)):
        file.write(data[i])

    file.write("\nStudents who passed: \n")
    for line in data:
        if 'P' in line:
            file.write(line) 

    file.write("Students who failed: \n")
    for line in data:
        if 'F' in line: 
            file.write(line)


