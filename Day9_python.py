#Loops or Control statements
#while loop
i=0
while(i<=10):
    print(i)
    i=i+1


#Printing Even numbers
val=int(input("How many even numbers are needed: "))
i=2
count=0
while(True):
    if(i%2!=0):
        i=i+1
        continue  
    print(i)
    count=count+1
    i=i+1
    if(count==val):
        break

'''printing this pattern
*
**
***
****
***** '''
i=1
while(i<=5):
    j=1
    while(j<=i):
        print("*",end=" ")
        j+=1
    print("\n")
    i+=1

'''printing this pattern
*****
****
***
**
* '''
i=1
while(i<=5):
    j=5
    while(j>=i):
        print("*",end=" ")
        j-=1
    print("\n")
    i+=1



#Homework
'''1.Basic Counting with `while` Loop:
   - Write a program that counts from 1 to 10 using a `while` loop.'''
i=1
while(i<=10):
    print(i)
    i+=1

'''2.Odd Numbers Printer:
Create a program that prints all odd numbers between 1 and 20 using a `while` loop.'''
i=1
while(i<=20):
    print(i)
    i+=2

#OR
i=1
while(i<=20):
    if(i%2!=0):
        print(i)
    i+=1

'''3.Ticket Booking Simulation:
   Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked, the available seats decrease. When there are no seats left, the loop stops and displays a message saying "All seats are booked."'''
list=[1,2,3,4,5,6,7,8]
while(len(list)!=0):
    print(f"Available Seats Are:{list}")
    seat=int(input("Which seat you want to book?: "))
    if(seat in list):
        print(f"Ticket Booked Your Seat Number is: {seat} .")
        list.remove(seat)
        print(f"Number of seat left {len(list)}")
    else:
        print("Seat already Booked!")
        print(" ")
    print("==========================")
    y_n=input("Do you Want To Book Another Ticket?: ")
    if(y_n=='No' or y_n=='no' or y_n=='NO'):
        break
    if(len(list)==0):
        print("All seats are booked")
        break




'''4. **Countdown Timer**:
Write a program that counts down from 10 to 1 using a `while` loop and prints "Happy New Year!" after the countdown is over.'''
i=10
while(i>=0):
    print(i)
    i-=1
print(' ""HAPPY NEW YEAR"" ')




