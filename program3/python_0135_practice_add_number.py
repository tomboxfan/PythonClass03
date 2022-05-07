'''
find the value of s
s = a + aa + aaa + aaaa + aa...a，
a can be any number from 1 to 9
term count comes from user input in console.

For example:
Enter the base number:2
Enter the term count:5
The answer is 24690

Explanation:
2 + 22 + 222 + 2222 + 22222 is 24690
'''


# -- Prepare function --------------------------


'''
-------------
Analysis
-------------
term 0 - 5
term 1 - 55 = 5 * 10 + 5
term 2 - 555 = (5 * 10 + 5) * 10 + 5
term 3 - 5555 = ((5 * 10 + 5) * 10 + 5) * 10 + 5
 
term 0 - Loop 0 times [* 10 + 5]
term 1 - Loop 1 times [* 10 + 5]
term 2 - Loop 2 times [* 10 + 5]
term 3 - Loop 3 times [* 10 + 5]
'''
def solution1_math1(base_number, term_count):

    # define a variable which store the final result
    sum = 0

    for term_no in range(term_count):

        term_value = base_number

        for _ in range(term_no):
            term_value = term_value * 10 + base_number

        sum += term_value

    return sum


'''
Question:
How many times the calculation (line 44) will be executed? 

Let's say, in total we have to calculate n terms.
Answer: 1 + 2 + 3 + .... + n
      = (1 + n) * n / 2
      = 1/2 * n^2 + 1/2 * n

Time Complexity: O(n^2)
'''



'''
-------------
Analysis
-------------
term 0 - 5
term 1 - 55 = (term 0 * 10) + 5
term 2 - 555 = (term 1 * 10) + 5
term 3 - 5555 = (term 2 * 10) + 5
'''


def solution2_math1_optimized(base_number, term_count):
    sum = 0

    # term 0
    term_value = base_number
    sum += term_value

    for _ in range(term_count - 1):                     # repeat term_count - 1 times
        term_value = term_value * 10 +base_number       # calculate the next value of 'term_value'
        sum += term_value                               # add to sum

    return sum


'''
Question:
How many times the calculation (line 84) will be executed?

Let's say, in total we have to calculate n terms.
Answer: n - 1

Time Complexity: O(n)
'''




'''
-------------
Analysis
-------------
term 0 - 1 = 10^0
term 1 - 11 = 10^1 + 10^0
term 2 - 111 = 10^2 + 10^1 + 10^0
term 3 - 1111 = 10^ 3 + 10^2 + 10^1 + 10^0

term 0 + term 1 + .... term n
= 10^0 + 10^1 + 10^0 + 10^2 + 10^1 + 10^0 ....

We can calculate the result above, and last step multiply it using base_number
'''


def solution3_math2(base_number, term_count):
    sum = 0

    for x in range(term_count):
        for j in range(x + 1):
            sum += 10 ** j

    return sum * base_number




def solution4_math2_optimized(base_number, term_count):
    term_value = 0
    sum = 0
    for i in range(0, term_count):
        term_value = term_value + (10 ** i) * base_number
        sum += term_value

    return sum



'''
--------------------
Analysis
--------------------
I make use of Python's built-in function eval(str) to calculate the result.
So I use the 2 param - base_number & term_count to construct the expression str
'''

def solution5_eval(base_number, term_count):

    expression = ''
    for i in range(1, term_count + 1):
        expression += str(base_number) * i

        if i < term_count:
            expression += '+'

    print("Here comes the expression: ", expression)

    sum = eval(expression)
    return sum









# -- Prepare data --------------------------
base_number = int(input("enter the base number: "))
term_count = int(input("enter the term count: "))

print("Base number: ", base_number)
print("Term count: ", term_count)

# -- main program --------------------------


result = solution1_math1(base_number, term_count)
print("The result is: ", result)

result = solution2_math1_optimized(base_number, term_count)
print("The result is: ", result)

result = solution3_math2(base_number, term_count)
print("The result is: ", result)

result = solution4_math2_optimized(base_number, term_count)
print("The result is: ", result)

result = solution5_eval(base_number, term_count)
print("The result is: ", result)


