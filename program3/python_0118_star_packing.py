def calculate_sum(*args):
    print(type(args))
    return sum(args)


result = calculate_sum(1, 2, 3, 4, 5) # Passing in 5 arguments to function calculate_sum
print(result)

result = calculate_sum(10, 20) # Passing in 2 arguments to function calculate_sum
print(result)

'''
Summary:

It is useful if you need to pass in 2 arguments this time, and 5 arguments next time.
The argument count is not fixed.

The star can help group all arguments into a list.


Function caller         ->      Function Body 
1, 2, 3, 4, 5                   *args

When star (*) appears in  'function body parameter' 
-> star packing
-> group multiple values into a list 



Function caller         ->      Function Body 
*list1                          a, b, c, d

When star (*) appears in  'function caller arguments' 
-> star unpacking
-> unpack list1 into individual arguments. 
'''