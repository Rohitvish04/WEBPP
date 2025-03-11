#-------- Set ------ 
#FrozenSet: immutable
#squence, duplicate not allowed, unordered

# Sets are used to store multiple items in a single variable
# add(element): Adds an element to the set.
# remove(element): Removes an element from the set. Raises a KeyError if the element is not present.
# discard(element): Removes an element from the set if it is present. Does nothing if the element is not present.
# pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
# clear(): Removes all elements from the set. 

# syntax()
grade = {1,2,3,4,5}
# print(grade)

#set()
no= [1,2,3,4,5,6,7,8,1,2,3,4,5,]
st = set(no)
# print(st)

#methods : CRUD
st.add(100)

st.remove(4)

st.discard(4)

st.pop()
# print(st)

# accessing

# operations: union | -combine, inseterion- &, difference - - 
# print(st)
# print(grade)
# print(st | grade)
# print( st & grade)
# print( st - grade)

# #membership - 
# print(3 in st)
# print(3 not in st)

 # Frozenst: no duplicates, unordered, immutable

fs = frozenset([1,2,3,4,5,6,7,8,9])
# print(type(fs))

# fs.add(100)
# print(fs)

# union - combine, insertion , difference
print(st)
print(fs)
print(fs | st)  # combine
print(fs & st)
print(fs - st)