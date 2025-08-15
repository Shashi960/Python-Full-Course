#Class Object Self __init__ and optional parameter in constructor
class Student:
    def __init__(self, name, marks="Not Given"):
        self.name = name
        self.marks = marks

    def show_marks(self):
        if self.marks=="Not Given":
              print(f"{self.name} 's marks: {self.marks}")
        else:
              print(f"{self.name} 's marks: {self.marks}/10")

b1 =Student("Ravi")
b2 = Student("Pramod", 7)

b1.show_marks()
b2.show_marks()


'''5. Homework
1.Create a Class with a Constructor:
   - Write a class `Movie` with attributes `title` and `rating` using the `__init__()` constructor.
   - Define a method to display the movie’s title and rating.'''
class Movie:
    def __init__(self,name,rating):
         self.name=name
         self.rating=rating
    def show_detail(self):
         print(f"{self.name} rated {self.rating}")

m1=Movie("KGF",5)
m2=Movie("Kaantara",5)
m3=Movie("Pushpa",3)
m1.show_detail()
m2.show_detail()
m3.show_detail


'''2. **Add Default Parameters**:
   - Create a class `Employee` with attributes `name`, `designation`, and `salary` (default value of `salary` is 30,000).
   - Write a method that displays the details of each employee.
   - Create multiple `Employee` objects with different values for `name` and `designation`, and test the default `salary` behavior.'''
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
