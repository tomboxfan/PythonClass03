'''
Requirement:
Ask user to input 3 numbers from console, sort the 3 numbers in ascending order.
'''

x = int(input("X:"))
y = int(input("Y:"))
z = int(input("Z:"))

if x <= y and x <= z and y <= z:
    print(x, y, z)

elif x <= y and x <= z and y >= z:
    print(x, z, y)

elif y <= x and y <= z and x >= z:
    print(y, z, x)

elif y <= x and y <= z and z >= x:
    print(y, x, z)

elif z <= y and z <= x and y >= x:
    print(z, x, y)

elif z <= y and z <= x and y <= x:
    print(z, y, x)

