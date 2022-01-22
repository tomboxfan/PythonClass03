animals = ['tiger', 'elephant', 'snake', 'shark'] * 2
print(animals) # ['tiger', 'elephant', 'snake', 'shark', 'tiger', 'elephant', 'snake', 'shark']

# Solution 1: Use del - remove item by index
del animals[1]
print(animals) # ['tiger', 'snake', 'shark', 'tiger', 'elephant', 'snake', 'shark']


# Solution 2: Use pop - remove last element
popped_animal = animals.pop()
print(popped_animal, 'is popped out.') # shark is popped out.
print(animals) # ['tiger', 'snake', 'shark', 'tiger', 'elephant', 'snake']

popped_animal = animals.pop(1)
print(popped_animal, 'is popped out.') # snake is popped out.
print(animals) # ['tiger', 'shark', 'tiger', 'elephant', 'snake']


# index must be a valid value, otherwise:
# IndexError: pop index out of range
# animals.pop(30)

# So you need to check index before calling pop method
index = -20
if -len(animals) <= index < len(animals):
     popped_animal = animals.pop(index)
else:
    print(f"{index} is an invalid index value for list animals, right now we only have {len(animals)} items in animals")

print(animals)


'''
The size of the animals list is 5.
The positive index range is [0,5)
The negative index range is [-5,-1]

So it full index range is [-5, 5), which is [-len(animals), len(animals))


'''


# Solution 3: Use remove - remove item by value
animals.remove('tiger')
print(animals) # ['shark', 'tiger', 'elephant', 'snake']
# remove(item) will only remove the 1st matched item, and ignore all the following matched items.

# ValueError: list.remove(x): x not in list
# animals.remove('leopard')

if 'leopard' in animals:
    animals.remove('leopard')
else:
    print("leopard doesn't exist in list animals")

if 'penguin' not in animals:
    animals.append('penguin')
    print('penguin has been appended to animals')
    print(animals)

'''
IMPORTANCE!!! ----------------------------------------------------
'in' operator tells you whether the item exists in the list or not!
------------------------------------------------------------------

'''