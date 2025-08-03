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