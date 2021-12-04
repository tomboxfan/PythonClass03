import random


'''
IMPORTANT!! -----------------------
random.randint(1, 10) is composed of 4 parts:

1) random   : module name
2) .        : separate the module name & function name
3) randint  : function name
              it is under random module
              It will return a random number in range[1,10], both 1 & 10 are included.
4) (1, 10)  : argument list. Both 1 and 10 are argument. 
-----------------------------------

'''


i = 0
while i < 10:
    random_int = random.randint(1, 3)
    print(random_int)
    i += 1

print('-----------------------------------------')

i = 0
while i < 10:
    random_number = random.random() # random.random() returns a random float in range [0,1)
    print(random_number)
    i += 1

print('-----------------------------------------')

i = 0
while i < 10:
    random_number = random.uniform(7.7, 7.8) # random.uniform(7.7, 7.8) returns a random float in range[7.7, 7.8)
    print(random_number)
    i += 1
