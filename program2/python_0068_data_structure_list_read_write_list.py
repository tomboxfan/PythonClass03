fruits = ['Apple', 'Orange', 'Banana', 'Pear']
animals = ['tiger', 'elephant', 'snake', 'shark']


'''
------------------------
read item VALUE from list
------------------------
'''


# Solution 1: use index to visit the list

print(animals[0], 'is at index 0')
print(animals[-1], 'is at index -1')

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# Solution 2: use for loop
for animal in animals:
    print(animal, end=' ')
print('\n---------------------------------')


'''
------------------------
read item INDEX from list
------------------------
'''

# Solution 1) use index() method
print("tiger's index is", animals.index('tiger'))
print("shark's index is", animals.index('shark'))


print('\n---------------------------------')

'''
----------------------------------
read item INDEX/VALUE from list
----------------------------------
'''

# Solution 1
index = 0
for animal in animals:
    print(f'{index} : {animal}')
    index += 1

print("--------")
# Solution 2 (better): use built-in function enumerate(list)
for index, animal in enumerate(animals):
    print(f'{index} : {animal}')

'''
IMPORTANCE!!! ------------------------------------------------------------------------------
built-in function enumerate(list) combines index and value into a group, return back to you
-------------------------------------------------------------------------------------------
'''

print('\n---------------------------------')

animals[0] = 'monkey'
print(animals)

fruits[1] = 'Durian'
print(fruits)

'''
IMPORTANCE!!! -----------------------
You can change the content of a list
list is MUTABLE.
-------------------------------------
'''