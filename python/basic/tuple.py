# Tuple: sequence, immutable, ordered

detail = (1, "Juveriya", "WEPP", "Delhi")
print(type(detail))

# operation
print(detail + (True, 156,34))

#indexing and slicing
print(detail[1])
print(detail[1:3])

#methods
print(detail.count(1))
print(detail.index(1))

# packing
print(detail)

age, name, course, place =detail
