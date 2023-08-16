# Reading the file and storing data in a list
with open('./inputFile.txt','r') as files:
    data=files.readlines()

print("\nPrinting data stored in the list: \n")
for line in data:
        print(line)
        
print("\nPrinting people who passed: \n")
for line in data:
    if 'P' in line: 
        print(line)

print("Printing people who failed: \n")
for line in data:
    if 'F' in line: 
        print(line)
