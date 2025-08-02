#LIST
list=['BCA','BBA','BCOM']
print(list)
print(list[0])
print(list[2])
print(list[-1])


#to remove last element
list1=[2,6,3,4,'ball','milk',[1,2,3]]
print(list1)
list1.pop()
print(list1)

#to add elements at last
list1.append("Banana")
print(list1)

#To remove element
list1.remove("ball")
print(list1)

#To add elements at perticular position
list1.insert(1,'ball')
print(list1)

#to replace item in a list
list1[6]='bread'
print(list1)

#List Slicing 
l=[100,200,300,400,500]
print(l[2:])
l1=l[2:]
print(l1)
print(l[0::2])

#COMMON fUNCTIONS IN LISTS
l=[2,4,6,8,10]
print(len(l))

l.append(7)
print(l)
print(sorted(l))

print(sum(l))

#Common Methods
print(list)
print(list.index('BBA')) #provides the index value of the item

print(list.count('BCA')) #count the number of elements of the name provided

list.reverse()  #reverse hte order of the elements
print(list)

list=[2,9,4,7,1,6]
list.sort()
print(list)

#Nested List
list=[[1,2],[3,4]]
print(list[0])
print(list[0][1])


#DAY 5 HOME WORK
#List Manipulation Exercise:

'''1)Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation.'''
list=[2,4,8,6,10]
list.append(12) #adds element st last position
print(list)
list.insert(1,3) #adds elements at index 1
print(list)
list.remove(8) #removes the third elements
print(list)


'''2)Reverse and Sort a List: Create a list of numbers and:
Sort it in descending order.
Reverse the sorted list and print it.'''
list=[2,6,3,7,9,1,4,8]
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)



