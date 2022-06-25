# This doesn't work! -----------
# a_list = []
# a_list[4] = 'Tom' # IndexError: list assignment index out of range
# I try to assign the string 'Tom' to position 4 in an empty list
# clearly impossible, because the position 4 does not exist!

# This is ok! ------------------
a_list = [None] * 5
a_list[4] = 'Tom'
print(a_list)


a_dict = {}
a_dict[4] = 'Tom'
print(a_dict)

'''
IMPORTANCE!!! -------------------------------
4 in list is index; list is ordered by index. 
4 in dict is key. 
---------------------------------------------
'''

print(f"Does value 'Tom' exist in a_list? {'Tom' in a_list}")
print(f"Does value '4' exist in a_dict? {'4' in a_dict}")

'''
HOMEWORK:
Why the 2nd one print 'False? How to change the code to make it print 'True'? 
'''