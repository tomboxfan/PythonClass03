
# example 1 -------------------------------

def square(x):
    return x ** 2

# you use keyword 'return' to return x square back to the function caller
# your function code finishes once it meets return


result1 = square(1)
result2 = square(2)
print(result1, result2)


result = []
for i in range(101):
    result.append(square(i))

print(result)



# example 2 -------------------------------

def volume_of_cuboid(length, width, height):
    return length * width * height

l = 5
w = 4
h = 3
print('length = ', l, ', width = ', w, ', height = ', h, ', volume = ', volume_of_cuboid(l, w, h))


'''
<HOMEWOKR>

Requirement:
Define a function to find the nth_root of number x.

For example:
print(nth_root(4,2)) # This should print the square root of 4, so it should print 2
print(nth_root(27,3)) # This should print the cube root of 27, so it should print 3
print(nth_root(625,4)) # This should print the 4th root of 625, so it should print 5
'''

def nth_root(x, n):
    pass

print(nth_root(4,2)) # 2
print(nth_root(27,3)) # 3
print(nth_root(625,4)) # 5