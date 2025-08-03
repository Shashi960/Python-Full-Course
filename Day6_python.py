#Tuples
a=('male','Female','others')
print(a)
print(a[0])
print(type(a))
print(len(a))

b=('apple',) #if an tuple has an single or only one elements then it should contain comma at last before closing bracket
print(b)

c=('2',)
print(c)
print(type(c))

#Concatanation
tuples=a+b
print(tuples)
print(type(tuples))

#repeattion
print(b*3)

#membership
print('male' in a)


#methods
print(a)
print(a.count('male'))
print(a.index('others'))

#SETS
s={'milk','butter','bread','milk'}  #set creation using {} 
print(s)

s1=set(('milk','butter','bread','milk')) #set creation using set()
print(s1)
print(type(s1))

#SET OPERATIONS
s1={1,2,3}
s2={3,4,5}
print(s1 | s2) #union
print(s1&s2) # intersection
print(s1-s2) #set difference 
print(s1 ^ s2) #symmetric difference 


#SET METHODS
s={1,2,3,4,5}
s.add(6)
print(s)
s.remove(6) #it will shows an error if specified element is not in the set
print(s)
s.discard(8) #it does not shows an error if specified element is not in the set
print(s)
s.pop()
print(s)
s.clear
print(s)


#HOME WORK 
#1)Tuple 
a=(1,2,3,4,5)
print(a)
b=list(a)
print(b)
b.append(6)
print(b)
a=tuple(b)
print(a)

print(a[1:3])

t1=(10,12,14,16)
print(a+t1)


#2
s={'banana','guava','Apple','kiwi'}
s1={'Apple','banana','drago fruit','orange'}
print(s|s1)#union
print(s&s1)#intersection
print(s-s1)#set difference
s.remove('Apple') #or
s.discard('Apple')


#3
l=[1,2,3,4,5,6,7,8,9,10]
t=tuple(l)
print(t)
s=set(l)
print(s)

s.add(12)
print(s)
