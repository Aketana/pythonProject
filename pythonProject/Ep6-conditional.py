#Conditional Statement

#Get input from users then print by if conditional
num_list = {10, 20, 30, 40, 50}
guess = eval(input('Guess a number: '))
if guess in num_list:
    print('your guess is right !')
print ('you can get prize only when your guess is right')

#If else, if you input correct numlist =  you get guess right, otherwise it will go wrong
num_list = {10, 20, 30, 40, 50}
guess = eval(input('Guess a number: '))
if guess in num_list:
    print('your guess is right !')
else:
    print('your guess is wrong !')
print ('you can get prize only when your guess is right')

#if-elif-else + nested if statement
firstPrize_num_list = {10, 20, 30, 40, 50}
secondPrize_num_list = {60, 70, 80 ,90 ,100}
guess = eval(input('Guess a number: '))
if guess < 100:
    if guess in firstPrize_num_list:
        print("you win our first price")
    elif guess in secondPrize_num_list:
        print("you win our second price")
    else:
        print("Sorry you are wrong")
elif guess > 100:
    print("out of range")
else:
    print("Sorry you are wrong")
print ('you can get prize only when your guess is right')

#for loop with range function
for i in range (5):
    print('*' * (i+1))
# will print 5 time and will keep add * more *, **, ***, ****, *****

#loop with list/tuple
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in weekday
    print("It's", day, '!')

#loop with String
for letter in "python":
    print(letter)
#will print each row p y t h o n

#while loop
user_input = ''
while user_input != 'unlock':
    user_input = input (('What is the password?: '))
print('Yes, the password is ' + user_input '. You may enter.')

#while loop - if day = satuday, will not print the rest of the value
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in weekday
    if day == 'Saturday':
        break
    print(day, 'is a weekday.')
print('These are all weekdays:')

#infinite loop till cancel or break
user_input = ''#nothing
while True:
    user_input = input(('What is the password?: ')) #get input from users
    if user_input == 'unlock':
        break
print('Yes, the password is ' + user_input '. You may enter.')

#ep 6 20 mins please read more

#continue statement
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in weekday:
    if day == 'Saturday': ##value = Saturday
        continue #skip instead of print
    print('Today is: ', day '!')
print('What day is missing?!')

#pass statement
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
    for i in weekday:
        pass
    for day in weekend:
        print("today is ", day, '!')

