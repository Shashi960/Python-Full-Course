#VARIABLE
#value assigning to the variable
a=10
b=20
c=30 

print(f"{a},{b},{c}")

#OR
a,b,c=15,30,45
print(f"{a},{b},{c}")

#Same value assigining to the variable
a=b=c=10
print(f"{a},{b},{c}")

 #DATATYPES
age=23
name="Ganesh"
weight=23.6
is_student=True

print(type(age))          #int
print(type(name))         #str
print(type(weight))       #float
print(type (is_student))  #bool


#TYPE CONVERSION
s="100"
print(s)
print(type(s))
s1=int(s)
print(s1)
print(type(s1))
  

#DAY 2 HOME WORK
#Program for Arithmatic calculator
a=int(input("Enter a number: "))
b=int(input("Enter an another number: "))
print("select Operator")
print("+ - * / % // **")
ch=input("Choose an operator: ")
if ch=="+":
    print(f"Addition Value {a+b}")
elif ch=="-":
    print(f"Subtraction Value {a-b}")
elif ch=="*":
    print(f"Multiplication Value {a*b}")
elif ch=="/":
    print(f"Division Value {a/b}")
elif ch=="%":
    print(f"Modulus Value {a%b}")
elif ch=="//":
    print(f"Floor Division Value {a//b}")
elif ch=="**":
    print(f"Power Value {a**b}")
else:
    print("Invalid Choice")




#Program For Swap Number Without using Temp variable
print("For Swaping Two Numbers: ")
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print(f"A={a}\nB={b}")
a=a+b
b=a-b
a=a-b
print(f"A={a}\nB={b}")