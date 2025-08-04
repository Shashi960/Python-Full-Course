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



