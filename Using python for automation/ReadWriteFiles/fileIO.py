#Reading a file using with statement
#Printing people who passed
print("People who passed :)\n")
with open('inputFile.txt','r') as file:
    for line in file:
        #splitting the lines into words:
        lineSplit = line.split()
        #Evaluating grades 
        if(lineSplit[2]=='P'):
            print(line)   
#Printing people who failed
print("People who failed :/\n")
with open('inputFile.txt','r') as file:
    for line in file:
        #splitting the lines into words:
        lineSplit = line.split()
        #Evaluating grades
        if(lineSplit[2]=='F'):
            print(line)
            
