def stupid_function():
    pass

print(stupid_function())

'''
None is a python value
None means, 'nothing is here'
None means, 'We haven't put any value here yet'
'''


# Initialize a list with size 10, but there is nothing in it.
# Just a empty list with 10 empty places
list1 = [None] * 10
print(list1)


def func1():
    print("A function returns nothing")

val1 = func1()
print(val1)

if val1 == None:
    print("The function doesn't return anything, as there is nothin inside var1")
else:
    print("The function returns something, as var1 is not None")