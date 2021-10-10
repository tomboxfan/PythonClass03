
# The most important thing in python programming is:
# 1) define a variable
# 2) use a variable



# --------------------------------
# DEFINE VARIABLES
# --------------------------------



# This defines a variable
# I can give the variable name what I like
# I want to give my variable a name -> a_number, and I want to put value 5 into variable a_number's box.
a_number = 5

# I want to give my variable a name -> another_number, and I want to put value 2 into variable another_number's box.
another_number = 2


# Shortcut key:
# duplicate the current line: Ctrl + D
# Move line up: Alt + Shift + Up
# Move line down: Alt + Shift + Down


# I want to give my variable a name -> greeting_word, and I want to put value 'Hello!' into variable greeting_word's box.
greeting_word = 'Hello!'


# IMPORTANCE!!! --------------------------------------------------------------------------
# The meaning of =:
# put the value on the right side to the variable's box on the left side
# This is called assignment.
# ----------------------------------------------------------------------------------------



# --------------------------------
# USE VARIABLES
# --------------------------------

# Now, I am going to use the 3 variables.
print(a_number)
print(another_number)
print(greeting_word)


# You can NOT use an undefined variable, you will see red-line below the undefined variable.
# print(q)

# Shortcut key:
# Convert the code to comment: Ctrl + /
# Convert the comment to code: Ctrl + /

print(a_number, another_number, greeting_word)



# These are using variables a_number and another_number
# This is also defining a new variable plus_variable
# a_number's value plus another_number value, assign it to a new variable, and I'd like to name it 'plus_variable'
# I shall give the variable a meaning name - plus_variable is a good one
plus_variable = a_number + another_number

minus_variable = a_number - another_number

multiply_variable = a_number * another_number

divide_variable = a_number / another_number

print(plus_variable, minus_variable, multiply_variable, divide_variable)

print(a_number, '+', another_number, '=', plus_variable)
print(a_number, '-', another_number, '=', minus_variable)
print(a_number, '*', another_number, '=', multiply_variable)
print(a_number, '/', another_number, '=', divide_variable)

# 5 / 2 = 2r1

# Floor division - find quotient
floor_division_variable = a_number // another_number    # 5 // 2 = 2 (quotient / 商)  5 divided by 2 = 2r1

# Modulus - find remainder
remainder_variable = a_number % another_number  # 5 % 2 = 1 (remainder / 余数)  5 divided by 2 = 2r1

print(a_number, '//', another_number, '=', floor_division_variable)
print(a_number, '%', another_number, '=', remainder_variable)


power_variable = a_number ** another_number # For example: 5 ** 2 = 25      5 ** 3 = 125     5 ** 4 = 625
print(a_number, '**', another_number, '=', power_variable)

power_variable2 = power_variable ** (1/2)  # For example: 25 ** (1/2) = 5     125 ** (1/3) = 5    625 ** (1/4) = 5
print(power_variable, '**', '1/2', '=', power_variable2)


# step 1) define variables a/b/c/d/e/f
a = 1
b = 2
c = 5
d = 6
e = 7
f = 9

# Step 2) doing math using variables a/b/c/d/e/f, assign the result to a newly-defined variable 'answer'
answer = (a - (a / b) * (b / c)) / (e / f)

# Step 3) use variable answer
print(answer)



