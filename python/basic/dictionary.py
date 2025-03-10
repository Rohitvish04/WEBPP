#   ------- dictionary ------
# A Python dictionary is a data structure that consists of key-value pairs
# Python dictionaries have several built-in methods for manipulation,
# including keys(), values(), items(), get(), update(), pop(), popitem(), copy(), clear(), and setdefault()
#   key - value
# Syntax - { }

details = {
    "id": 1,
    "name": "Aditya",
    "eligibility": True,
    "height": 188.7,
    "Gender": 'M'
}

details = {
    "Name": ["Aditya", "shivam", "Nilesh","Shekhar"],
    "id": [1,2,3,4]
}
print(details)

# Iteration: keys(), items(), values()
 
for key in info.keys():
    print(key)

for val in info.values():
    print(val)

for key, val in info.items():
    print(key,val)
    
     

info= dict(name = "Aditya", contact= 987623349, gender= 'M' )
print(info)

#--------*methods*--------
#----- accessing---------

# -----------get(key)-----------
# print(info.get("contact"))
# print(info.get("address", "Not available"))

# # 
# print(info.items())
# print(info.keys())
# print(info.values())

# pop(key) :
# Removes the element with the specified key and returns its value
print(info.pop('gender'))
print(info.pop("addess","key not available"))
print(info)

#   --- popitems()-	
# Removes and returns the last inserted key-value pair (as a tuple)
print(info.popitem())
print(info)

# update(other_dict)
# Updates the dictionary with the key-value pairs from another dictionary
info.update({"Address": "Mumabi- Maharashtra"})
print(info)

info['name'] = 'Rohit'

info['User-Name'] = info.pop("name")

print(info)

# create nested dictionary
inform = {
    "personal": {
        'first_name': 'Rohit',
        'last_name': 'Vishwakarma',
    },
    "education": {
        'SSC': '10th pass',
        'HSC': '12th pass',
        'graduation': 'BSC IT'
    }
}
        