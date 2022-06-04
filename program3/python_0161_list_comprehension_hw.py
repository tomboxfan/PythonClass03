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

# example()
