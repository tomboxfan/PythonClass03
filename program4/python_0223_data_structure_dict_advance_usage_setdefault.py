names = ['Ringo', 'Paul', 'John', "Ringo", 'Ringo', 'John']

'''
Requirement: 
I have a list of names. I want to know how many times each name appears.
'''


# Step 1) I create an empty dict, so that I can remember how many times each name appears.
count = {}

# Step 2) I loop list names

for name in names:

    # Solution 1) traditional way ---------------------------
    # if name not in count:
    #     count[name] = 0

    # Solution 2) new way ---------------------------
    count.setdefault(name, 0)

    count[name] += 1


print(count)


'''
IMPORTANCE!!! ------------------------------------------
count.setdefault(name, 0) will insert key / value pair (name, 0) ONLY IF key name doesn't exist in dict count. 
--------------------------------------------------------
'''
