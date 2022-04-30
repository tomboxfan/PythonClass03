'''

Requirement:

Leibniz is a famous German mathematician who lived 300 years ago!
He figured out the value of pi using the following formula

pi / 4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 ...

People call this formula Gregory-Leibniz Series

You task is to write a program to find pi's value
Calculate 1,000,000 entries
'''

# step 1) I define a variable quarter_of_pi
quarter_of_pi = 0

# step 2) I loop and calculate the quarter_of_pi

'''
[solution 1]

1) because: there are 1,000,000 entries in total
   so:  for i in range(1000000)
   
2) 
when i = 0 -> 1/1    -> 1/(1+i*2)
when i = 1 -> 1/3    -> 1/(1+i*2)
when i = 2 -> 1/5    -> 1/(1+i*2)
when i = 3 -> 1/7    -> 1/(1+i*2)

'''

for i in range(1000000):
    entry = 1/(1 + i * 2)
    if i % 2 == 0:
        quarter_of_pi += entry
    else:
        quarter_of_pi -= entry

value_of_pi = quarter_of_pi * 4
print(f"{value_of_pi:.5f}")
print('--------------------------------------------')



'''
[solution 2]
   
2) 
when i = 0 -> 1/1     -> 1/(1+i*2) * ((-1) ** i)
when i = 1 -> -1/3    -> 1/(1+i*2) * ((-1) ** i)
when i = 2 -> 1/5     -> 1/(1+i*2) * ((-1) ** i)
when i = 3 -> -1/7    -> 1/(1+i*2) * ((-1) ** i)
'''


quarter_of_pi = 0

for i in range(1000000):
    quarter_of_pi += 1/(1 + i * 2) * ((-1) ** i)

value_of_pi = quarter_of_pi * 4
print(f"{value_of_pi:.5f}")
print('--------------------------------------------')

'''
[solution 3]
group1 = 1/1 - 1/3   
group2 = 1/5 - 1/7
group3 = 1/9 - 1/11

1) because: there are 500,000 groups in total
   so     : for i in range(500000)

2) 
when i = 0 -> 1/1 - 1/3     -> 1/(1+i*4) - 1/(3+i*4)
when i = 1 -> 1/5 - 1/7     -> 1/(1+i*4) - 1/(3+i*4)
when i = 2 -> 1/9 - 1/11    -> 1/(1+i*4) - 1/(3+i*4)
'''


quarter_of_pi = 0

for i in range(500000):
    group = 1 / (1 + i * 4) - 1 / (3 + i * 4)
    quarter_of_pi += group

value_of_pi = quarter_of_pi * 4
print(f"{value_of_pi:.5f}")
print('--------------------------------------------')




