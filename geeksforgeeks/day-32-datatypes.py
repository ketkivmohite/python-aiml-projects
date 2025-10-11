x = 50 #int
x = 60.5 #float
x = "Hello World" #string
x = ["geeks","for","geeks"] #list
x = ("geeks","for","geeks") #tuple

a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

s = "welcome to geeks world"
print(s)

print(type(a))
print(s[1])
print(s[2])
print(s[-1])

#list data types 
a = []
a = [1,2,3]
print(a)

b = ["Geeks","for","Geeks",4,5]
print(b)

a = ["Geeks","for","Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])

#tuple data type
tup1 = ()
tup2 = ('Geeks','For')
print("\n Tuple with the use of string: ",tup2)

#access tuple items
tup1 = tuple([1,2,3,4,5])
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

#boolean data type 
print(type(True))
print(type(False))
#print(type(true))

#set data type 
#initializing empty set
s1 = set()

s1 = set("Geeks For Geeks")
print("Set with the use of string: ",s1)

s2 = set(["Geeks","For","Geeks"])
print("Set with the use of list: ",s2)

#access set items 
set1 = set(["Geeks","For","Geeks"]) #duplicates are removed automatically
print(set1)

for i in set1:
    print(i, end="")#prints elements one by one

print("Geeks" in set1)

# initialize empty dictionary
d = {}

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))

#Arithmetic operators 
# Variables
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)

#Relational or Comparison operators
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#Logical AND OR NOT Operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#Bitwise operators
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#Assignment Operators 
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

#Identity Operators
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

#Membership operators 
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


#Ternary Operator 
a, b = 10, 20
min = a if a < b else b

print(min)

#Operator Precedence 
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

#Operator Associativity
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)

age = 20
if age >= 18:
    print("Eligible to vote.")

age = 19
if age > 18: print("Eligible to Vote.")

age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")

#check if the user is eligible to vote 
age = int(input("Enter your age : "))
if age>=18:
    print("You are eligible to vote.")

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")

print(10 % 3)
