age=int(input("Enter Your Age: "))
if(age>=18):
    yes_no=input("you have voter id?(yes/no): ")
    if(yes_no=="yes"):
        print("You can Vote")
    else:
        print("You need to make voter card for voting")
else:
    print("You are not eligible to vote")
