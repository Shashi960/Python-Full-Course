#Day8
#Debugger And Functions
#Debugger Program
i=1
while(i<=5):
    j=1
    while(j<=i):
        print('*',end=" ")
        j+=1
    i+=1
    print("\n")


#Functions
def name(boy,girl='Rani'): #formal parameter
    print(f"Boy Name is {boy}")
    print(f"Girl Name is {girl}")
    print(f"{boy} and {girl} are friends.")

men=input("Enter a Boy name: ")
women=input("Enter a Girl name: ")
name(men,women) #actual parameter
name(men)

#Returning values
def square(num):
    a=num          #Local variable(A variable within a function is called local variable)
    return num*a
n=int(input("Enter A number: "))
b=square(n)        #Global variable(A variable Outside a function is called Global variable)
print(f"Square of {n} is {b}")
print(f"Adding 2 to Squared number is {b+2}")


#Homework
'''1.Greet Function:
Write a function `greet()` that takes no arguments and prints a greeting message.'''
def greet():
    print("Hello,Welcome TO Python World.")
greet()

'''2.Parameterized Greet:
Write a function `greet_user()` that takes a name as input and prints a custom greeting.'''
def greet(name):
    print(f"Hello {name},Welcome TO Python World.")
user=input("Enter Your Name: ")
greet(user)

'''3.Sum Function: 
Write a function `add_numbers(a, b)` that returns the sum of two numbers. 
Call this function with different values.'''
def add(a,b):
    return a+b
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
c=add(num1,num2)
print(f"Sum of Two Numbers:{c}")
print(f"Sum of Two Numbers:{add(num1,num2)}")





