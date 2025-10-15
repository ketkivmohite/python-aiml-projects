#functions
def fun():
    print("Welcome to GFG")

def fun():
    print("Welcome to GFG")
    
fun() # Driver code to call a function

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

#types of functions 
#default arguments 
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

#keyword arguments 
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

#positional arguments 
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

#arbitary arguments 
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')

#nested functions 
def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
f1()

#anonymous function 
def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))

#return statement 
def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(square_value(2))
print(square_value(-4))

#pass by reference and pass by value 
# Function modifies the first element of list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified

#recursive functions 
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))

#pass statement in functions 
def fun():
    pass

fun() # Call the function

#conditional statement 
x = 10

if x > 5:
    pass  # Placeholder for future logic
else:
    print("x is 5 or less")

#pass statement in loops 
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(i)

#pass statement in classes 
class EmptyClass:
    pass  # No methods or attributes yet

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        pass  # Placeholder for greet method

# Creating an instance of the class
p = Person("Emily", 30)

#Local variables 
def greet():
    msg = "Hello from inside the function!"
    print(msg)

greet()

#global variable 
msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)

#use of local and global variable 
def fun():
    s = "Me too."
    print(s)

s = "I love Geeksforgeeks"
fun()   
print(s)

#modifying global variables inside a function 
def fun():
    s += ' GFG'   # Error: Python thinks s is local
    print(s)

s = "I love GeeksforGeeks"
fun()