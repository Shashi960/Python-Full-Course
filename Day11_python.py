#for loop extended
student_marks={}
num=int(input("How many students are there?: "))
for i in range(num):
    name=input("Enter Student Name: ")
    marks=int(input("Enter Student Marks: "))
    student_marks[name]=marks
for i,j in student_marks.items():
    print(f"{i}---{j}")
print()

#split() and list of inputs 
l="this is a tree"
words=l.split()
print(words)
print()

l="this-is-a-ball"
words=l.split("-")
print(words)
print()

#num of input 
list=input("Enter num of inputs: ")
words=list.split()
print(words)
print()

#OR
#num of string inputs
list=input("enter num of innputs: ").split()
print(list)
print()

#num of int inputs
list=input("enter num of inputs: ").split()
print(list)
number=[]
for i in list:
    number.append(int(i))
print(number)
print()

#OR
print("list inputs")
list=[int(num) for num in input("Enter list of numbers: ").split()]
print(list)


#List comprehension
#normal method
l=[1,2,3,4,5]
num=[]
for i in l:
    num.append(i*2)
print(num)

#by list comprehension
l=[1,2,3,4]
num=[i*2 for i in l]
print(num)

#1
l=[1,2,3,4,5,6,7,8,9,10]
num=[i*2 for i in l if i%2==0]
print(num)

#2
l=[1,2,3,4,5,6,7,8,9,10]
num=[i for i in l]
print(num)

#by dictionary comprehension
cities=['Honnavara','Kasarkod','Murdeshwar']
dic={city:len(city) for city in cities}
print(dic)
print(type(dic))
print()

item_price={'Banana':75,
            'Apple':50,
            'Orange':62,
            'Mango':42
            }
less_price={key:value for key,value in item_price.items() if value <=50}
print(less_price)

#HOMEWORK
'''1.List Manipulation:
Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.'''
food=['Dosa','Idli','Vada','Bonda','Payasa']
print(food)
food_upper=[item.upper() for item in food]
print(food_upper)

'''2.Sum of Prices:
Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a `for` loop.'''
vegetables={'Potato':30,
       'Tomato':20,
       'Ginger':100,
       'Onion':25,
       'Capsicum':60
}
print(vegetables)
sum=0
for price in vegetables.values():
    sum+=price
print(f"Total amount is :{sum}.")
print()


'''3.List of Squares:
Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.'''
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
square=[num*num for num in list]
print(square)
print()

'''4.Student Data Task:
Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.'''
s1={'name':'Ravi','age':21,'marks':72}
s2={'name':'Ramesh','age':22,'marks':98}
s3={'name':'Rani','age':21,'marks':64}
students=[s1,s2,s3]
for i in students:
    for detail,info in i.items():
        print(f"{detail}={info}",end=" ")
    print("\n")
print(" ")

'''5.Dictionary Comprehension:
Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.'''
populations={'Banglore':32,
             'Manglore':25,
             'Rayachuru':8,
             'Beedar':6,
             'Mysooru':22
             }
print(populations)
low_populations={city:pop for city,pop in populations.items() if pop<10}
print(low_populations)
print(" ")

'''6.Nested List Challenge:
Write a Python program that takes a list of lists (a 2D list) as input and:
   - Prints the entire matrix row by row.
   - Prints the sum of each row in the matrix.'''
list=[]
n=int(input("How many list you want to add:? "))
i=1
while(i<=n):
    list1=[int(item) for item in input("Enter numbers: ").split()]
    list.append(list1)
    i+=1
print("Given Lists and their elements sum:")
for i in list:
    sum=0
    print(i,end=" ")
    for item in i:
        sum+=item
    print(f"Sum={sum}")


    