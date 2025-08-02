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



