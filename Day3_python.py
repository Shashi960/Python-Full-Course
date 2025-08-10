#Simple Program For Input And Output 
Boy_name=input("Enter Boy name: ")
Boy_age=int(input("Enter Boy age: "))

Girl_name=input("Enter Girl name: ")
Girl_age=int(input("Enter Girl age: "))

age_diff=abs(Boy_age-Girl_age)  #used abs because age difference never -ve, sometimes boy is younger than girl
print(f"{Boy_name} Loves {Girl_name}.Age Difference is {age_diff}")

#STRING
#concatanation
first_name="Shashi"
last_name="kodiya"
full_name=first_name+last_name
print(full_name)
full_name=first_name+ " "+last_name
print(full_name)

#repeatation
message="warning!"*100
print(message)

message="Warning"
print(message*10)

#string methods
str="good Morning "
print(str.upper())
print(str.lower())
print(str.strip()*2)
print(str.replace("Morning","night"))
print(len(str))

#For retaining quotes
str="manu said 'Hello'"
print(str)
str='manu said "Hello"'
print(str)

#for multi line 
str="""hello 
             'goood
                    Mornning' """
print(str)


#ACESSING STRING or SLICING
s="Shashi"
print(s[4])  #index=pos-1\
print(s[2:])
print(s[:2])
print(s[::-1])
print(s[-1])
print(s[2:5:2])
print(s[::2])


#ESCAPEE SEQUENECE
line="hari is a \ngood boy"
print(line)
line="hari is a \tgood boy"
print(line)

#Homework

'''1.Simple Greeting Program:
   Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the `+` operator and f-strings for output.'''
name=input("Enter Your Name : ")
age=input("Enter Your Age : ")
print("Hello " + name + "! You are " + age + " years old.")  # Using + operator
print(f"Hello {name}! You are {age} years old.")  # Using f-string


'''2.String Manipulation Exercise:
   Write a Python program that:
   - Takes a sentence as input from the user.
   - Prints the sentence in all uppercase and lowercase.
   - Replaces all spaces with underscores.
   - Removes leading and trailing whitespace'''
line=input("Enter a Sentence: ")
print(f"Uppercase :{line.upper()}")
print(f"Uppercase :{line.lower()}")
print(f"Uppercase :{line.replace(" ","_")}")
print(f"Uppercase :{line.strip()}")

'''3.Character Counter
   Write a Python program that:
   - Asks the user for a string.
   - Prints how many characters are in the string, excluding spaces.
'''
str=input("Enter a String: ")
i=0
for char in str:
    if char!=" ":
        i=i+1
print(f"Total number of character in a given string is: {i} ")

'''4.Escape Sequence Practice:
   Write a Python program that uses escape sequences to print the following output:
Output:
   ```
   Hello
       World
   This is a backslash: \
   ```
'''
str="Hello \n\t World\n This is a backslash: \\"
print(str)
