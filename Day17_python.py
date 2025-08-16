#Encapsulation
class ATM:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance")
atm = ATM(1000)
ch=int(input("Welcome To SBI ATM: \n Select Following Options\n 1.Deposit \t 2.withdraw\n"))
if(ch==1):
    atm.deposit(int(input("Enter Amount You Want To Deposit: ")))
elif (ch==2):
    atm.withdraw(int(input("Enter Amount Need To Withdrawl: ")))
else:
    print("Please Select Valid Option")
#print(atm.self.balance)   #encapsulation cannot alllow balance

#Abstraction
class Car:
    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Car accelerating")

    def brake(self):
        print("Car stopping")

car = Car()
car.start_engine()  # Abstracts complex internal workings
car.accelerate()
car.brake()


#example for both
class Database:
    def __init__(self):
        self.__storage = {}

    def save_data(self, key, value):
        self.__storage[key] = value
        print(f"Data saved for {key}")

    def get_data(self, key):
        return self.__storage.get(key, "No data found")

db = Database()
db.save_data("user_101", {"name": "Raj", "age": 30})
print(db.get_data("user_101"))

#Inheritance
class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in")

class Admin(User):
    def delete_user(self, user):
        print(f"Admin {self.username} deleted user {user}")

admin = Admin("karnataka_admin")
admin.login()  # Inherited from User
admin.delete_user("user_102")


#Polymorphism
class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in")

class Admin(User):
    def delete_user(self, user):
        print(f"Admin {self.username} deleted user {user}")

admin = Admin("karnataka_admin")
admin.login()  # Inherited from User
admin.delete_user("user_102")








#Homework
'''1.Encapsulation:
   - Create a `BankAccount` class with private attributes for `account_number` and `balance`.
   - Add methods to check balance, deposit, and withdraw funds.
   - Try accessing the balance directly and observe the result.'''
class BankAccount:
    def __init__(self,AcNO,balance):
        self.__AcNO=AcNO
        self.__balance=balance
        self.__Account={}
        self.__Account[self.__AcNO]=self.__balance
    def checkbalance(self,acnno):
        if acnno in self.__Account.keys():
            print(f"Balance Left: {self.__Account[self.__AcNO]}")
        else:
            print("Invalid Acno")
    def deposit(self,acno,amount):
        if acno in self.__Account.keys():
            self.__Account[acno]+=amount
            print(f"Amount deposited {amount}. New Balance {self.__Account[acno]}")
        else:
            print("Invalid Acno")
    def withdraw(self,acno,amount):
        if acno in self.__Account.keys():
            if self.__Account[acno]>=amount:
                self.__Account[acno]-=amount
                print(f"Amount withdrawed {amount}. New Balance {self.__Account[acno]}")
            else:
                print("Insufficient Amount:")
        else:
            print("Invalid Acno")
        
bank=BankAccount(2238,10000)
bank.checkbalance(2238)
bank.deposit(2238,1000)
bank.withdraw(2638,12000)
#print(bank.__Account)  #cannot directly accessible



'''2. **Abstraction**:
   - Design a `Phone` class with methods to `call_contact` and `take_picture`. Abstract away any internal processing details and focus on creating a user-friendly interface.'''
class Phone:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.contacts = {}  # store contacts as {name: number}
    
    def add_contact(self, name, number):
        """Add a contact to the phonebook."""
        self.contacts[name] = number
        print(f"Contact saved: {name} - {number}")

    def call_contact(self, name):
        """Call a saved contact by name."""
        if name in self.contacts:
            print(f"Calling {name} at {self.contacts[name]}...")
        else:
            print(f"Contact '{name}' not found!")

    def take_picture(self):
        """Simulate taking a picture."""
        print(" Picture taken and saved to gallery!")

my_phone = Phone("Arjun")
my_phone.add_contact("Mom", "9876543210")
my_phone.add_contact("Best Friend", "9123456789")

my_phone.call_contact("Mom")
my_phone.take_picture()


'''3.Inheritance**:
   - Create a base class `Vehicle` with a `start` method. Then create a subclass `Bike` with an additional `ride()` method.
   - Demonstrate how the `Bike` can use both `start` and `ride`.'''
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Bike(Vehicle):
    def ride(self):
        print("Bike is being ridden!")
my_bike = Bike()
my_bike.start()  
my_bike.ride()  

'''4.Polymorphism:
   - Implement a `Shape` class and derive `Circle` and `Rectangle` classes with a method `calculate_area`. Each class should calculate area differently based on its shape.
   - Create a loop to calculate areas for both `Circle` and `Rectangle` objects.'''
import math
class Shape:
    def calculate_area(self):
        pass 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

shapes = [
    Circle(5),
    Rectangle(4, 6)
]

for shape in shapes:
    area = shape.calculate_area()
    print(f"Area: {area:.2f}")
