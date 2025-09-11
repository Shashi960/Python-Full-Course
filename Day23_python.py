#File Handling
#(read)
# To read file
file=open('Day1_python.py','r')
print(file.read())
file.close()

#(write)
# To write or creates file(It overwrites file Content if File Exists)
file=open('file1.txt','w')
file.write('This file contain some lines.')
file=open('file1.txt','r')
print(file.read())
file.close()

#(append)
# Adds data to end of last content without deleting existing Content
file=open('file1.txt','a')
file.write('\nNext line it is')
file=open('file1.txt','r')
print(file.read())
file.close()

#(x-create)
#it creates a file if a file exist it does not overwrites like write it shows eror
try:
    file_name=input("Enter File Name: ")
    file=open(file_name,'x')

except Exception as e:
    print(f'Error:{e}')

else:
    file.write('Shashi\nKumar\nNayani')
    file=open(file_name,'r')
    print(f"{file_name} Contents:\n{file.read()}")
finally:
    file.close()

#Example
list=['Ramesh','Suresh','Manoj','Pavan']
file=open('file3.txt','w')
for i in list:
    file.write(f'{i}\n')
file.close()



#(with)
'''using with helps automatically closes the opened file 
Because some time we for got to close the file,
So it is necessary to close to prevent unnessary ram Usage
We can take above example '''
list=['Ramesh','Suresh','Manoj','Pavana']
with open('file3.txt','w') as file:
    for i in list:
        file.write(f'{i}\n')


#read() 
#Reads Entire content from a file
file=open('file3.txt','r')
print("\n")
print(file.read())

#readLine() 
#Reads Single line of a file
file=open('file3.txt','r')
print("\n")
print(file.readline())

#readLines() 
#Reads all lines into a list
file=open('file3.txt','r')
print(file.readlines())

#strip()
#uses as readline
with open('file3.txt','r') as file:
    for i in file:
        print("student:", i.strip())


#Homework
'''1.Create a File and Write

   * Ask user for 3 friend names.
   * Write them into `friends.txt`, one per line.'''
with open('friends.txt','w') as file:
    for i in range(0,3):
        file.write(input("Enter Friend Name: "))
        file.write("\n")
    print("Friends")
with open('friends.txt','r') as file1:
    print(file1.read())


'''2.Append Marks

   * Ask for student name and marks.
   * Append the info to `marks.txt` in this format: `Ravi - 85`'''
with open('marks.txt','w')as file:
    n=int(input("How many students?: "))
    for i in range(0,n):
        name=input("Enter Name: ")
        marks=int(input("Enter Marks: "))
        file.write(f"`{name}-{marks}`\n")
with open('marks.txt','r') as file:
    print(file.read())

'''3.Read and Count Lines

   * Read any file and count how many lines it has.
   * Example: How many students are listed?'''
files=input("Enter File Name: ")
with open(files,'r') as file:
    c=file.readlines()
    print(f"{files} file contain {len(c)} lines")

'''4.Search From File

   * Write a program that searches for a name in `friends.txt`
   * If found, print "Found!" else "Not Found!"'''
with open('friends.txt','r') as file:
    content=file.read()
    name=input("Enter search Name in friends.txt: ")
    if name in content:
        print("Found!")
    else:
        print("Not found!")



