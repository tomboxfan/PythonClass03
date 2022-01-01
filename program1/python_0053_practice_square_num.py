'''
Requirement:
Find all the possible value for number X which satisfies the following condition:
1) X + 100 is a square number.
2) X + 100 + 168 is another square number.

X is in range [-100, 2000]
'''

'''
Our 1st algo: brute force.

Analysis:
1) The range is [-100, 2000], so all I need to do is to loop all numbers in range(-100, 2001)
2) for each number in range, I just need to check whether the number x
    whether x + 100 is a square number or not?
    whether x + 100 + 168 is a square number or not?
    if both are True, x is what I am looking for
'''

import math


for x in range(-100, 2001):
    sqr_num_1 = x + 100
    sqr_num_2 = x + 100 + 168

    sqr_root_for_sqr_num_1 = math.sqrt(sqr_num_1)
    sqr_root_for_sqr_num_1_int = int(sqr_root_for_sqr_num_1)

    if sqr_root_for_sqr_num_1 != sqr_root_for_sqr_num_1_int:
        continue

    sqr_root_for_sqr_num_2 = math.sqrt(sqr_num_2)
    sqr_root_for_sqr_num_2_int = int(sqr_root_for_sqr_num_2)

    if sqr_root_for_sqr_num_2 != sqr_root_for_sqr_num_2_int:
        continue

    print(x, "is such a number")

