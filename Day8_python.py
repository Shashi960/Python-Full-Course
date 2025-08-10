#Condition Statements(indentation is needed)
#if-statements
Age=int(input("Enter Your Age: "))
if(Age>=18):
    print("Congratulations ! You  Are Eligible To Vote")

#if-else statements
Age=int(input("Enter Your Age: "))
if(Age>=18):
    print("Congratulations ! You  Are Eligible To Vote")
else:
    print("Sorry, You are Not Eligible To Vote.")

#if-elif-else
marks=int(input("Enter Your Marks: "))
if(marks>=90):
    print("A+")
elif(marks>=60):
    print("B+")
elif(marks>=35):
    print("C+")
else:
    print("Not Pass")


#nested-if
age=int(input("Enter Your Age: "))
if(age>=18):
    yes_no=input("you have voter id?(yes/no): ")
    if(yes_no=="yes"):
        print("You can Vote")
    else:
        print("You need to make voter card for voting")
else:
    print("You are not eligible to vote")

#match Case
print("Welcome to calcultor")
print("+ - * / %  ")
case=input("Enter Your choice")
a=int(input("Enter First number: "))
b=int(input("Enter Second number: "))
match case:
    case "+":
        print(a+b)
    case "-":
        print(a+b)
    case "*":
        print(a+b)
    case "/":
        print(a+b)
    case "%":
        print(a+b)
    case _:
        print("Errror!")


#Homework

'''1.Basic Conditions:
Write a program to check if someone is eligible for a bus pass. If they are below 5 years, the bus pass is free. If they are 60 years or older, they get a senior citizen discount. Otherwise, they pay the full price.'''  
age=int(input("Enter Your Age: "))
if(age<5):
    print("You Are Eligible For Bus Pass")
elif(age>=60):
    print("You are able to get senior citizen discount")
else:
    print("You need to pay the full price for the ticket")

'''2.Meal Time Checker:
Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
     - Breakfast: 8 AM to 9AM
     - Lunch: 1 PM to 2PM
     - Dinner: 8 PM to 9PM
     - If none of these times, print "It's not meal time".'''
print("MEAL TIME CHECKER")
print("===================")
h=int(input("Enter Hour: "))
if(h<24):
    t=int(input("Enter Time: "))
    if(t>=60):
        h=h+1
        t=t-60
    if(h<=12):
        am_pm=input("AM or PM: ")
        print(f"TIME:{h}:{t} {am_pm}")
    else:
        print(f"TIME:{h}:{t}")
    if(h==8 and (am_pm=='AM' or am_pm=='am')):
        print("It's Breakfast Time.")
    elif((h==1 and (am_pm=='PM' or am_pm=='pm')) or h==13):
        print("It's Dinner Time.")
    elif((h==8 and (am_pm=='PM' or am_pm=='pm')) or h==20):
        print("It's Lunch Time.")
    else:
        print("It's not meal time")
        



'''3.Simple Eligibility Check:
Write a program that checks whether a person is eligible for a library membership. If they are under 18, they get a student membership. If they are 60 or older, they get a senior citizen membership. Otherwise, they get a regular membership.'''
age=int(input("Enter Your Age: "))
if(age<18):
    print("You are eligible to get student membership.")
elif(age>=60):
    print("You are eligible to get senior citizen membership.")
else:
    print("You need to get regular membership.")