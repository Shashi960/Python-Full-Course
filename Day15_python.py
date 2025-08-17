#Class and Object
class Student:
   def __init__(self,name,age,marks):
      self.name=name
      self.ages=age
      self.marks=marks

   def scores(self):
      print(f"{self.name} scored {self.marks}")
   def age(self):
      print(f"{self.name} is {self.ages} years old")

A=Student("Kuppa",12,67)
A.scores()
A.age()


#Class with multiple Object
class Student:
   def __init__(self,name,age,marks):
      self.name=name
      self.ages=age
      self.marks=marks

   def scores(self):
      print(f"{self.name} scored {self.marks}")
   def age(self):
      print(f"{self.name} is {self.ages} years old")

A=Student("Krupa",12,67)
S=Student("Shashank",21,89)
S.scores()
A.scores()
S.age()
A.age()

      
'''5.Homework
1.Create a Class:
   - Write a class `Mobile` with attributes `brand` and `price`.
   - Create two objects of the class and display their attributes using a method.'''
class Mobile:
    def __init__(self,brand,price):
       self.brand=brand
       self.price=price
    def detail(self):
       print(f"{self.brand} costs {self.price}")
r=Mobile('Redmi',10000)
s=Mobile('Samsung',70000)
r.detail()
s.detail()

'''2.Method Definition:
- Define a class `Student` with attributes `name` and `marks`.
- Write a method `display_info()` that prints the student's name and marks.
- Create multiple objects of the `Student` class and call the method on each'''
class Student:
    def __init__(self,name,marks):
       self.name=name
       self.marks=marks

    def display_info(self):
       print(f"{self.name} scored {self.marks}")

s1=Student('Ravi',60)
s2=Student('Sameer',70)
s3=Student('Sarvesh',79)
s4=Student('Varun',98)

s1.display_info()
s2.display_info()
s3.display_info()
s4.display_info()
