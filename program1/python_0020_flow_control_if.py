

today = input("What day is today? ")

print('I get up at 7 am.')
print('I have my breakfast ast 8 am.')


'''
IMPORTANCE !! -----------------------------------------

if <boolean expression>:
    <statement>
    <statement>
    <statement>
    
1) ":" at the end of the if clause
2) all code under if section are indented 4 spaces. (auto done by Pycharm)    
3) Python will treat all these indented code as a single unit, a single block, either run all, or run none.
4) The block will be executed if boolean expression is True.
-------------------------------------------------------
'''
if today == 'Saturday': # after if, you put a boolean expression, which gives you a True/False value, followed by ":"
    print("I attend Mr Fan's Python lesson at 9 am.")
    print("I start working on my Python homework at 10:15 am.")
    print("I am done with my Python homework at 10:45 am.")


print("I have my lunch at 12 pm.")
print("I play football with my friends at 5 pm.")
print("I have dinner at 7 pm.")
print("I go to bed at 10 pm.")
