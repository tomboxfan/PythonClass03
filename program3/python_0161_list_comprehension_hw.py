'''
HOMEWORK:
without actually run example(), please tell me,
1) what does the new_list look like?
2) what type of value does it contain?
2) what values does it contain?

You can google the meaning of pow() function in python, but you can never run it.
after you get the answer, you can run it and verify.
'''


def example():
    new_list = [(val, pow(val, 3)) for val in range(10)]
    print(new_list)

example()


'''

1) The function creates a list of tuples from a range object.
2) the range object generates numbers from 0 to 9
3) each tuple contains the number and its cube, which is calculated using the pow function.
4) the expression returns a tuple (val, pow(val, 3))


-------------------
About pow(a, b) 
-------------------
pow(a, b) is a python built-in function, which calculates a to the power of b

For example:
pow(5, 2), equals to 5 ** 2, equals to 25 
pow(5, 5), equals to 5 ** 3, equals to 125 

'''