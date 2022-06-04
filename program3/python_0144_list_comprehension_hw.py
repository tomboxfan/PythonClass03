
'''
HOMEWORK  -------------------------------------
Requirement:
1) Use list comprehension to define a new list which contains 10 square numbers of 1 to 10, being 1,4,9....100
2) Calculate the sum of the newly-created list
'''


def sum_of_all_square_num():
    r = range(1, 11)
    sqr_list = [ i * i    for i in r]
    print(sqr_list)
    result = sum(sqr_list)
    print(f"The sum of square list is: {result}")



sum_of_all_square_num()