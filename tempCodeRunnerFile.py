with open('friends.txt','r') as file:
    content=file.read()
    name=input("Enter search Name in friends.txt: ")
    if name in content:
        print("Found!")
    else:
        print("Not found")
