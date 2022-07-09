dict1 = {'A': 80, 'B': 85}
dict2 = {'B': 90, 'C': 95}

'''
Requirement:
I have 2 dict - dict1 & dict2.
I want to merge dict2 into dict1, then dict1 and dict2 becomes 1 dict.
Possibly, some key / value pair in dict2 will override those in dict1
'''

print("Original dict1: ")
print(dict1)

# Solution 1 ----------------------
# for key, value in dict2.items():
#     dict1[key] = value


# Solution 2 ---------------------
dict1.update(dict2)



print("Updated dict1: ")
print(dict1)