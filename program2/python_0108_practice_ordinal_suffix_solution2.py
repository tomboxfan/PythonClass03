
'''
-------
Analysis
-------

str has a function endswith()
We can convert int to str, then I can use str.endswith("1") function to tell, whether the number ends with 1
'''

def ordinal_suffix(number):

    # Step 1) Convert int variable number to str variable number_str
    number_str = str(number)

    # Step 2) special situation: we check 11 / 12 / 13 first, as they are special
    if number_str.endswith("11") or number_str.endswith("12") or number_str.endswith('13'):
        return 'th'

    # Step 3) Common situation:
    elif number_str.endswith("1"):
        return 'st'
    elif number_str.endswith('2'):
        return 'nd'
    elif number_str.endswith('3'):
        return 'rd'
    else:
        return 'th'



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