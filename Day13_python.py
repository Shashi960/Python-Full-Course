#Day  8
#variable Length arguements(*args)&(**kwargs)
def sum(*args):
    sum=0
    for i in  args:
        sum+=i
    return sum
total=sum(1,2,3,4)
print(f"Sum of Given Number: {total} ")


#(**args)
def info(**detail):
    for index,value in detail.items():
        print(f"{index}:{value}")
info(name='Shashi',marks='98',Grade="A")


#Lamda
'''It takes one or more arguemwnts but only one expression'''
x=lambda a,b:a+b
print(x(10,20))

#uses
student=[{'name':'Shashi','Age':'22','course':'BCA','marks':97},
         {'name':'Kumar','Age':'21','course':'Bcom','marks':78},
         {'name':'Ramesh','Age':'21','course':'BCA','marks':87}
]
student.sort(key=lambda x:x['marks'])
print(student)

#Recursion
def fact(n):
    f=1
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
num=int(input("Enter a number:"))
print(f"factorial of {num} is {fact(num)}")

#nested functioin
def calculator(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    def div():
        print(a/b)
    add()
    sub()
    mul()
    div()
calculator(10,2)



#Homework
'''1.Lambda Function:
Write a lambda function that multiplies two numbers.'''
x=lambda a,b:a*b
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print(f"multiplication of two numbers:{x(a,b)}")


'''2.Recursive Function:
Write a recursive function that calculates the sum of the first `n` numbers.'''
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
n=int(input("How many numbers sum do you want?: "))
print(f'sum of {n} numbers is {sum(n)}')


'''3.Variable-Length Arguments:
Write a function that accepts any number of arguments and returns their average.'''
def average(*nums):
    sum=0
    n=len(nums)
    for i in nums:
        sum+=i
    return sum/n
print(f"Average:{average(10,20,70,45)}")