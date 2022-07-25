# create a class
class BankAccount:
    pass


account = BankAccount()  ##account is instance of BankAccount

##check the instance's type
print(type(account))


# this means check the type of account having BankAccount as a Class

##initializer/constructor
# special method that is called by default once you create an object/instance of a class

# Parent Class
class Shape:
    def __int__(self):
        self.color = 'black'
    def get_color(self):
        return self.color

# Child Class
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 10

    def get_radius(self):
        return self.radius
# Create an instance from Circle class
c1 = Circle()

print('radius of circle c1:', c1.get_radius())
print('color of circle c1:', c1.get_color())

#Polymorphism - Overwrite attribute or method overriding
# Parent Class
class Shape:
    color = 'black'

# Child Class
class Rectangle(Shape):
    pass

# Child Class
class Circle(Shape):
    color ='blue'
S1 = Rectangle()

print('color of rectangle S1:', S1.color) # this will run black because rectangle inherited from Shape
S2 = Circle()
print('color of circle S2:', S2.color) # this will run blue because inherited overwrite by circle

#Special / Magic / Dunder Methods
# 1. init method

class BankAccount:
    ## class attribute
    bankAccountType = 'Saving Account'

    # inintializer / constructor
    def __init__(self, owner, amount = 0):
        ## instance attribute
    self.owner = owner
    self.amount = amount

## create an instance of BankAccount class
account1 = BankAccount('Aketana')

print (account1.owner)
print (account1.amount)

## 2. str method
class BankAccount:
    ## class attribute
    bankAccountType = 'Saving Account'

    # inintializer / constructor
    def __init__(self, owner, amount = 0):
        ## instance attribute
    self.owner = owner
    self.amount = amount

    # string representation method
    def __str__(self):
        return 'The account of user {} has {} Baht in total'.format(self.owner, self.amount)

#cretea an instance of BankAccount class
account1 = BankAccount('Peter')
str(account)
