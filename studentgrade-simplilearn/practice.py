# name = input("Write your name : ")
# hobby = input("Write your hobby : ")
# print(f"So your name is {name} and your hobby is {hobby}")

# number = int(input("Enter the number : "))
# if number > 0 :
#     print("Positive")
# elif number < 0 :
#     print("Negative")
# else:
#     print("Zero")

# lists = ["Milk","Bread","Eggs"]
# print("I need to buy: ")
# for item in lists:
#     print(item)

# Create a Python dictionary that describes a movie. It must have a 'title' key and a 'director' key. 
# Then, write a line of code that prints only the director's name

# movies = {
#     "title" : "Jab We Met",
#     "director":  "Imtiaz Ali"
# }

# print(movies["director"])

#Create a list of strings with two of your favorite songs. 
# Then, write a single line of code that adds a third song to the end of that list.
#  Finally, print the entire updated list to see the result.

# my_favourite_songs = ['lover','daylight','blankspace']
# my_favourite_songs.append('cruel summer')
# print(my_favourite_songs)

# Create a list of strings containing three of your favorite cities. 
# Then, write a for loop that goes through this list and, for each city,
#  prints a full sentence like "I would love to visit Mumbai."
# cities = ['mumbai','pune','bengaluru']
# for city in cities :
#     print(f"I would love to visit {city}")

    # 1. Open the file in 'a' (append) mode.
# If log.txt doesn't exist, this will create it.
# If it does exist, it will get ready to write at the very end.
# with open("log.txt", "w") as file:
#     # 2. Write a new line. The '\n' is important to make sure
#     # the next entry starts on a fresh line.
#     file.write("A new log entry was added.\n")

# # 3. Print a success message to the user.
# print("Successfully added a new line to log.txt")

# Create a Python dictionary that represents a game character's stats. It should have keys like 'level' and 'strength'. 
# Then, write the code to save this entire dictionary to a file named character.json

# import json

# game_characters_stats = {

#     "char1" : {
#         "level" : "1",
#         "strength" : "great"
#     },

#     "char2" : {
#         "level" : "2",
#         "strength" : "average"

#     },
# }
# with open("character.json","w") as file :

#     json.dump(game_characters_stats,file,indent=4)

# print("characters added successfully")

# age = int(input("Enter your age : "))
# print(f"Your age is {age}")
# print function 
# print("Hello World")
# print('Single quotes')
# print('conca'+'tenation')
# print('hello','there')
# print('I am' ,5)
# # print('I am '+ 5) #String and Number cant be added 
# # print('I'm 5') #This will also give me error 
# print("I'm 5")
# print('He said "hi"')

#decimals are floats 
#four to the power of 2 (4**2)
# print(1+3)
# print(1-3)
# print(1*3)
# print(1/3)

#variables act as a placeholders
#variables can store all integers strings etc
#cant start a variable with number 

# exVar = 100
# print(exVar)

# opVar = exVar /5.3
# print(opVar)


#while loop 
#while something is the case while somethiing
#conditional 
# condition = 1
# while condition <= 10 :
#     print(condition)
#     condition += 1  #condition = condition +  1

# condition = 5
# while condition < 15 :
#     print('True')
#This will give infinite loop

# while True :
#     print('Infinite')

# exampleList = [1,6,7,3,6,9,0]
# #for loop to iterate through the list 
# for x in exampleList:
#     print(x)

# for x in range(1,1000):   #generator range()
#     print(x) 

# if statement 
# if something does something then it is true 
# x = 2 
# y =7 
# z = 10

# if x > y:
#     print(x, 'is greater than ',y)

# if x < y:
#     print(x,'is less than ', y)

# if x == y :
#     print(x,'is the same as ',y)

# # if x == '2' :        #cannot do this 
# #     print(x,'is the same as ',y)

# if z > y > x :
#     print(z,'is greater than',y,'which is greater than ',x)

# x = 3
# y = 6
# if x<y:
#     print(x,'is less than',y)
# if x > y:
#     print(x,'is greater than',y)
# else:
#     print(x,'is not less than',y)


 #if elif else
# x = 3
# y = 7
# z = 10
# if x > y :
#     print(x,'is greater than ',y)
# elif x < z:
#     print(x,'is less than',z)
# elif y > z:
#     print(y,'is greater than',z)
# else:
#     print('nothing was the case')

#functions a bit of code to a single word 
#define a function by def 

# def example():
#     x = 1
#     y = 3
#     print(x+y)

#     if x < y :
#         print(x,'is less than',y)
# def main():
#     example() 

# def addition(num1 , num2):
#     answer = num1 + num2
#     return answer

# x = addition(5,6)
# print(x)


# def website(font, background_color, font_size, font_color):
#     print('font', font)
#     print('bg', background_color)
#     print('Font Size', font_size)
#     print('Font color', font_color)

# # Calling the function
# website('TNR', 'white', '11', 'black')

# This code demonstrates the intended use of the functions and variables.

# --- Global and Local Variables Explained ---

# 'x' is a GLOBAL VARIABLE because it is defined outside of any function.
# It can be accessed (read) from anywhere in the script.
# x = 6

# # This function modifies the global variable 'x'.
# def example3():
#     # The 'global' keyword tells Python we want to MODIFY the global 'x',
#     # not create a new local variable named 'x'.
#     global x 
#     x += 1
#     print(f"Inside example3(), global x is now: {x}")

# # This function demonstrates a LOCAL VARIABLE.
# def example():
#     # 'z' is a LOCAL VARIABLE. It only exists inside this 'example' function.
#     # It is created when the function is called and destroyed when it finishes.
#     z = 5
#     print(f"Inside example(), local z is: {z}")

# # This function reads a global variable and uses local variables.
# def example2():
#     # 'z' and 'y' are LOCAL VARIABLES, specific to this 'example2' function.
#     # A different function (like example()) can have its own 'z' without conflict.
#     z = 7
#     print(f"Inside example2(), local z is: {z}")
    
#     # Python looks for a local 'x', doesn't find one, so it reads the global 'x' (value: 6).
#     y = x + 1
#     print(f"Inside example2(), local y calculated using global x is: {y}")
#     return y 

# # --- Calling the Functions to See the Output ---

# print(f"Initial global x value: {x}")

# # Call example() to see its local variable.
# example()

# # Call example2(). It reads the global 'x' and returns a new value.
# # We store the returned value in a new variable.
# returned_value = example2()
# print(f"example2() returned: {returned_value}")

# # The value of global 'x' has not changed yet.
# print(f"Global x value after calling example2(): {x}")

# # Call example3() which explicitly modifies the global 'x'.
# example3()

# # The value of global 'x' has now been changed.
# print(f"Final global x value after example3(): {x}")


#Python common errors
#nameerror
#varaible =55
# print(varaible)

#Expect an indent 
#def func1():
#def func2():
    # print(2)

#Unexpected Indent:
# def task():
#     print('1')
# print('2')
#    print('3')

#Working with files and classes
#writing to a file
# WriteMe = 'Example text'

# saveFile = open('exampleWrite.txt','w')
# saveFile.write(WriteMe)
# saveFile.close()

#appending to a file (addding to the end of a file )
# appendMe = 'Some text'
# saveFile = open('exampleFile.txt','a')
# saveFile.write(appendMe)
# saveFile.close()

#Reading from a file 
# readMe = open('exampleFile.txt','r').read()
# print(readMe)

# splitMe = readMe.split('\n')
# print(splitMe)

#readMe2 = open('exampleFile.txt','r').readlines()
# print(readMe2)

#classes in python 
# class calc:
#     def add(x,y):
#         answer = x+y
#         print(answer)
#     def add(x,y):
#         answer = x-y
#         print(answer)
#     def add(x,y):
#         answer = x*y
#         print(answer)
#     def add(x,y):
#         answer = x/y
#         print(answer)


#input and statistics 
#input from users 
# name = input("What is your name : ")
# print('Hello',name)
# import statistics
# exList = [5,3,2,9,7,4,3,1,8,9]

# x = statistics.mean(exList)
# print(x)

# x = statistics.median(exList)
# print(x)

# x = statistics.mode(exList)
# print(x)

# x = statistics.stdev(exList)
# print(x)

# x = statistics.variance(exList)
# print(x)


#import syntax 
# import statistics as s 
# exList = [5,3,2,9,7,4,3,1,8,9]
# print(s.mean(exList))

# from statistics import mean
# exList = [5,3,2,9,7,4,3,1,8,9]
# print(mean(exList))

# from statistics import mean as m
# exList = [5,3,2,9,7,4,3,1,8,9]
# print(m(exList))

# from statistics import mean , stdev
# exList = [5,3,2,9,7,4,3,1,8,9]
# print(mean(exList))
# print(stdev(exList))

# from statistics import mean as m , stdev as s 
# exList = [5,3,2,9,7,4,3,1,8,9]
# print(m(exList))
# print(s(exList))

# from statistics import *
# exList = [5,3,2,9,7,4,3,1,8,9]
# print(m(exList))
# print(s(exList))


# making modules
# File: practice.py
# File: exampleModule.py

# File: practice.py

# File: practice.py
# This file imports the other file and uses its contents.

# # 1. Import the 'module.py' file
# import module

# # 2. Call the function that lives inside the module
# module.exampleFunc('This is the correct way!')

# Lists vs Tuples 
# tuple is immutable is that you cannot change it 
# def example():
#     return 15,19

# a,b = example()
# print(a)
# print(b)

# x = [2,4,3,5,4,6,5,7]
# print(x)
# x.append(12)
# print(x)
# x.insert(0,12)
# x.remove(12)
# print(x)
# print(x.index(4))
# print(x.count(3))
# x.sort()
# print(x)

# x = ["Seeta","Geeta","Reeta","Meeta"]
# x.sort()
# print(x)

# x.reverse()
# print(x)

#dictionaries 
# gradeDict = {
#     "Seeta": 89,
#     "Geeta":95,
#     "Reeta":80
# }
# print(gradeDict)
# print(gradeDict["Geeta"])
# gradeDict["Geeta"] = 98
# print(gradeDict["Geeta"])
    