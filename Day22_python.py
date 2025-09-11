#Errors And Exception Handling
a=int(input("A: "))
b=int(input("B: "))
try:
    print(a/b)
except Exception as e:
    print(f"Error: {e}")     #This May not under stand user
else:
    print("No Error Occured")
finally:
    print("Excecution Done")


#Catch specific Errors
try:
    a=int(input("A: "))
    b=int(input("B: "))

    print(a/b)

except ZeroDivisionError:
    print("Number Cannot be Division By Zero:")   

except ValueError:
    print("Value Must Be Number!!")   

else:
    print("No Error Occured")

finally:
    print("Excecution Done")



#raise
try:
    bike=input("Which Bike You Want To Buy Under 200 cc: ")
    if bike.lower() != 'pulsar':
        raise Exception("You Need To buy A Pulsar!!")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Pulsar is Good Choice")

finally:
    print("book pulsar Bike")



#HomeWork
'''1.Age Verifier:
   * Ask the user for their age.
   * If age is valid (number), show in how many years they will be 100 years old.
   * Handle invalid input gracefully.'''
try:
    age=int(input("Enter Your age: "))
    if (age<1 or age > 100):
        raise Exception("Age should be less than100 and greater than 1")    

except ValueError:
    print("Enter  Valid Age!!")
    age=int(input("Enter Your age: "))
    print(f"You will be 100 years old in {100-age} years")

except Exception as e:
    print(f"Error:{e}")

else:
    print(f"You will be 100 years old in {100-age} years")
finally:
    print("=========Done==========")

'''2.Safe Divider:
   * Ask two numbers from the user and divide them.
   * Handle ZeroDivisionError and ValueError.'''
try:
    a=int(input("A: "))
    b=int(input("B: "))

    print(a/b)

except ZeroDivisionError:
    print("Number Cannot be Division By Zero:")   

except ValueError:
    print("Value Must Be Number!!")   

else:
    print("No Error Occured")

finally:
    print("Excecution Done")


'''3.File Reader:
   * Ask the user for a file name and try to open it.
   * Show error message if file doesn't exist.
   * Use `finally` to print “Program End”.'''
try:
    filename = input("Enter file name: ")
    f = open(filename, "r")   # try to open the file
    print("\n--- File Content ---")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("Error: File does not exist!")

finally:
    print("Program End")
