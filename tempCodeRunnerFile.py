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