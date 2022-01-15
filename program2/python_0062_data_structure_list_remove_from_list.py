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
if index < len(animals):
     popped_animal = animals.pop(index)
else:
    print(f"{index} is an invalid index value for list animals, right now we only have {len(animals)} items in animals")

'''
HOMEWORK:
How to correct line 25, to make sure the index value is always valid? Even when it is negative.
'''