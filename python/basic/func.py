#method - block of code

#funcName() calling method
#parameters
def hello(name , age):
    return f"Hello {name} and my age is {age}"

hello('rohit',21) #arguments

#define a method which prints your name, the course you are pursuing
def myCourse(name, courseName):
    return f"Hello {name} and my course is {courseName}"

myCourse('rohit', 'web dev with python')
# deine a method to perform add, subtract
def add(num1,num2):
    return num1+num2
add(12,3)

def subtract(num1,num2):
    return num1-num2
subtract(12,3)

# Pre-define

import math

print(math.sqrt(625))
print(math.floor(290.10))

import string
# A-Z , a-z , 0-9, special cases
print(string.ascii_letters)
print(string.digits)
