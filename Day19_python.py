#Menu Driven Programing
def add(a,b):
    print(f"Result: {a+b}")
def sub(a,b):
    print(f"Result: {a-b}")
def mul(a,b):
    print(f"Result: {a*b}")
def div(a,b):
    print(f"Result: {a/b}")
def display_menu():
     print("Simple Calculator")
     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")

while True:
    display_menu()
    ch=int(input("Enter Your Choice: "))
    if ch in [1,2,3,4]:
        a=int(input("Enter First Number: "))
        b=int(input("Enter First Number: "))
    if ch==1:
        add(a,b)
    elif ch==2:
        sub(a,b)
    elif ch==3:
        mul(a,b)
    elif ch==4:
        div(a,b)
    elif ch==5:
        break
    else:
        print("Select a valid Choice !")


'''Homework
1.Banking System:
Write a menu-driven program to simulate a basic banking system with options like:
   - Check Balance
   - Deposit Money
   - Withdraw Money
   - Exit'''
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
    def display_menu(self):
        print("SBI")
        print(f"1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit'''")

while True:
    b.display_menu()
    ch=int(input("Enter Your Choice: "))
    if ch==1:
        b.get_balance()
    elif ch==2:
        amount=int(input("Enter Amount need to Deposit: "))
        b.set_balance(amount)
    elif ch==3:
        amount=int(input("Enter Amount need to Withdraw: "))
        b.out_balance(amount)
    elif ch==4:
        break
    else:
        print("Select a valid choice!")


'''2. **Grocery Store Menu**:
    - Create a program where users can:
        - Add items to their cart.
        - Remove items.
        - View the total price.
        - Exit.'''
cart = {}  
def add_item():
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    cart[item] = cart.get(item, 0) + price
    print(f"\n {item} added to cart!\n")

def remove_item():
    item = input("Enter item name to remove: ")
    if item in cart:
        del cart[item]
        print(f"\n {item} removed from cart!\n")
    else:
        print("\n Item not found in cart!\n")

def view_total():
    if not cart:
        print("\n Your cart is empty!\n")
        return
    total = sum(cart.values())
    print("\n Items in your cart:")
    for item, price in cart.items():
        print(f"- {item}: ₹{price}")
    print(f"\n Total Price = ₹{total}\n")

def menu():
    while True:
        print("=== Grocery Store Menu ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Total Price")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_total()
        elif choice == '4':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice! Please enter 1-4.\n")


menu()



'''3. **Educational System**:
    - Write a program with options to:
        - Add student details.
        - Display student details.
        - Exit'''

students = [] 
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    
    student = {"Name": name, "Roll": roll, "Course": course}
    students.append(student)
    print("\nStudent added successfully!\n")

def display_students():
    if not students:
        print("\n No student records found!\n")
        return
    
    print("\nStudent Details:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['Name']}, Roll: {student['Roll']}, Course: {student['Course']}")
    print()

def menu():
    while True:
        print("=== Educational System Menu ===")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print(" Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.\n")
menu()
