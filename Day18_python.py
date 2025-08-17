#getter and setter
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        if isinstance(age,int):
            self.__age=age
        else:
            print("Age Should Be An Integer: ")
s=Student("Shashi",21)
s.set_age("20")
print(s.get_age())
print(s.get_name())


#Method Overloading
#Python Does not  Support Method Overloading Directly We can achieve it through default value for the arguement
class Math:
    def add(self,a,b,c=0):
        print(a+b+c)
c=Math()
c.add(2,4)
c.add(2,4,6)

#Method Overriding
class Animal:
    def make_sound(self):
        print("Animal Make Sound")
class Dog(Animal):
    def make_sound(self):
        print("Bark")

d=Dog()
d.make_sound()

#super() ex1
class Animal:
    def make_sound(self):
        print("Animal Make Sound")
class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Bark")

d=Dog()
d.make_sound()

#super() ex2
class Animal:
    def make_sound(self):
        print("Animal Make Sound")

class Dog(Animal):
    def make_sound(self,name):
        super().make_sound()
        print(f"{name} is Barking")

    def get_angry(self):
        super().make_sound()
        self.make_sound()

d=Dog()
d.make_sound()


#Abstract Method
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract base class
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method with no implementation

class Bike(Vehicle):
    def __init__(self,name):
        self.name=name
    def start_engine(self):
        print("Car engine started")

# Usage
bike = Bike()
bike.name
bike.start_engine()

'''6. Homewor:
1.Getters and Setters:
   - Create a class `BankAccount` with a private attribute `balance`.
   - Write a getter method to retrieve the balance and a setter method to update it, ensuring the balance never goes below zero.''' 
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        print(f"Available Balance :{self.__balance}")
    def set_balance(self,balance):
        self.__balance+=balance
        print(f"Amount {balance} Added to account successfully")
        print(f"Available Balance :{self.__balance}")
    def out_balance(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Amount Debited {amount}")
            print(f"Available Balance :{self.__balance}")
        else:
            print("Insufficient Amount to Withdraw")

b=BankAccount(10000)
b.get_balance()
b.set_balance(1000)
b.out_balance(6000)

'''2.Method Overloading:
   - Write a class `Calculator` with a method `multiply()`. Allow it to take either two or three arguments to multiply two or three numbers.'''
class Calculator:
    def multiply(self,a,b,c=1):
        print(f"multiplicationn of given numbers:{a*b*c}")

c=Calculator()
c.multiply(10,2)
c.multiply(10,2,5)

'''3.Method Overriding:
   - Create a parent class `Shape` with a method `draw()` that prints "Drawing shape".
   - Create a child class `Circle` that overrides `draw()` to print "Drawing circle".'''
class Shape:
    def draw(self):
        print("Drawing Shape")
class Circle(Shape):
        def draw(self):
            #super().draw()
            print("Drawing Circle")

c=Circle()
c.draw()

'''4. **Abstract Classes**:
   - Define an abstract class `Employee` with an abstract method `calculate_salary()`.
   - Create a subclass `Manager` that implements `calculate_salary()` based on working hours and rate per hour.'''
from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(Employee):
    def __init__(self, working_hours, rate_per_hour):
        self.working_hours = working_hours
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.working_hours * self.rate_per_hour

manager1 = Manager(working_hours=160, rate_per_hour=500) 
print("Manager Salary:", manager1.calculate_salary())
