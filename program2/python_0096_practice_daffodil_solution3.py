
'''
Logic:
if it is so difficult to find the unit / tens / hundreds numbers from the 3 digit number itself
Then we can use nested loop to find the answer directly
'''


for hundreds_digit in range(1, 10):
    for tens_digit in range(10):
        for unit_digit in range(10):

            i = 100 * hundreds_digit + 10 * tens_digit + unit_digit

            if hundreds_digit ** 3 + tens_digit ** 3 + unit_digit ** 3 == i:
                print(i)



'''
What we've learnt:
1) nested loop
'''