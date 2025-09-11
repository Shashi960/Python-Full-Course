#Solid Principles in Python
#1. Single Responsibility Principle (SRP)
#Homework

'''1. **SRP Practice**: Create a `Book` class that only stores details. Create another class that prints book details.'''
class Book:
    def __init__(self, id, name, author, price):
        self.id=id
        self.Name = name
        self.author = author
        self.price = price

    def __str__(self):
        return f"Id:{self.id}, Name: {self.Name}, Author Name:{self.author}, Price:{self.price}"
class library:
    def __init__(self):
        self.books={}

    def add_books(self, id, name, author, price):
        if name in  self.books.values():
            print("Book Already exists....")
            return
        self.books[id]=Book(id, name, author, price)
        print("Book Entered Successfully")

    def show_books(self):
        if not self.books:
            print("Book not found.")
            return
        
        print("======Available Books======")
        for book in self.books.values():
            print(f"{book.Name}")

lib=library()
lib.add_books(1, 'Ganeshji', 'Shashi', 210)
lib.add_books(2, 'Ram', 'Aishu', 150)
lib.add_books(3, 'Gaja', 'Varun', 150)
lib.add_books(4, 'Mera vatan', 'Raagu', 100)
lib.show_books()


'''2.OCP Practice: Build a billing system that calculates tax based on `ProductType`. Add `Food`, `Electronics`, etc., using subclasses.'''
class Tax:
    def tax(self):
        return 0

class FoodTax(Tax):
    def tax(self):
        return 2

class MedicineTax(Tax):
    def tax(self):
        return 3

class ElectonicsTax(Tax):
    def tax(self):
        return 8
    
#for 500  rs purchase can pay different tax
amt=500
food=FoodTax()
food1=food.tax()
foodtax=int((amt*food1)/100)
print(f"Your bill for Food :{amt} Tax:{foodtax} \n ==>>Total Bill:{amt+foodtax}\n============================")

med=MedicineTax()
med1=med.tax()
medtax=int((amt*med1)/100)
print(f"Your bill for Medicine :{amt} Tax:{medtax} \n ==>>Total Bill:{amt+medtax}\n============================")

ele=ElectonicsTax()
ele1=ele.tax()
eletax=int((amt*ele1)/100)
print(f"Your bill for Food :{amt} Tax:{eletax} \n ==>>Total Bill:{amt+eletax}\n============================")


'''3.LSP Practice: Write a class `Vehicle` and subclasses like `Bike`, `Boat`. Avoid breaking behavior.'''
class Vehicle:
    def move(self):
        print("Moving")

class Bike(Vehicle):
    def move(self):
        print("Running")

class Boat(Vehicle):
    def move(self):
        print("Floating")

class Airoplane(Vehicle):
    def move(self):
        print("Flying")

b=Bike()
bo=Boat()
air=Airoplane()
b.move()
bo.move()
air.move()



'''4.DIP Practice: Make a `HomeAppliance` system where high-level class `Remote` works with abstract `Appliance`, and you can pass `TV`, `AC`, etc.'''
class Homeappliance:
    def input(self):
        pass

class Tv(Homeappliance):
    def input(self):
        return "Tv is Turning On..."

class Ac(Homeappliance):
    def input(self):
        return "Ac is Turning On..."

class remote:
    def __init__(self, device: Homeappliance):
        self.device = device

    def get_input(self):
        return self.device.input()
    
c=remote(Ac())
print(c.get_input())



'''5.ISP Praactise:'''
class workable:
    def work(self):
        print("Workig")

class eatable:
    def eat(self):
        print("eating")

class human(workable,eatable):
    def eat(self):
        print("Human is Eating")

    def work(self):
        print("Human is working")
class robot(workable):
    def work(self):
        print("Robot is working")

h=human()
r=robot()
h.work()
h.eat()
r.work()
