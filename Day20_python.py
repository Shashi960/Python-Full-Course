#1. Banking System Simulation
'''Design a system to simulate a bank's operations, where users can create accounts, deposit and withdraw money, and check their account balance.  
- Extend functionality to include multiple account types (e.g., savings, current) with unique behaviors like interest calculation or overdraft limits.
- Emphasize encapsulation, inheritance and polymorphism'''
class Account:
    def __init__(self,id,holder_name):
        self.id=id
        self.holder_name=holder_name
        self._balance=0
    
    def check_balance(self):
        print(f"Balance:{self._balance}")

    def deposit(self,amount):
        self._balance+=amount
        print(f'Amount Credited Successfully ,New Updated balance {self._balance}')
    
    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance-=amount
            print(f'Amount Debited Successfully ,New Updated balance {self._balance}')
        else:
            print("Insufficient Amount To Withdraw..")

class SavingsAccount(Account):
    def calculate_interest(self):
        INTEREST_RATE=0.04
        interest=self._balance*INTEREST_RATE
        print(f"Interest Amount: {interest}")

class CurrentAccount(Account):
    def withdraw(self,amount):
        overdraft=1000
        if self._balance+overdraft>=amount:
            self._balance-=amount
            print(f'Amount Debited Successfully ,New Updated balance {self._balance}')
        else:
            print("Amount is Over Limit..")
class Bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__accounts={}
    def create_account(self,id,holder_name,type):
        if type=="savings":
            new_account=SavingsAccount(id,holder_name)
        elif type=="current":
            new_account=CurrentAccount(id,holder_name)
        self.__accounts[id]=new_account
        print("Account Created succcessfully:")
        return new_account
    def get_account(self,id):
        if id not in self.__accounts:
            print("Acccount not Found")
        else:
            account=self.__accounts[id]
            print(f"\n ID:{account.id} \n Holder Name:{account.holder_name}")

sbk=Bank("State Bank of Karnataka","Honnavara")
#sbk.create_account(1,"ravi",'savings')
#s1=Account()
#s1.check_balance()
print("======Welcome To State Bank of Karnataka=======")
while True:
    print("Select operations:")
    print("1.create Account\n2.Check Balance\n3.Deposit Money\n4.Withdrraw Amount\n5.Calculate interest\n6.Get Account Details\n6.Exit")
    ch=int(input("Enter Your Choice: "))
    if ch == 1:
        id=int(input("Enter Your ID: "))
        name=input("Enter Your Name: ")
        acc_type=input("Enter Your account type(savings/currrent): ")
        sbk.create_account(id,name,acc_type)
    elif ch == 2:
        id=int(input("Enter Account id: "))
        name=input("Enter Your Name: ")
        account=Account(id,name)        
        account.check_balance()
    elif ch == 3:
        amt=int(input("Enter amount to Deposit: "))

    elif ch == 4:
        amt=int(input("Enter Amount to withdraw:"))
    elif ch == 5:
        print("hello")
    elif  ch == 6:
        print("Account id : Account Name")

    else:
        break
    
'''2. Library Management System
Create a library system that keeps track of books, borrowers, and availability. Allow borrowing, returning, and viewing available books.
- Include due dates, penalties for late returns, and unique IDs for books and users.
- Focus on class relationships and method responsibilities'''
import datetime

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.borrower_id = None
        self.due_date = None

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by User {self.borrower_id}, Due: {self.due_date}"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}"


class Library:
    PENALTY_RATE = 5  # ₹5 per day late

    def __init__(self, name):
        self.name = name
        self.books = {}
        self.users = {}

    # Add book to library
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("Book ID already exists.")
            return
        self.books[book_id] = Book(book_id, title, author)
        print("Book added successfully!")

    # Register user
    def add_user(self, user_id, name):
        if user_id in self.users:
            print("User ID already exists.")
            return
        self.users[user_id] = User(user_id, name)
        print("User registered successfully!")

    # Show available books
    def show_available_books(self):
        available = [book for book in self.books.values() if book.is_available]
        if not available:
            print("No books available right now.")
        else:
            print("\n--- Available Books ---")
            for book in available:
                print(book)

    # Borrow book
    def borrow_book(self, book_id, user_id):
        if book_id not in self.books:
            print("Book not found.")
            return
        if user_id not in self.users:
            print("User not registered.")
            return

        book = self.books[book_id]
        if not book.is_available:
            print("Book already borrowed.")
            return

        book.is_available = False
        book.borrower_id = user_id
        book.due_date = datetime.date.today() + datetime.timedelta(days=7)
        print(f"Book borrowed successfully! Due Date: {book.due_date}")

    # Return book
    def return_book(self, book_id, user_id):
        if book_id not in self.books:
            print("Book not found.")
            return
        book = self.books[book_id]
        if book.is_available:
            print("Book was not borrowed.")
            return
        if book.borrower_id != user_id:
            print("This user didn’t borrow the book.")
            return 

        today = datetime.date.today()
        penalty = 0
        if today > book.due_date:
            days_late = (today - book.due_date).days
            penalty = days_late * self.PENALTY_RATE
            print(f"Book returned late by {days_late} days. Penalty: ₹{penalty}")
        else:
            print("Book returned on time.")

        book.is_available = True
        book.borrower_id = None
        book.due_date = None


library = Library("Shashi Public Library")

while True:
    print("\n===== Library Management Menu =====")
    print("1. Add Book")
    print("2. Register User")
    print("3. Show Available Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.add_book(book_id, title, author)

    elif choice == "2":
        user_id = int(input("Enter User ID: "))
        name = input("Enter User Name: ")
        library.add_user(user_id, name)

    elif choice == "3":
        library.show_available_books()

    elif choice == "4":
        user_id = int(input("Enter User ID: "))
        book_id = int(input("Enter Book ID: "))
        library.borrow_book(book_id, user_id)

    elif choice == "5":
        user_id = int(input("Enter User ID: "))
        book_id = int(input("Enter Book ID: "))
        library.return_book(book_id, user_id)

    elif choice == "6":
        print("Thank you for using the Library System!")
        break

    else:
        print("Invalid choice! Please try again.")

'''3. Hospital Patient Management**
Create a hospital management system that tracks doctors, patients, and appointments.  
- Doctors can have specialties, and patients may have different ailments.
- Each appointment should store the doctor-patient relationship, along with the date and time.
- Add functionality for doctors' schedules and ensuring no double booking.'''

import datetime

class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialty: {self.specialty}"


class Patient:
    def __init__(self, patient_id, name, ailment):
        self.patient_id = patient_id
        self.name = name
        self.ailment = ailment

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Ailment: {self.ailment}"


class Appointment:
    def __init__(self, doctor, patient, date, time):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

    def __str__(self):
        return (f"Appointment - Doctor: {self.doctor.name} ({self.doctor.specialty}), "
                f"Patient: {self.patient.name} ({self.patient.ailment}), "
                f"Date: {self.date}, Time: {self.time}")


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = {}
        self.patients = {}
        self.appointments = []

    # Add doctor
    def add_doctor(self, doctor_id, name, specialty):
        if doctor_id in self.doctors:
            print("Doctor ID already exists.")
            return
        self.doctors[doctor_id] = Doctor(doctor_id, name, specialty)
        print("Doctor added successfully!")

    # Add patient
    def add_patient(self, patient_id, name, ailment):
        if patient_id in self.patients:
            print("Patient ID already exists.")
            return
        self.patients[patient_id] = Patient(patient_id, name, ailment)
        print("Patient added successfully!")

    # Schedule appointment
    def schedule_appointment(self, doctor_id, patient_id, date, time):
        if doctor_id not in self.doctors:
            print("Doctor not found.")
            return
        if patient_id not in self.patients:
            print("Patient not found.")
            return

        # check double booking
        for appt in self.appointments:
            if appt.doctor.doctor_id == doctor_id and appt.date == date and appt.time == time:
                print("Doctor already has an appointment at this time.")
                return

        doctor = self.doctors[doctor_id]
        patient = self.patients[patient_id]
        new_appointment = Appointment(doctor, patient, date, time)
        self.appointments.append(new_appointment)
        print("Appointment scheduled successfully!")

    # Show all doctors
    def show_doctors(self):
        if not self.doctors:
            print("No doctors registered.")
        else:
            print("\n--- Doctors ---")
            for d in self.doctors.values():
                print(d)

    # Show all patients
    def show_patients(self):
        if not self.patients:
            print("No patients registered.")
        else:
            print("\n--- Patients ---")
            for p in self.patients.values():
                print(p)

    # Show appointments
    def show_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            print("\n--- Appointments ---")
            for appt in self.appointments:
                print(appt)



hospital = Hospital("Shashi Multispeciality Hospital")

while True:
    print("\n===== Hospital Management Menu =====")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Show Doctors")
    print("4. Show Patients")
    print("5. Schedule Appointment")
    print("6. Show Appointments")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        doc_id = int(input("Enter Doctor ID: "))
        name = input("Enter Doctor Name: ")
        specialty = input("Enter Specialty: ")
        hospital.add_doctor(doc_id, name, specialty)

    elif choice == "2":
        pat_id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        ailment = input("Enter Ailment: ")
        hospital.add_patient(pat_id, name, ailment)

    elif choice == "3":
        hospital.show_doctors()

    elif choice == "4":
        hospital.show_patients()

    elif choice == "5":
        doc_id = int(input("Enter Doctor ID: "))
        pat_id = int(input("Enter Patient ID: "))
        date = input("Enter Date (YYYY-MM-DD): ")
        time = input("Enter Time (HH:MM): ")
        hospital.schedule_appointment(doc_id, pat_id, date, time)

    elif choice == "6":
        hospital.show_appointments()

    elif choice == "7":
        print("Thank you for using Hospital Management System!")
        break

    else:
        print("Invalid choice! Please try again.")




'''4. E-Commerce Platform Prototype**
Simulate a basic e-commerce platform where customers can browse products, add them to a cart, and place orders.  
- Use OOP principles to manage inventory, pricing (e.g., discounts), and order tracking.
- Integrate functionality for calculating taxes and shipping costs dynamically.

'''
class Product:
    def __init__(self, product_id, name, price, stock, discount=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.discount = discount  # percentage discount

    def get_price_after_discount(self):
        return self.price * (1 - self.discount / 100)

    def __str__(self):
        return (f"ID: {self.product_id}, {self.name}, "
                f"Price: ₹{self.price}, Discount: {self.discount}%, "
                f"Final Price: ₹{self.get_price_after_discount():.2f}, Stock: {self.stock}")


class Cart:
    TAX_RATE = 0.1   # 10% tax
    SHIPPING_COST = 50

    def __init__(self):
        self.items = {}  # product_id -> quantity

    def add_to_cart(self, product, quantity):
        if product.stock < quantity:
            print("Not enough stock available.")
            return
        self.items[product.product_id] = self.items.get(product.product_id, 0) + quantity
        product.stock -= quantity
        print(f"{quantity} x {product.name} added to cart.")

    def calculate_total(self, inventory):
        subtotal = 0
        for pid, qty in self.items.items():
            product = inventory[pid]
            subtotal += product.get_price_after_discount() * qty
        tax = subtotal * self.TAX_RATE
        total = subtotal + tax + (self.SHIPPING_COST if subtotal > 0 else 0)
        return subtotal, tax, self.SHIPPING_COST if subtotal > 0 else 0, total

    def clear_cart(self):
        self.items.clear()


class Order:
    order_counter = 1

    def __init__(self, cart, inventory):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.items = cart.items.copy()
        self.subtotal, self.tax, self.shipping, self.total = cart.calculate_total(inventory)

    def __str__(self):
        return (f"Order ID: {self.order_id}\n"
                f"Subtotal: ₹{self.subtotal:.2f}, Tax: ₹{self.tax:.2f}, "
                f"Shipping: ₹{self.shipping}, Total: ₹{self.total:.2f}")


class ECommercePlatform:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.orders = []

    # Add product to inventory
    def add_product(self, product_id, name, price, stock, discount=0):
        if product_id in self.inventory:
            print("Product ID already exists.")
            return
        self.inventory[product_id] = Product(product_id, name, price, stock, discount)
        print("Product added successfully!")

    # Show available products
    def show_products(self):
        if not self.inventory:
            print("No products available.")
        else:
            print("\n--- Available Products ---")
            for product in self.inventory.values():
                print(product)

    # Place order
    def place_order(self, cart):
        if not cart.items:
            print("Cart is empty.")
            return
        new_order = Order(cart, self.inventory)
        self.orders.append(new_order)
        print("\nOrder placed successfully!")
        print(new_order)
        cart.clear_cart()

    # Show all orders
    def show_orders(self):
        if not self.orders:
            print("No orders yet.")
        else:
            print("\n--- Order History ---")
            for order in self.orders:
                print(order)


platform = ECommercePlatform("Shashi Online Store")
cart = Cart()

while True:
    print("\n===== E-Commerce Menu =====")
    print("1. Add Product to Inventory")
    print("2. Show Products")
    print("3. Add Product to Cart")
    print("4. View Cart & Checkout")
    print("5. Show Orders")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock Quantity: "))
        discount = float(input("Enter Discount % (0 if none): "))
        platform.add_product(pid, name, price, stock, discount)

    elif choice == "2":
        platform.show_products()

    elif choice == "3":
        platform.show_products()
        pid = int(input("Enter Product ID: "))
        qty = int(input("Enter Quantity: "))
        if pid in platform.inventory:
            product = platform.inventory[pid]
            cart.add_to_cart(product, qty)
        else:
            print("Product not found.")

    elif choice == "4":
        subtotal, tax, shipping, total = cart.calculate_total(platform.inventory)
        print(f"\nCart Summary:\nSubtotal: ₹{subtotal:.2f}, Tax: ₹{tax:.2f}, Shipping: ₹{shipping}, Total: ₹{total:.2f}")
        confirm = input("Do you want to place the order? (yes/no): ").lower()
        if confirm == "yes":
            platform.place_order(cart)

    elif choice == "5":
        platform.show_orders()

    elif choice == "6":
        print("Thank you for shopping with us!")
        break

    else:
        print("Invalid choice! Please try again.")




'''5. Student Report Card Generator**
Build a system that collects student data and subject-wise marks to generate a report card.
- Include grade calculation, average score, and pass/fail result.
- Use encapsulation for mark storage and method abstraction for result generation.'''

class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.__marks = {}   # Encapsulation: private mark storage

    # Add marks for subjects
    def add_marks(self, subject, marks):
        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100")
            return
        self.__marks[subject] = marks
        print(f"Marks for {subject} added successfully!")

    # Calculate average
    def calculate_average(self):
        if not self.__marks:
            return 0
        return sum(self.__marks.values()) / len(self.__marks)

    # Determine grade
    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 85:
            return "A+"
        elif avg >= 70:
            return "A"
        elif avg >= 55:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "F"

    # Pass/Fail
    def result(self):
        if all(m >= 40 for m in self.__marks.values()):
            return "Pass"
        return "Fail"

    # Generate report card
    def generate_report(self):
        print("\n===== Report Card =====")
        print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}")
        print("\n--- Marks ---")
        for sub, marks in self.__marks.items():
            print(f"{sub}: {marks}")
        avg = self.calculate_average()
        print(f"\nAverage: {avg:.2f}")
        print(f"Grade: {self.calculate_grade()}")
        print(f"Result: {self.result()}")
        print("==========================")


class ReportCardSystem:
    def __init__(self):
        self.students = {}

    # Add student
    def add_student(self, student_id, name, course):
        if student_id in self.students:
            print("Student ID already exists.")
            return
        self.students[student_id] = Student(student_id, name, course)
        print("Student added successfully!")

    # Get student
    def get_student(self, student_id):
        return self.students.get(student_id, None)

    # Show all students
    def show_students(self):
        if not self.students:
            print("No students added yet.")
        else:
            print("\n--- Student List ---")
            for s in self.students.values():
                print(f"ID: {s.student_id}, Name: {s.name}, Course: {s.course}")



system = ReportCardSystem()

while True:
    print("\n===== Student Report Card Menu =====")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. Generate Report Card")
    print("4. Show All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        system.add_student(sid, name, course)

    elif choice == "2":
        sid = int(input("Enter Student ID: "))
        student = system.get_student(sid)
        if student:
            subject = input("Enter Subject Name: ")
            marks = int(input("Enter Marks (0-100): "))
            student.add_marks(subject, marks)
        else:
            print("Student not found. ")

    elif choice == "3":
        sid = int(input("Enter Student ID: "))
        student = system.get_student(sid)
        if student:
            student.generate_report()
        else:
            print("Student not found.")

    elif choice == "4":
        system.show_students()

    elif choice == "5":
        print("Exiting Report Card System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")



        


