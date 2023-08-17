import os
from pathlib import Path
#Dictionary that maps file extensions to certain folders
subdirectories = {
    "Documents": ['.pdf','.txt'],
    "Audio": ['.m4a','.mp3'],
    "Videos": ['.mov','.mp4'],
    "Images": ['.jpg','.jpeg']
}

#Printing keys
print("Keys:\n")
for keys in subdirectories:
    print(keys)

#Printing Key value pairs
print("\nKey value pairs: \n")
for keys, values in subdirectories.items():
    print(keys,values)

#A function to determine the directory based on the actual file extension
def findDirectory(extension):
    #loop that iterates throuh all key value pairs
    for keys, values in subdirectories.items():
        #loop that iterates all values
        for value in values:
                #if statement that compares the value with the given extension
                if value == extension:
                    #The current folder is then returned
                    return keys

print("\nTESTING 2nd FUNCTION\n")

#find extension of each file in the given directory
def findExtension():
    #loop that iterates all files and folders in the path given
    for entries in os.scandir():
        #skips the code if it's a directory
        if entries.is_dir():
            continue
        #variable that stores the extension of the file by slicing the name string and makes it lowercase
        fileExtension= entries.name[(entries.name.rfind('.')):].lower()
        print(fileExtension)
        #variable that stores the current path of the file
        filePath=Path(entries)
        print(filePath)
        #variable that stores the name of the directory the file belongs to
        directory=findDirectory(fileExtension)
        print(directory)
        #if statement that evaluates if the file must be moved or not
        if (directory!= None):
            #a path object for the directory is created
            directoryPath = Path(directory)
            #Statement that finds if the directory exists or not
            if(directoryPath.is_dir() == False):
                print("create directory")
                directoryPath.mkdir()
            #File is moved to the directory (either recently created or older)
            filePath.rename(directoryPath.joinpath(filePath))
            print("move file\n")
        else:
            print("File does not need to be moved\n")

findExtension()
