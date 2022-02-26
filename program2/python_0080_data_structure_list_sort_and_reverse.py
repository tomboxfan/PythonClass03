scores = [80, 90, 70, 60]

'''
----------------------
sort a list
----------------------
'''

# Solution 1: built-in function: sorted(a_list)
sorted_scores = sorted(scores)
print(sorted_scores) # [60, 70, 80, 90]
print(scores) # [80, 90, 70, 60] The scores list is NOT changed!

sorted_scores = sorted(scores, reverse=True) # an extra reverse param allows you to sort the list in descending order.
print(sorted_scores)


# Solution 2: method sort()
scores.sort()
print(scores) # [60, 70, 80, 90]

'''
IMPORTANCE!! ------------------------------------------------------------------------------------------------
built-in function: sorted(my_list)     create a NEW list with my_list's sorted value, my_list is NOT changed!
my_list.sort()                         sort the values in my_list, my_list is changed.
-------------------------------------------------------------------------------------------------------------
'''

print('-------------------------------------')

'''
----------------------
Reverse a list
----------------------
'''

scores = [80, 90, 70, 60]
scores.reverse()
print(scores)