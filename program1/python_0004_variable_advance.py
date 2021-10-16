
# define a variable with value = 5
h = 5
print("Now h value is", h)

'''
IMPORTANCE!!! ------------------------------------
FOREVER REMEMBER:
when variable appears on the right side of '='  : use variable's value
when variable appears on the left  side of '='  : assign value from the right to the variable on the left

explanation --------------------------------------
on the right side of '='    : h - 1
                              use variable h's value -> 5
                              5 - 1 = 4
 
on the left  side of '='    : h
                              assign value from the right, to the variable h
                              now h becomes 4 
'''

h = h - 1
print("Now h value is", h)

h -= 1 # this equals to 'h = h - 1'
print("Now h value is", h)

h += 1 # this equals to 'h = h + 1'
print("Now h value is", h) # 4

h *= 2 # this equals to 'h = h * 2'
print("Now h value is", h) # 8

h /= 4 # this equals to 'h = h / 4'
print("Now h value is", h) # 2.0

