#loops 
n = 4
for i in range(0, n):
    print(i)

li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x)
#iterating by index of sequences 
li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])

#while loop 
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")

# #nested loops 
# from __future__ import print_function
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()

#continue
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

#break statement 
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)

for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

#print each item in a shopping list 

items = input("Enter shopping items separated by commas: ").split(',')

for item in items:
    print("Buy:", item.strip())

#print squares of numbers from 1 to n 
n = int(input("Enter a number : "))
for i in range(1,n+1):
    print("Square of",i,"is",i**2)

#while loop countdown timer 
seconds = int(input("Enter countdown time in seconds: "))
while seconds > 0:
    print("Time left: ",seconds)
    seconds -=1

#sum until users enters 0 (while loop)
total = 0 
num = int(input("Enter number(0 to stop): "))
while num !=0:
    total += num 
    num = int(input("Enter number(0 to stop): "))
print("Total sum: ",total)

#nested for loops 
#print a multiplication table
n = 3
for i in range(1,n+1):
    for j in range(1,11):
        print(i*j,ends='')
    print()

#print identity matrix
n = 4

for i in range(n):
    for j in range(n):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()  # move to the next row


#control flow atatements
# 1. break 
#stop printing at a target item 
items = ["apple", "banana", "cherry", "stop", "mango"]

for item in items:
    if item == "stop":
        break
    print("Item:", item)

#find first even number 
while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("First even number found:", num)
        break

# 2. continue
items = ["milk", "bread", "out of stock", "eggs"]

for item in items:
    if item == "out of stock":
        continue
    print("Buy:", item)

#skip even numbers 
n = 10

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

#pass 
#use passs for future implementation
tasks = ["email", "meeting", "call"]

for task in tasks:
    if task == "call":
        pass  # Logic to be added later
    print("Do:", task)

#pass in empty loop for now
for i in range(5):
    pass  # Placeholder for future logic 

