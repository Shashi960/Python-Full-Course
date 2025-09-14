#Match Case
#Class Examples
num = int(input("Enter number: "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Other Number")

#class Example
Day = input("Enter A Day: ")

match Day.lower():
    case 'saturday' | 'sunday':
        print("Weekend")
    case 'Friday':
        print("Almost Weekend")
    case 'monday':
        print("Start ofth e week")
    case _:
        print("other day")

#Class Ecxample
time = int(input("Enter time(in hour H): "))
if time == 17:
    hungry = input("Are You Hungry?: ")
    if hungry == 'yes' or 'YES' or 'Yes' or 'Y' or 'y':
        is_hungry = True
    else:
        is_hungry = False

match time:
    case 9:
        print("Breakfast Time..")
    case 13 | 14:
        print("Lunch Time..")
    case 17 if is_hungry:
        print("Snacks Time")
    case 20 | 21:
        print("Dinner Time")
    case _:
        print("Do Work!!")


    
