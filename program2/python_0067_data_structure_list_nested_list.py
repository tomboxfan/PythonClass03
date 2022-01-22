'''
IMPORTANCE!!! --------------------------------------------------------------------------------
list can be nested, when you put a list inside another list, you get a nested list
----------------------------------------------------------------------------------------------
'''

x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x) # ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']


# Requirement 1: print
# a g j

# Requirement 2: print
# ['bb', ['ccc', 'ddd'], 'ee', 'ff']

# Requirement 3: print
# 'bb'

# Requirement 4: print
# ['ccc', 'ddd']

# Requirement 5: print
# 'ddd'

# Requirement 6: print
# 'ee'

# Requirement 7: print
# 'ff'

'''
Try to use as many as expression you can to give the correct answer!
'''























































































'''

# Requirement 1: print
# a g j
print(x[0], x[2], x[4])

# Requirement 2: print
# ['bb', ['ccc', 'ddd'], 'ee', 'ff']
print(x[1])

# Requirement 3: print
# 'bb'
print(x[1][0])

# Requirement 4: print
# ['ccc', 'ddd']
print(x[1][1])

# Requirement 5: print
# 'ddd'
print(x[1][1][1])
print(x[1][1][-1])

# Requirement 6: print
# 'ee'
print(x[1][2])
print(x[1][-2])

# Requirement 7: print
# 'ff'
print(x[1][3])

'''