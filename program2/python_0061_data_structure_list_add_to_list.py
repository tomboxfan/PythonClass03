fruits = ['Apple', 'Orange', 'Banana', 'Pear']
animals = ['tiger', 'elephant', 'snake', 'shark']

# Solution 1: use append() - add a new value to the END of the list
fruits.append("Watermelon")
print(fruits)


# List is heterogeneous
fruits.append(True)         # add boolean to the end of the list
fruits.append(1)            # add int to the end of the list
fruits.append(1.2)          # add float to the end of the list
fruits.append("Hello")      # add str to the end of the list
print(fruits)

fruits.append([1,2,3])      # add another list!!!
print(fruits)


'''
        ['tiger', 'elephant', 'snake', 'shark']
index      0           1         2        3
          -4          -3        -2       -1

'''


# Solution 2: Use insert - add new value to the list at index specified
animals.insert(1, "leopard")
print(animals)
animals.insert(100, "giraffe") # when index > length of the list, append it to the end of the list
print(animals)
animals.insert(-2, "hedgehog")
print(animals)


# Solution 3: Use extend - join another list
insects = ['catepillar', 'ant', 'butterfly']
animals.extend(insects)
print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'hedgehog', 'shark', 'giraffe', 'catepillar', 'ant', 'butterfly']

# animals.append(insects) # if you use append here, the insects list will be seend as an indiviual item, and added to the end of the list.
# print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'hedgehog', 'shark', 'giraffe', ['catepillar', 'ant', 'butterfly']]



# Solution 4: Use + to join another list
birds = ['swallow', 'eagle', 'toucan']
# animals = animals + birds
animals += birds
print(animals)


# Solution 5: Use * to duplicate list
many_birds = birds * 3
print(many_birds)

zeros_list = [0] * 20
print(zeros_list)