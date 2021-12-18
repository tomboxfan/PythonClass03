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

print('--------------------')

for i in range(10):
    print("*" * 10)

print('--------------------')


'''
IMPORTANT!!! ------------------------------------
[style 2]
range(start, stop) generates number in range [start, stop)
-------------------------------------------------
'''

print('range(5,10) generates number from 5 to 9, no 10!')
for i in range(5, 10):
    print(i)

print('--------------------')

print('range(5,6) generates 1 number only - 5, it only loops once.')
print('range(5,5) generates no number. So this prints nothing, no loop at all')
for i in range(5, 6):
    print(i)

print('--------------------')



'''
IMPORTANT!!! ------------------------------------
[style 3]
range(start, stop, step) generates number in range [start, stop), with step 
-------------------------------------------------
'''
print("range(2,10,2) generates number: 2 4 6 8")
for i in range(2, 10, 2):
    print(i)

print('--------------------')

print("range(10,100,10) generates number: 10 20 30 40 50 60 70 80 90")
for i in range(10, 100, 10):
    print(i)

print('--------------------')


for i in range(10, -10, -2):
    print(i)

print('--------------------')

'''
There are three ways you can call range() : 
range(stop) takes one argument.
range(start, stop) takes two arguments.
range(start, stop, step) takes three arguments.
'''

'''
HOMEWORK:
Change the output to single line except the '*' * 10 example.
'''