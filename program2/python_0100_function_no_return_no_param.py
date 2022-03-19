'''
We used to say : define a variable, use a variable
Now we say     : define a function, call a function
'''



# Part 1) define a function: greet_user() ----------------------------------

'''
def         : reserved keyword. Every time you define a function, you ALWAYS start with 'def'.
greet_user  : function name. Just like variable name. 
()          : parentheses
:           : Whenever you start some body - if body / for loop body / while loop body, you need to put this colon. 
              You start your function body. 
              All code after that should be put in the next indentation.
'''

def greet_user():

    print("Hello!")
    print("What a nice day!")
    print("Nice to meet you on this beautiful day!")
    print("Any plan tomorrow? I wish you had a good rest!")



# Part 2) call the function: greet_user() ---------------------------------

greet_user()
print("-------------------")
greet_user()
print("~~~~~~~~~~~~~~~~~~~")
greet_user()


'''
Alt + Shift + F9 -> debug
debug means: your program will pause at the break point.
'''


# another example ------------------------

def launch_missile():
    print("Missile launched!")
    print("Mission Accomplished!")


launch_missile()
launch_missile()
launch_missile()
launch_missile()
