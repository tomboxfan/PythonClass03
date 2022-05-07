'''
Nilakantha is another famous Indian mathematician who lived 500 years ago!
He figured out the value of pi using the following formula

pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) ...

People call this formula Nilakantha Series

You task is to write a program to find pi's value
Calculate 1,000,000 entries
'''


'''
------------
Analysis
------------

group 1 -> 4/(2*3*4) - 4/(4*5*6)        -> 1st entry number starts from 2   -> index = 2    -> 4/(index * (index + 1) * (index + 2)) - 4/((index + 2) * (index + 3) * (index + 4)) 
group 2 -> 4/(6*7*8) - 4/(8*9*10)       -> 1st entry number starts from 6   -> index = 6    -> 4/(index * (index + 1) * (index + 2)) - 4/((index + 2) * (index + 3) * (index + 4)) 
group 3 -> 4/(10*11*12) - 4/(12*13*14)  -> 1st entry number starts from 10  -> index = 10   -> 4/(index * (index + 1) * (index + 2)) - 4/((index + 2) * (index + 3) * (index + 4)) 
... ... 

because we need to calculate 1,000,000 entries, so there are in total 500,000 groups.

group 1 -> index 2  -> 2 + 4 * 0
group 2 -> index 6  -> 2 + 4 * 1
group 3 -> index 10 -> 2 + 4 * 2
...
group 500,000 -> index ? -> 2 + 4 * 499,999 = 1,999,998

so, it should be:

for index in range(2, 1999998, 4)

because the 2nd param is exclusive, so we have to add 4 to it, it becomes

for index in range(2, 2000002, 4)

'''

value_of_pi = 3

group_count = 0

for index in range(2, 2000002, 4):
    denominator1 = index * (index + 1) * (index + 2)
    denominator2 = (index + 2) * (index + 3) * (index + 4)
    group = 4 / denominator1 - 4 / denominator2
    value_of_pi += group
    group_count += 1

print(f"The result is: {value_of_pi:.10f}")
print(f"There are in total {group_count} groups, a.k.a {group_count * 2} entries.")
