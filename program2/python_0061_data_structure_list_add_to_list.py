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