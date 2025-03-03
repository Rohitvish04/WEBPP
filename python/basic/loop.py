#Loops: repeatitive, repeatition of pattern
# 1) For loop- limit
# range(starting no, ending no)
# for item in range(1,50):
#     print(item)

#Write a multiplication table of 5
# for item in range(20):
#     item*=5
# #     print(item)
# num = 5
# for i in range(1,11):
#     print(f" {num} x {i} = {num*i}")

#write to print even numbeer
# for i in range(1,21,3):
#      print(i)

#sum all the odd numbers from 1 to 100
# sum =0
# for i in range(1,101,2):
#     sum+=i
# print(sum)
    
#WAP to print squares from  1 to 20
# for i in range(1,21):
#     print(i**2)
    
#WAP to print your name using for loop
# name= ['R','O','H','I','T']
# for i in name:
#     print(i)

# while loop - entry

# while loop - entry control loop

#while condition:
    #loop /pattern
    #increment/decrement

num = 1
while num<=10:
    print(num*5)
    num+=1

num=2
while num<=100:
    print(num)
    num+=2

num=1
while num<=20:
    print(num**2)
    num+=1

name='Rohit'
i=0
while i<len(name):
    print(name[i])
    i+=1
