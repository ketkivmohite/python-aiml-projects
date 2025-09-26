# Your Task: Write a small Python script that does three things:

# Asks the user for their name and stores it in a variable.

# Asks the user for their favorite color and stores it in another variable.

# Prints a single sentence using an f-string that says, "Hello, [Name]! Your favorite color is [Color]."

# name = input("Enter your name : ")
# color = input("Enter your favourite color: ")
# print(f"Hello,{name} ! Your favourite color is {color}")

# Your Task: Write a small Python script that does three things:

# Asks the user for their age.

# Converts the input into an integer.

# Prints one of two messages:

# If the age is 18 or greater, it should print "You are old enough to vote."

# Otherwise (if the age is less than 18), it should print "You are not old enough to vote yet."

# The Hint: You can combine the int() and input() functions on one line to make your code shorter.
#  You'll need an if/else block and the greater than or equal to operator (>=)

# age = int(input("Enter your age : "))
# if age >= 18 :
#     print("You can vote .")
# else:
#     print("You are not old enough to vote yet.")

# This challenge will test your ability to work with a collection of items using lists and for loops.

# Your Task: Write a small Python script that does two things:

# Creates a list of strings containing three of your favorite fruits.

# Uses a for loop to print each fruit from the list on its own, separate line.

# The Hint: Remember the "conveyor belt" analogy. The for loop gives you a temporary variable that 
# holds one item from the list at a time. Your print() statement will be inside the loop.

# fruits = ["mango","litchi","banana"]

# for fruit in fruits:
#     print(fruit)

# This challenge will test your ability to work with dictionaries to store and retrieve structured data.

# Your Task: Write a small Python script that does two things:

# Creates a single dictionary to represent a user profile. The dictionary must have three keys: "name", "job", and "city".

# Uses f-strings to print a single, formatted sentence that introduces the user, like: "Meet [Name], who works as a [Job] in [City]."

# The Hint: To get a value from a dictionary, you use its key inside square brackets [].
# You can put this my_dict['key'] syntax directly inside the curly braces of an f-string!

# my_dict = {
#     "name":"Ketki",
#     "job":"Python - dev ",
#     "city":"Mumbai"
# }
# print(f"Meet {my_dict['name']} , who works as a {my_dict['job']} in {my_dict['city']}")

# Your Task: Write a small Python script that does three things:

# Defines a function called create_greeting. This function should take one argument (a name).

# Inside the function, it should return a greeting string, like "Hello and welcome, [Name]!".

# Outside the function, call your create_greeting function with your own name and print the result.

# The Hint: Remember the syntax for defining a function: def function_name(argument):. 
# The return keyword is used inside a function to send a value back out.

# def create_greeting(name):
#     print(f"Hello and welcome {name}")

# create_greeting("Ketki")

# my_tuple = (20,30,40)
# print(my_tuple)
# my_tuple[0] = 15


# my_numbers = [1,2,3,4,2,5,1,3,6]
# my_numbers_new = set(my_numbers)
# print(my_numbers_new)


# my_numbers = [1,2,5,2,4,5,1]
# my_set = set(my_numbers)
# print(my_set)


# Create a list of numbers in a random order, for example: my_numbers = [40, 10, 50, 20, 30]

# Use the .sort() method to sort the list.

# Print the list to show that it is now sorted.

# Next, use the .reverse() method on the now-sorted list.

# Print the list again to show that it is now in descending order.

# The Hint: Remember that these methods are "in-place," just like .append(). You call them directly on your list 
# (e.g., my_list.sort()), and they change the list automatically. You don't need to assign the result to a new variable.

# my_nos = [40,10,50,20,30]
# print(f"Original List: {my_nos} ")

# my_nos.sort()
# print(f"Sorted List: {my_nos}")

# my_nos.reverse()
# print(f"Reversed List: {my_nos}")


# def calc_sum(a , b):
#     return a+b

# sum = calc_sum(2,3)
# print(sum)

#average of 3 nos 


# def calc_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)

# calc_avg(1,2,3)

#input two  numbers and print their sum 
# a = int(input("Enter  a : "))
# b = int(input("Enter  b : "))
# print(a + b)

#WAP to input side of a square and print its area 
# a = int(input("Enter the side of a square: "))
# square = a * a
# print("The square of an area is : ", square)

#WAP to input two floating nos and print their average 
# a = float(input("Enter 1st Number : "))
# b = float(input("Enter 2nd Number: "))
# sum = a + b 
# avg = sum / 2 
# print(avg)

#WAP to input 2 int numbers a and b print true if a is greater than or qual to b . if not print false 
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# if a >= b :
#     print("True")
# else:
#     print("False")

#WAP to check if the user entered a odd no or even 
# number = int(input("Enter a number: "))
# if number % 2 == 0 :
#     print("Even number.")
# else:
#     print("Odd")

#WAP to find the greatest of 3 nos entered by the user 
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))
# if a >= b and a >= c :
#     print(a,"a is greater")
# elif b>=a and b>=c :
#     print(b," b is greater")
# else :
#     print(c,"c is greater") 


#WAP to find the greatest of 4 nos entered by the user 
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))
# d = int(input("Enter d : "))

# if a>=b and a>=c and a>=d:
#     print("1st number is the largest")
# elif b>=c and b>=a and b>=d:
#     print("2nd number is the largest")
# elif c>=a and c>=d and c>=b :
#     print("3rd number is the largest")
# else:
#     print("4th number is the largest ")

#WAP to check if a number is a multiple of 7 or not 
# number = int(input("Enter a number: "))
# if number % 7 == 0 :
#     print("Multiple of 7 ")
# else:
#     print("Not a multiple of 7")

#WAP to ask the user to enter names of their fav 3movies and tore it in a list 
# print("Enter your fav 3 movies")
# movie1 = input("Enter 1st movie : ")
# movie2 = input("Enter 2nd movie : ")
# movie3 = input("Enter 3rd movie : ")
# movies_list = [movie1,movie2,movie3]
# print(movies_list)

#WAP to check if a list contains a palindrome of elements 
# numbers = [1,2,1]

# copy_numbers = numbers.copy()
# copy_numbers.reverse()
# if copy_numbers == numbers :
#     print("palindrome")
# else:
#     print("not a palindrome")

#WAP to count the number of students with the "A" grade in the following tuple .

# grades = ("C","D","A","A","B","B","A")
# print(grades.count("B"))

#WAP to store the same tuple above as a list and sort the list 
# grades = ["C","D","A","A","B","B","A"]
# grades.sort()
# print(grades)

#Store the following word meanings in a dictionary 
# my_dict = {
#     "table" : ("a piece of furniture" , "lists of facts and figues"),
#     "cat": "a small animal"

# }

# print(my_dict)
#count the number of items in a set 
# subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
# print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary . 
#Start with an empty dictionary and add one by one . 
#use subject name as key and marks as value 
# marks = {}

# x = int(input("enter phy : "))
# marks.update({"phy" : x})

# x = int(input("enter chem : "))
# marks.update({"chem" : x})

# x = int(input("enter math : "))
# marks.update({"math" : x})

# print(marks)

#class = blueprint 
# class cat :
#     def __init__(self,name,age,favourite_activity):
#         self.name = name 
#         self.age = age
#         self.favourite_activity = favourite_activity

#     def greet(self):
#         print(f"Meow! I'm {self.name} and I have to {self.favourite_activity}.")

# marble = cat("Marble",2,"nap")
# cookie = cat("cookie",4,"chase toys")
# whiskers = cat("whiskers",3,"greet visitors")

# marble.greet()
# cookie.greet()

#Create a class called Book that stores the title and author of a book. 
# Add a method called display_info that prints out the book's title and author in a nice format. 
# Then, create two objects of the Book class with different titles and authors, and call the display_info method for each object.

# Hint:

# Your class should have an __init__ method to set the title and author.

# The display_info method should use self.title and self.author.

# After creating your objects, use object_name.display_info() to call the method.

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def book(self):
#         print(f"The book title is {self.title} and the author is {self.author}")

# # Create objects outside the class definition
# chanakyaneeti = Book("chanakyaneeti", "chanakya")
# atomichabits = Book("atomichabits", "james clear")

# # Call the method using objects
# chanakyaneeti.book()
# atomichabits.book()

# class Animals:
#     def __init__(self,type,age,make_sounds):
#         self.type = type
#         self.age = age
#         self.make_sounds = make_sounds
#     def animals(self):
#         print(f"The animal is {self.type} it is {self.age} and it makes the sound {self.make_sounds}")

# dog = Animals("dog",2,"woof")
# cat = Animals("cat",3,"meow")

# dog.animals()
# cat.animals()

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def fullname(self):
#         print(f"My name is {self.firstname} {self.lastname}")

# class Student(Person):
#     def __init__(self, firstname, lastname,graduationyear):
#         super().__init__(firstname, lastname)
#         self.graduationyear = graduationyear 

#     def welcome(self):
#         print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")

# student1 = Student("Ketki", "Mohite", 2025)
# student1.fullname()
# student1.welcome()

# class Vehicle :
#     def __init__(self,brand):
#         self.brand = brand 

#     def start(self):
#         print("Vehicle Started ")

# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model 
#     def start(Self):
#         print(f"Car Started {Self.brand} {Self.model}")

    
# my_car = Car("Tata","Altroz")
# my_car.start()
# print(my_car.brand)

