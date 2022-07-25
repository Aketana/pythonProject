#without arguments
def greeting(): #no argument
    print("Hello, Good Morning!")

#with arguments
def greeting(name, day):
    print("Hello", name, "!", "Have a nice", day)

#return value

def tempConversion(celsiusTemp):
    fahrenhietTemp = (celsiusTemp*9/5)÷32
    return fahrenhietTemp

convertTemp = tempConversion(30) ##การเรียกใช้ tempconversion โดยนำค่าที่ได้ไป *9/5÷32
print(convertTemp)

#Global Veriable - means the code is available every part of the code
# define a to global
a = 1
def funcl():
    print('Inside funcl() a =', a)

def func2():
    a = 2
    print('Inside funcl2() a =', a) #still 1 because a = 1 on first function, not globally

def func3():
    global a #force a to be always 3
    a = 3
    print('Inside funcl3() a =', a)

#Global Scope
print ('global a =', a)
funcl1()
print ('global a =', a)
funcl2()
print ('global a =', a)
funcl3()
print ('global a =', a)

#Normal Function vs Lambda Function
def square(y):
    return y*y

print(square(5))

square = lambda y: y*y #same row
print(square(5))

#Lambda function with map()
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_list = map(lambda x: x*x, num_list) #map lambda is using value x*x by itself
print(list(square_list))

#print 1, 4, 9, 16, 25, 36, 49, 64, 81, 100


#Lambda function with filter()
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num_list = filter(lambda x:(x%2 == 0), num_list) #หาเลขที่หาร 2 ลงตัวให้แสดงผลออกมาทาง Print
print(list(even_num_list))

#print 2, 4, 6, 8, 10
