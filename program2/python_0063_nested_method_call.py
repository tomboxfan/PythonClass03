animals = ['tiger', 'elephant', 'snake', 'shark']


'''
Python runs code from top line to bottom line.
In the same line, python runs from left to right.
Here python notices, it needs to append something at the end of the animals list.
Then python tries figuring out what it should append, it notices it is another function call.
So append function pauses first.
Python will first call animals.pop(0), 'tiger' is popped out, returned as the value to be appended.
Then append function resumes.
'''
animals.append(animals.pop(0))

'''
it equals to:
popped_animal = animals.pop(0)
animals.append(popped_animal)
'''

print(animals) # ['elephant', 'snake', 'shark', 'tiger']