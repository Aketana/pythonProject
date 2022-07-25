#module is python file and it is being used to refer to another python file
#dir(ModuleName) by check Class and syntax


Allgood

import sys
dir(sys)

#import statement - import all
import random
a = random.randint(1, 10)
print(a)

#from statement - import some of variety only
from random import randint, choice
a = randint(1, 10)
list1 = [1, 2, 3, 4, 5]
b = choice(list1)
print(b)

#universal import
from random import *
a = randint(1, 10)
list1 = [1, 2, 3, 4, 5]
b = choice(list1)
print(b)

#change module name
import random as rdom
a = rdom.randint(1, 10)
print(a)

from random import randint as rint
a = rint(1, 10)
print(a)

#Module: sys
import sys
while True:
    answer = input ('would you like to quit the program(yes/no)')
    if answer.lower() == 'yes':
        sys.exit()

#randint(x ,y)
import random
print (random.randint(1, 10))

#choice(list)
myList = ['orange', 109, Fale, 10.52, 'blue', 'pink']
print(random.choice(myList))

#random by range - randrange(x, y, step)
print(random.randrange(0, 100, 10)) # แรนด้อมตัวที่มีค่า = 10

#ceil(x)
import math
print('Ceiling value of 24.11 is', math.ceil(24.11))

#floor(x)
print('Floor value of 24.11 is', math.floor(24.11))

#sqrt(x)
print('Square root value of 100 is', math.sqrt(100))

#fabs(x)
print ('Absolute value of -12.50 is', math.fabs(-12.50))

import calculate
weight = int(input('What is your weight(kg): '))
height = int(input('What is your height(cm): '))
print('Your BMI is: ', int(calculate.calculateBMI(weight, height)))
