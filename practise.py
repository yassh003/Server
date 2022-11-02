from platform import python_branch
from xml.dom.pulldom import START_DOCUMENT


print("Yashraj Vijayan")

# Single line Comment
"""
Author : Yash
Role : Student
EmpId : 0001
Description : Multiline Comment
"""
a=1
print(a)
b = "Hello World"
c=5.7
print(b)
print(a,b)

#Type of Function to check the data type
print(type(a))
print(type(b))
print(type(c))

#Contactionation
print("The output is "+str(a)) # Concat of Str with int is not allowed in python

#Type Casting
print("The output is"+str(a))

#Not allowed in Python
#1a = 3
#First-name = "Jhon Smith"
#FIRST NAME = space is not aloowed

#Multiple Variable Assignment
a = b = c = "Avengers"
print(c)

a,b,c = "Avengers: Infinty War","Avengers: Endgame","Avengers: Kang Dynasty"
print(b)

#python strings
s = "HelloWorld"
print(s[0:3])
print(s[:3])
print(s[3:])
print(s.upper())
print(s.lower())
print(a.replace('A','Re'))

#Python operators
a = 4
b = 10
c = 15
print(a + b)
print(b - a)
print(a * b)
print(a % b)

print(b > a)
print(b ** a) #exponential operator 10 to power 4

print(a > c and b > c)
print(a > c or c > b)

#list
l = ["iPhone","Samsung","Realme"]
print(l[0]) # first element from list
print(l[-1]) # last element from the list

for i in l:
    print(i)

l[2] = 'oppo' # Update values in the list

print(l)

l.append("One Plus")
print(l)

l.insert(2,'Pixel')
print(l)

l.remove("oppo")
print(l)

#print first 10 numbers using for loop
for n in range(1,11):
    print(n)

for c in "VVCE":
    print(c)

def helloworld():
    print("Hello World")

helloworld()

def add(a,b):
    return a + b

print(add(10,6))

def add(*a): # arbitrary arguements
    return a[0] + a[2]

print(add(1,5,7))

import datetime

todaydate = datetime.datetime.now()
print(todaydate.year)
print(todaydate)