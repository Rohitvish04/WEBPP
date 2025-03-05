 #String

para = 'hello my name is rohit'


#accessing element/har from str - indexing

#for single char
print(para[10])
print(para[-11])

#for range of char
print(para[ :13])
print(para[9: ])
print(para[-10:])

#for range with steps str[starInd : endIndex: steps]
print(para[0:10:2])

# reverse your Stirng
print(para[::-1])

#operation
# print(para + para) #concatenation
# print(para - 1) 
#print(para * 2) #repeatention
#print(para/2)

name = 'NeeRaJ cHaudHaRY'

# cases - 
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.swapcase())


print('----------------------')

# To check type of content
para = "Python12345678Programming"
print(para.isalpha()) 
print(para.isalnum())   # alpha + num = alnum
print("1234567890".isdigit())
print("      ".isspace())


#Find :
# para = "The pyhton Hello python my name is python"

# print(para.find('python')) # 1st occurence
# print(para.rfind('pyhton'))  # Last occurence
# print(para.find('Rohit'))  #-1 not present in para
# print(para.index('The'))  
# print(para.replace('python', 'Rohit')) #


#Trimming :
# para = "   Hello, my name is   rohit  "
# print(para)
# print(para.strip())  #Leading space remove
# print(para.lstrip()) #left side space remove
# print(para.rstrip()) #right side space remove

# starts ande ends
# para = "the Hello ,I am robot"
# print(para.startswith('The'))
# print(para.endswitch('robot'))

# splitting
para = 'Hello welocme to the pyhton sesssion hope you are enjoying'
splitted =  para.split() # convert str into a list
print(splitted)

 
# rsplit = para.rsplit(',',1)   # (sep, max) sep - ,
# print(rsplit)

#iterable - join(List[]) : str.join(list)
# names = ['harshit', 'shivam' , 'nikal']
# val = "Hello".join(names)
# print(val)

 
