'''
There are 2 loops in all programming languages - while loop and for loop
'''


'''
IMPORTANT!!! -----------------------------------------
This is how your define a for loop.

1) In for loop, you are actually defining a new variable i.
2) range() is a python built-in function.
   range() helps you generate a series of numbers within a given range.
   range(5) generates number 0, 1, 2, 3, 4. No 5!
   
3) So the for loop will loop 5 times. In these 5 times, looping variable i equals to 0, 1, 2, 3, 4.
   
------------------------------------------------------

'''

print('[range style 1] ------------------------------------------')
print('range(stop) generates number in range [0, stop)')
print('----------------------------------------------------------')
for i in range(5):
    print(i)
