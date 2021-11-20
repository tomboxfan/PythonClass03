'''
Requirement:
Ask user to input 3 numbers from console, sort the 3 numbers in ascending order.
'''

x = int(input("X:"))
y = int(input("Y:"))
z = int(input("Z:"))

if x <= y and y <= z:
    print(x, y, z)

elif x <= z and z <= y:
    print(x, z, y)

elif y <= z and z <= x:
    print(y, z, x)

elif y <= x and x <= z:
    print(y, x, z)

elif z <= x and x <= y:
    print(z, x, y)

elif z <= y and y <= x:
    print(z, y, x)

