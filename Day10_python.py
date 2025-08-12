#FOR Loops
#printing 1 to 20 numbers using for loop
print("printing 1 to 20 numbers using for loop")
for i in range(1,21):
    print(i)
print(" ")
#printing 1 to 20  even numbers using for loop
print("printing 1 to 20  even numbers using for loop")
for i in range(2,21,2):
    print(i) 
    print(" ")


#using list
print("Fruits in bag")
bag=['Apple','Orange','Mango','Banana']
for fruits in bag:
    print(fruits)
print(" ")

#using string
print("Letter Slicig")
str="Shashi"
for letter in str:
    print(letter.upper(),end=' ')
print("\n")


#enumerate function
'''enumerate() unpack  the items and index'''
print("enumerate() using")
str="shashi"
for index,letter in enumerate(str):
    print(f"Letter {letter} in {index}th index")
print(" ")

print("Simple code")
str="shashi"
for index,letter in enumerate(str):
    print(letter*(index+1))
print("")


#else in for loops
for i in range(1,11):
    print(i)
    #if i==6:
        #break
else:
    print("All Printed")

print("")

#using dictionary
d={'name':'Ravi',
   'age':'33',
   'city':'honnavara'
}

for i,item in d.items():
    print(i+" "+item)
print(" ")

#nested for loop 
print("printing 1 to 20 multiplication table using nested for loop")
for i in range(1,21):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print(" ")

#OR
for i in range(1,11):
    for j in range(1,11):
        print(f"{j}*{i}={i*j}",end="   ")
    print("\n ")
#multiplication table using user input
print(" ")
n=int(input("Which number multiplication table you want?: "))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
print(" ")

#Homework
'''1.Multiples of 3:
Write a `for` loop that prints all multiples of 3 between 1 and 30.'''
print("all multiples of 3 between 1 and 30")
for i in range(1,11):
    print(i*3,end=" ")

'''2.Sum of First 10 Numbers:
Write a program using a `for` loop that calculates the sum of numbers from 1 to 10.'''
sum=0
for i in range(1,11):
    sum+=i
print(f"sum of numbers from 1 to 10 is:{sum}")
print(" ")
    
'''3.Print Your Name Letter by Letter:
Write a program that takes your name as input and prints each letter of your name using a `for` loop.'''
str=input("Enter your name: ")
for i in str:
    print(i,end="  ")
print("\n")
'''4. Count Vowels in a String:
Write a program that counts how many vowels are in a given string using a `for` loop.'''
str=input("Enter A string: ")
vovels=['a','e','i','o','u','A','E','I','O','U']
list=[]
count=0
for i in str:
    if i in vovels:
       # if  i in list:
            #continue
        count+=1
        list.append(i)
if(count>0):
    print(f"{count} vowels are there in a given string.\nThey are {list} ")
else:
    print("No vewels found")
