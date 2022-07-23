'''
Requirement:
Find all 3 number combination possibilities for number 1, 2, 3, 4, 5

Your program should output all 10 possibilities, as below:
There are total 10 groups. They are: {(2, 4, 5), (1, 3, 5), (1, 2, 3), (1, 3, 4), (2, 3, 5), (3, 4, 5), (2, 3, 4), (1, 2, 5), (1, 4, 5), (1, 2, 4)}
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
                final_result_container.add(tuple({i, j, k}))




print(f"There are total {len(final_result_container)} groups. They are: {final_result_container}")

