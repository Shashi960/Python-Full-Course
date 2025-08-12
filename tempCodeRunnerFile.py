list=[]
n=int(input("How many list you want to add:? "))
i=1
while(i<=n):
    list1=[int(item) for item in input("Enter numbers: ").split()]
    list.append(list1)
    i+=1
print("Given Lists Are:")
for i in list:
    sum=0
    print(i,end=" ")
    for item in i:
        sum+=item
    print(f"Sum={sum}")