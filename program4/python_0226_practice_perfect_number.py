'''
Requirement:
if a number equals to the sum of all of its factors (excluding itself), then the number is called a perfect number
6 is a perfect number, as 6 = 1 + 2 + 3.
Find all perfect number within 1000
'''



















































# Because I need to find all perfect numbers within 1000
# So, I loop from 2 to 1000, check each of them, whether it is perfect number or not.
for candidate in range(2, 1001):

    # print(f"LOG - start checking number {candidate} --------------------------------------")

    factor_list = []

    # Then I just need to check them one by one, whether you are a perfect number or not.
    for potential_factor in range(1, candidate):

        # How to do that? I just need to find all the factors of the number
        # meaning, I need a data structure to hold all the factors, that's why I define a factor_list in the front.
        if candidate % potential_factor == 0:
            factor_list.append(potential_factor)

    # So after this for loop, I have all the factors of the number, I just need to compare its sum vs the number itself.

    # print(f"LOG - its factors are: {factor_list}, its sum is: {sum(factor_list)}")

    if sum(factor_list) == candidate:
        print(f"{candidate} is a perfect number")
    # else:
    #     print(f"{candidate} is not a perfect number")
