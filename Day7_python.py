#Dictionary
Birthday={
    "Shashi":"30-11-2003",
    "Nithin":"10-02-2008"
}
print(Birthday)
print(type(Birthday))

#Acessing Dictionary Items
print(Birthday["Shashi"])  #Using Key but it will shows an erroro if key does not present in the specified dictionary

print(Birthday.get("Shashi"))
print(Birthday.get("Ravi","Could not Found")) #Using get() method safer execution is possible

#Adding and Updating Items
print("before adding New value:")
print(Birthday)
Birthday["Ramesh"]='03-03-2006'
print("After adding New value:")
print(Birthday)

#updating 
Birthday["Ramesh"]='03-03-2004'
print(Birthday)

#Deleting and clearing 
x=Birthday.pop("Ramesh")
print(x)

del Birthday["Nithin"]
print(Birthday)

Birthday.clear()

#Dictionary Methods
Birthday={
    "Shashi":"30-11-2003",
    "Nithin":"10-02-2008"
}

#For all keys
print(Birthday.keys())
#For all values
print(Birthday.values())
#For all key value pairs
print(Birthday.items())
#adding another dictionary
Birthday1={'sanju':'09-02-2009'}
Birthday.update(Birthday1)
print(Birthday)

#just Practise
item1={
    'Name':'Rice',
    'Weight':2,
    'Amount':200
    }

item2={
    'Name':'Chilli',
    'Weight':1,
    'Amount':150
    }

item3={
    'Name':'Ginger',
    'Weight':0.5,
    'Amount':80
    }
item4={
    'Name':'Tomato',
    'Weight':4,
    'Amount':60
    }

Items=[item1,item2,item3,item4]
print(f"Total weights : {item1["Weight"]+item2["Weight"]+item3["Weight"]+item4["Weight"]} Kg.")
print(f"Total weights : {item1["Amount"]+item2["Amount"]+item3["Amount"]+item4["Amount"]} Rs.")


#Homework
'''1.Basic Dictionary Operations**:
   - Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
   - Add a new city and its dish to the dictionary.
   - Update the dish for Bengaluru.
   - Remove one city from the dictionary.
   - Use the `keys()` method to print all city names in the dictionary.
   - Use the `values()` method to print all dishes in the dictionary.'''
#Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
dishes={'Honnavara':'Fish_fry',
        'Mysooru':'Mysore_pak',
        'Dharwad':'Peda',
        'Hubli':'Rotti',
        'Mandya':'Mudde'
        }
print("Cities And their Dishes")
print(dishes)
# Add a new city and its dish to the dictionary.
city=input("Enter city Name: ")
dish=input("Enter Dish Name: ")
dishes[city]=dish
print(dishes)

#Remove one city from the dictionary
rcity=input("Enter city name which you want to remove: ")
dishes.pop(rcity)
print(dishes)

#- Use the `keys()` method to print all city names in the dictionary.
print("All cities in the dictionary")
print(dishes.keys())

#OR
print("All cities in the dictionary")
for keys in dishes.keys():
    print(keys)

# - Use the `values()` method to print all dishes in the dictionary.
print("All dishes in the dictionary")
print(dishes.values())

#OR
print("All dishes in the dictionary")
for keys in dishes.values():
    print(keys)

'''2.Nested Dictionary Practice (Simple for now):
   - Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
   - Access and print the favorite food of one friend.'''
Friends={
    'friend1':{'Name':'Ravi',
             'Favorite_subject':'Maths',
             'Favorite_Food':'Pizza'
             },
    'friend2':{'Name':'Raju',
             'Favorite_subject':'Bio',
             'Favorite_Food':'Samosa'
             }            
             
}

print(f"Favorite Food of friend2 {Friends['friend2']['Favorite_Food']}")