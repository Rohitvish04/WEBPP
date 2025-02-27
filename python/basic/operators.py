#operators: +, -, *, / , %
#operands : 
num1 = 12
num2 = 13
sum = num1 + num2
multiple = num1 - num2
divided = num1 / num2
print(sum,multiple, divided)

#Logical operator : and , or , not - negation

value1 = False
value2 = False

print(value1 and value2)  # F v F = T
print(value1 or value2)  # 
print(not value2) 

#Assignment operator: = , +=, -=, *=, /=, %= , //= ->augmented , **=

a =10
b =True
name ='python'

c = 5 
a+=c
print(a)

b -=1
print(b)

name *= 3
print(name) 

a /= 2
print(a)

b %= 1
print(b)

print(130 / 3)
print(130 // 3)
a //= 2
print(a)

a**= 2
print(a)

#Memebership operator: in , not in  a-z , A-Z
name = 'Rohit Vishwakarma'
print('R' in name) #True
print('v' in name) #False

#Identity operator: is, is not
lst = ['Rohit', 'Princy', 'Juvera']
name = [1,2,3]

print(name is lst)
print(name is not lst)