class emp:
    def __init__(self,name,work,salary=30000):
         self.name=name
         self.work=work
         self.salary=salary
    def details(self):
         print(f"Name:{self.name}\n Designation:{self.work}\n Salary:{self.salary}")

e1=emp("Ravi","Manager",25000)
e2=emp("Raji","emp",55000)
e3=emp("Prassu",'emp')
e1.details()
e2.details()