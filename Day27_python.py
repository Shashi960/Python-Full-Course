#Decorator
def welcome(func):
    def wrapper():
        print("Namaskara")
        func()
        print("Take Care")
    return wrapper

@welcome
def myself():
    print("hello ,I am Shashank from Honnavara.")

myself()


#Decorator With Arguements
def show_result(func):
    def wrapper(a, b):
        print("Result: ",end='')
        func(a, b)
    return wrapper

@show_result
def add(a, b):
    print(a+b)

@show_result
def subtract(a, b):
    print(a-b)

add(2, 5)
print("\n")
subtract(7, 5)


#decorator for logging
def logging(func):
    def wrapper(a, b):
        print(f"Function '{func.__name__}' is being called.")
        func(a, b)
    return wrapper

@logging
def add(a, b):
    print(a+b)

@logging
def sub(a, b):
    print(a-b)

add(10,100)
sub(100,90)



#Class notes
def login_required(func):
    def wrapper():
        print("Checking if user is logged in...")
        func()
    return wrapper

@login_required
def view_profile():
    print("Ravi's profile opened.")

view_profile()

# Homework

'''1. **Create a Decorator to Log Calls**

   * Create a decorator called `log_function_call` that prints function name and when it was called.
   * Apply it to a function like `add()`.'''

def logging(func):
    def wrapper(a, b):
        print(f"Function '{func.__name__}' is being called.")
        func(a, b)
    return wrapper

@logging
def add(a, b):
    print(a+b)

@logging
def sub(a, b):
    print(a-b)

add(10,100)
sub(100,90)


'''2. **Create a Decorator That Times a Function**

   * Use `time` module to record how long a function takes to run.
   * Apply it to a `long_task()` function that sleeps for 2 seconds.'''


'''3. **Multiple Decorators**

   * Create two decorators: one adds `"==="` above and below output, another adds `>>>` before the output.
   * Apply both on a function that prints your name.'''
def startend(func):
    def  wrapper():
        print("======================")
        func()
        print("======================")
    return wrapper

@startend
def before(func):
    def wrapper():
        print(">>>>>>>>>>>>>")
        func()
    return wrapper

@before
def info():
    print("My name is Shashi")

info()


'''4. **Create a Decorator That Only Allows a Specific User**

   * Create a function `view_data(name)`
   * Decorator `allow_only(name)` should print “Access Denied” if the name is not `"admin"`'''