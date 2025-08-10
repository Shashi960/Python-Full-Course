#OPERATOR
#Assignment operator
x=5
print(x)
x+=5
print(x)
x-=2
print(x)
x*=2
print(x)
x/=2
print(x)
x%=2
print(x)

#COMPARISION OPERATOR
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)


#LOGICAL OPERATOR 
print(1>2 and 2>1)
print(1>2 or 2>1)
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not(True))
print(not(False))


#MEMBERSHIP 
list=[2,4,6,8,10]
str="Shashi"
print(3 in list)
print(2 in list)
print("s" in str)
print("A" in str)


#BITWISE OPERATOR
a=5
b=3
print(a&b)
print(a|b)
print(~a)
print(a<<1)
print(a>>1)


# DAY 4 HOMEWORK 
"""1)program for taking 2 input from user and check if 
-both  numbers are greater than 10
-at least one number is less than 5
-the first number is not greater than second  (using not)"""
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print(f"Both numbers are greater than 10 : {a>10 and b>10}")
print(f"at least one number is less than 5 : {a<5 or a<5}")
print(f"The first number is not greater than second : {not(a>b)}")

#2)CHeck user age is eligible to vote ir not
age=int(input("Enter Your Age : "))
if(age>=18):
    print("You are Eligible to vote")
if(age<18):
    print("You are not eligible to vote")

#3)program for membership
str=input("Enter a string :")
print('s' in str)
print('shi' in str)











