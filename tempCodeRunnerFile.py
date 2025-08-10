h=int(input("Enter Hour: "))
if(h<24):
    t=int(input("Enter Time: "))
    if(t>=60):
        h=h+1
        t=t-60
    if(h<=12):
        am_pm=input("AM or PM: ")
        print(f"TIME:{h}:{t} {am_pm}")
    else:
        print(f"TIME:{h}:{t}")
    if(h==8 and (am_pm=='AM' or am_pm=='am')):
        print("It's Breakfast Time.")
    elif((h==1 and (am_pm=='PM' or am_pm=='pm')) or h==13):
        print("It's Dinner Time.")
    elif((h==8 and (am_pm=='PM' or am_pm=='pm')) or h==20):
        print("It's Lunch Time.")
    else:
        print("It's not meal time")
        