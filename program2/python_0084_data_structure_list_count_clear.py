fruits = ['Apple', 'Orange', 'Banana', 'Pear'] * 2
fruits.remove('Orange') # Remove 1st 'Orange', 2nd is untouched
fruits.append('Apple')

print(f"There are {fruits.count('Apple')} 'Apple' in fruits list")
print(f"There are {fruits.count('Orange')} 'Orange' in fruits list")
print(f"There are {fruits.count('Banana')} 'Banana' in fruits list")
print(f"There are {fruits.count('Pear')} 'Pear' in fruits list")

print(fruits)

fruits.clear()
print(fruits)
