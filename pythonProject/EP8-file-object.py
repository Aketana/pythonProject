#open file from the computer
myFile = open("myFile", "r")
myFile = open("C:\Users\peter\Desktop\Peter\backup\PycharmProjects\pythonProject\myFile.txt", r)

#Hello, world! Welcome to Python!
#Believe me, Python is fun and easy!
#Let's Learn Python

#read file through read funciton
myFile = open("myFile", "r")
print =(myFile.read())

myFile = open("myFile", "r")
print =(myFile.read(5))

#read file through readline funciton
myFile = open("myFile", "r")
print(myFile.readline())
#read file through readline funciton show first 20 on the line
myFile = open("myFile", "r")
print(myFile.readline(20))
#read all and become a only line for the code
myFile = open("myFile", "r")
print(myFile.readlines())

#read line by line using while loop // read till there is no more line
myFile = open("myFile.txt", "r")
line = myFile.readline()
while line:
    print(line)
    line = myFile.readline()
myFile.close()

#read line by using with statement
with open('myFile.txt', 'r') as t_file:
    for line in t_file:
        print(line)

#write to a file, remember to close file all the time or it won't overwrite
myFile = open ("myFile.txt", "w")
myFile.write('Today, we learn how to handle file:\n')
myFile.close()

#Hello, world! Welcome to Python!
#Believe me, Python is fun and easy!
#Let's Learn Pythohn

## all the line will change to today, we learn how to handle file

#create new file and write text in it
myFile = open('newFile.txt', 'w')
myFile.write('Hello World!')
myFile.close()

#writeline function
myFile = open ("myFile.txt", "w")
nameList = ['Alice\n', 'Barbie\n', 'Candy\n', 'Daisy\n']
myFile.writelines(nameList)
myFile.close()

#adding to a file, like update more value instead of overwrite
myFile = open ("myFile.txt", "a")
nameList = ["Elizabeth\n", "Franky\n", "George\n", "Harry\n"]
myFile.writelines(nameList)
myFile.close()
