#statement: command
# 1) assignment statement:
age = 21
course = "python"

# 2) print statement: output
print(age)

# 3) Expression statement:
a = 2
b = 6
result = a + b

#4) Input statement:

#string
name = input("Enter your Name: ")
print(type (name))

#integer
age = input("Enter your age: " )
print(type (age))


# 5) Conditional statement: if else
voting_age = 18
if (voting_age >= 18):
    print("You are eligible for voting!!")
else:
    print("You are not eligible for voting!!")

#elif: multiple options
#Number guessing game
num =  int(input("Enter your number: "))
if num == 0:
    print("Your number is zero")
elif num > 0:
    print("Your number is postivie!!")
elif num < 0:
    print("Your numbe ris Negative!!")
else:
    print("Please Enter your number")

# Ternary operator:
result = "You are eligible for voting!!" if (voting_age >= 18) else "NOT eligible"
print(result)

# 6)Comments:
# Single - #
'''
Multiline comments
sadfa
ada
'''