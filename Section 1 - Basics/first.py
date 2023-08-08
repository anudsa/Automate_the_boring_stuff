#This program says hello and asks for name, then age.

print('Hello!')
print("What is your name?")
myName= input()
print("Hello there " + myName) #asks for name
print("The legnth of your name is " + str(int(len(myName))))
print("What is your age tho?") #asks for age
myAge= input()
print("You will be " + str(int(myAge)+1) + " in a year.")