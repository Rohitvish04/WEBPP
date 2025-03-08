    # Data structure:
print(len("String"))

# name1= 'Rutika'
# name2 = 'Shabbir'
# name3 = 'Nilesh'

# ------------List-----------------
names = ['rutika', 'Shabbir', 'Nilesh', 'Udhav']
print(names)

#------------diff types--------
names = ['Rutika', 1 , True, 9.45, 'sa']
print(names)

no = [1,2,3,4,5]
print(no)

#------------list of list---------
names = ['Rutika', 'Shabbir', 'Nilesh', 'Udhav']
no = [1,2,3,4,5]

lists = [names, no]
print(lists)

#-------------lsit operation ----------
no = [1,2,3,4,5] + [5,6,6,7,8,9]
print(no)

no =[1,2,2,3] * 2
print(no)


# # accessing element from List
# no = [1, 2,3, 4,5 ]
# print(no[-1])
# print(no[2:4])
# print(no[::2])

#updating elements in a list
no[0] = 100
print(no)

#------------List methods:-------------
# no = [1, 2, 3, 4,5]
# no.append(200)

# --------insert(index , newvalue)---
no.insert(1, 1000)

#-------------to merger 2 List---------
no.extend([101,102,103])
# print(no)

# # ----reomve--------
# no.remove(200)
# print(no)

# ----------pop----------- 
no.pop(1) # index as param
print(no)

# -------index----
print(no.index(4))

no.insert(0,2)
#count
print(no)
print(no.count(2))

#----------- sort ---------
no.sort()  #asce
print(no)

#reverse()
no.reverse() # desc
print(no)

# sorted method returns a sorted copy of the list, without changing the original list.
list1 = sorted(no, reverse = True)
print(list1)

# copy
newList = no.copy()
print(newList)

#Iteration
print(no)

for i in no:
    print(i)

for i in range(len(no)):
    print(i)

------------*List comprehension*-----------------

for i in range(1,11):
    if i%2 ==0:
        print("even")
    else:
        print("odd")
        
# 1 t0 10
num = [i for i in range(1,11)]
print(num)

# square from 1 to 100 : i **2
square = [i**2 for i in range(1, 21)]
print(square)

# multiple of 2
multiple =  [i*2 for i in range(1, 21)]
print(multiple)

