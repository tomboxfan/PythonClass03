
'''
--------------------------------------------------
Purpose of the parameter: Pass information to a function
--------------------------------------------------
Q) What is inside function parentheses?
A) You can define a variable which is only valid inside the function body.
   So here you learn another way to define variable.

Q) What is parameter?
A) Because, it is only valid inside the function body, so it is has a special name -> parameter

Q) Who will assign value to the variable(the parameter)?
A) When you call the function, you pass the value to the function.
'''

def greet_user(username):

    print(f"Hello, {username}!")
    print("What a nice day!")
    print("Nice to meet you on this beautiful day!")
    print("Any plan tomorrow? I wish you had a good rest!")


greet_user("Tom")
print("-------------------")
greet_user("Billy")
print("~~~~~~~~~~~~~~~~~~~")
greet_user("Sandy")

'''
Q) What is argument? 
A) "Tom" / "Billy" / "Sandy" are arguments.
   When you call the function greet_user("Tom"), you put a str value "Tom" in the pair of parentheses
   We say, you 'pass' value 'Tom' to the function greet_user
   When the control goes inside the function body, this str value 'Tom' becomes the value of the parameter (variable) 'username'
   
   Here, 'Tom' has a speical name - argument.
'''