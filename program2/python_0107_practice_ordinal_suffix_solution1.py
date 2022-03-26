'''
Requirement:
Implement a python function to convert a int to its ordinal.

def convert_to_ordinal(number):
    pass

For example:
convert_to_ordinal(1) returns  1st
convert_to_ordinal(2) returns  2nd
convert_to_ordinal(200) returns  200th
'''



'''
------------
Analysis
------------

Here come some natural numbers together with their ordinal suffix:

0   1   2   3   4   5   6   7   8   9
th  st  nd  rd  th  th  th  th  th  th

10  11  12  13  14  15  16  17  18  19
th  th  th  th  th  th  th  th  th  th

20  21  22  23  24  25  26  27  28  29
th  st  nd  rd  th  th  th  th  th  th

30  31  32  33  34  35  36  37  38  39
th  st  nd  rd  th  th  th  th  th  th

def ordinal_suffix(number):
    pass
    
print(ordinal_suffix(1)) # st
print(ordinal_suffix(2)) # nd
print(ordinal_suffix(11)) # th
print(ordinal_suffix(21)) # st
'''


def ordinal_suffix(number):

    # edge case
    # Step 1) becuase 11 / 12 / 13 are special, so we consider them first
    if number in [11, 12, 13]: # if number == 11 or number == 12 or number == 13:
        return 'th'


    # common situation
    # Step 2) I use modulo operator % to find the number's unit digit
    unit_digit = number % 10

    # Step 3) I make use of list index - value relationship.
    ordinal_suffix_list = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
    return ordinal_suffix_list[unit_digit]

# test code ----------------------------
# for i in range(30):
#     print(f"Number: {i}, ordinal suffix: {ordinal_suffix(i)}")



def convert_to_ordinal(number):
    return str(number) + ordinal_suffix(number)


# test code ----------------------------
for i in range(200):
    print(convert_to_ordinal(i))


'''
IMPORTANCE !!! ---------------------------------------
convert_to_ordinal function calls 2 extra functions:
1) built-in function: str constructor
2) user-defined function: ordinal_suffix(value)

function composition means: you call a function inside another function.
------------------------------------------------------
'''