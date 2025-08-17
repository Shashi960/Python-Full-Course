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
b=BankAccount(10000)
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
        - Exit.

    3. **Educational System**:
    - Write a program with options to:
        - Add student details.
        - Display student details.
        - Exit'''