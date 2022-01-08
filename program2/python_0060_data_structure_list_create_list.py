'''

What is data structure?

Variable is like a pointer, points to a box which holds a value - int / float / boolean / str
Data structure is like a cabinet, which contains many boxes!
When the variable pointer, points to a cabinet, then you can use the variable to open the cabinet, and use any value inside the cabinet.

The first data structure we learn today is called - list

List -> Workhorse

'''

# Solution 1: Use square bracket --------------------------------------
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
print(fruits)

animals = ['tiger',
           'elephant',
           'snake',
           'shark']

print(animals)

cars = [] # create an empty list
print(cars)

# Solution 2: use list constructor --------------------------------
students = list() # create an empty list
print(students)

numbers = list(range(10)) # pass in a range object to create numbers list
print(numbers)

char_list = list("I love Python!")
print(char_list)