def average(*nums):
    sum=0
    n=len(nums)
    for i in nums:
        sum+=i
    return sum/n
print(f"Average:{average(10,20,70,45)}")