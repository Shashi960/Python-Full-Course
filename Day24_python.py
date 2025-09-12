import my_Library.greeting
import my_Library.My_package2.menu
import my_Library.My_pacakage1.Orders

my_Library.greeting.welcome('Naman')

cart=[]
print("==:Foods Available:==")
c=my_Library.My_package2.menu.items()
for item in c:
    print(item.upper(),end=",  ")
print("\n")
try:
    n=int(input("How many items You want to order?:"))
except ValueError:
    print("Enter Number Not Item !!")
    n=int(input("How many items You want to order?:"))
finally:
    print("===:Enter Items:===")
if n>0:
    for i in range(0,n):
        item = input("which You want To order ?:")
        if item.lower() in c:
            cart.append(item.upper())
        else:
            ask=input(f"{item} not avilable. Can you order another item that available(Yes/No)")
            if  (ask == 'Yes' or ask == 'yes' or ask == 'y' or ask =='Y'):
                item = input("which You want To order ?:")
                if item.lower() in c:
                    cart.append(item.upper())
            else:
                  print("Ok Item Not Available right Now!!")
    my_Library.My_pacakage1.Orders.Cart(cart)        
    my_Library.greeting.goodbye('Naman')
else:
    my_Library.greeting.bye('Naman')


#Homework
'''1.Create Your Module
   * Write a file `calculations.py` with functions: `add()`, `subtract()`, `multiply()`
   * Use it in another file by importing and testing all functions.'''
import calculation.calculations as cal

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition value: ",cal.add(a,b))
print("Subtraction value: ",cal.subtract(a,b))
print("Multiplication value: ",cal.multi(a,b))


'''2.Random Name Selector
   * Use the `random` module to pick a winner from a list of names.'''
import random as rd

names=['hari','manu','kunit','raagu']
print(rd.choice(names))



'''3.Math Helper
   * Use the `math` module to:

     * Find square root of 81
     * Get factorial of 6
     * Get `pi` value and multiply by 2'''

import math as m
print("Squareroot of 81 is:",m.sqrt(81))
print("Factorial Of 6 is:",m.factorial(6))
print('Double of PI value:',m.pi*2)



'''4. **Organize Code in a Package**
* Create a package called `library` with two modules:

     * `books.py` (function: `list_books()`)
     * `members.py` (function: `list_members()`)
   * Import and use both in a main file.'''

from Library import books, members

print("Books in Library:", books.list_books())
print("Library Members:", members.list_members())
