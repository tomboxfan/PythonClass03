

def func1(a, b, c, d):
    print(a, b, c, d)

func1(1, 2, 3, 4)





list1 = [1, 2, 3, 4]

# func1(list1) # this doesn't work - because argument count is not the same as parameter count
               # TypeError: func1() missing 3 required positional arguments: 'b', 'c', and 'd'


'''
Star (*) can unpack a list
Star (*) can convert list1 to 4 individual values
'''

func1(*list1) # become func1(1, 2, 3, 4)
# This is called 'unpack'