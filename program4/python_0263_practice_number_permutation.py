'''
Requirement:
Find all 3 number permutation possibilities for number 1, 2, 3, 4, 5

Your program should output all 60 possibilities, as below:
There are total 60 groups. They are: {(5, 4, 2), (1, 5, 4), (2, 1, 3), (4, 2, 1), (2, 5, 1), (3, 2, 1), (4, 5, 3), (2, 5, 4), (5, 2, 1), (3, 2, 4), (1, 2, 5), (1, 4, 2), (3, 1, 2), (3, 4, 1), (3, 1, 5), (1, 4, 5), (5, 2, 4), (4, 1, 2), (4, 1, 5), (2, 4, 5), (4, 3, 2), (4, 3, 5), (5, 3, 2), (5, 1, 2), (5, 4, 1), (3, 5, 2), (1, 5, 3), (2, 1, 5), (4, 2, 3), (4, 5, 2), (2, 5, 3), (1, 2, 4), (5, 2, 3), (3, 1, 4), (1, 3, 2), (1, 3, 5), (4, 3, 1), (2, 4, 1), (2, 3, 5), (5, 1, 4), (5, 3, 1), (5, 4, 3), (3, 5, 1), (1, 5, 2), (5, 3, 4), (3, 5, 4), (2, 1, 4), (4, 2, 5), (4, 5, 1), (1, 2, 3), (1, 3, 4), (3, 2, 5), (1, 4, 3), (3, 4, 2), (3, 4, 5), (2, 3, 4), (4, 1, 3), (2, 4, 3), (2, 3, 1), (5, 1, 3)}
'''


# PREPARE DATA STRUCTURE BEGIN =========================================

# I define a set to hold the 5 numbers
number_set = set(range(1, 6))
print(number_set)

# I define another set to hold all the combinations
# Why I use set here? Because combinations don't have duplicate values,and they don't have any order.
final_result_container = set()


# BEGIN YOUR ALGO / MAIN PROGRAM BEGIN =================================

# Algo name: Complete Search
# Use your computer's strong power to check all situations one by one

for i in number_set:
    for j in number_set:
        for k in number_set:

            if len({i, j, k}) == 3:



                final_result_container.add((i, j, k))




print(f"There are total {len(final_result_container)} groups. They are: {final_result_container}")

