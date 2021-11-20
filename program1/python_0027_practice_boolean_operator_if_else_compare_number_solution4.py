'''
Requirement:
Ask user to input 3 numbers from console, sort the 3 numbers in ascending order.
'''

x = int(input("X:"))
y = int(input("Y:"))
z = int(input("Z:"))


'''
Nested if / else
We have another if / else inside a parent if / else 
'''

if x <= y and x <= z:
    if y <= z:
        print(x, y, z)
    else:
        print(x, z, y)


elif y <= x and y <= z:
    if x >= z:
        print(y, z, x)
    else:
        print(y, x, z)


elif z <= y and z <= x:
    if y >= x:
        print(z, x, y)
    else:
        print(z, y, x)