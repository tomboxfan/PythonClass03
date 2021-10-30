first_name = 'James'
last_name = 'Bond'

# Requirement: Print out str: 'My name is Bond, James Bond'


# [Solution 1] pass 4 str values to print() function
# [Solution 1 Problem] there is an extra space between Bond and ','
print('My name is', last_name, ',', first_name, last_name)

# [Solution 2] Use '+' sign to join 5 str values together, pass this newly-joined single str value to print() function
# [Solution 2 Problem] Too many '+' sign, very messy, not readable
print('My name is ' + last_name + ', ' + first_name + ' ' + last_name)


# [Solution 3] Use python f string
# IMPORTANCE!!! ----------------------------------------------
# 1) Have an f at the beginning
# 2) curly braces containing expressions / variables that will be replaced by python
# ------------------------------------------------------------
print(f'My name is {last_name}, {first_name} {last_name}')

# expression
print(f'2 + 3 = {2 + 3}')
print(f'My full name is: {first_name + " " + last_name}')

print(f'No, Mr {last_name}, I expect you to die!')

age = 91
print(f'Sean Connery is now {age} years old.')

language = 'Python'
rank = 1
who = 'all kids'
kids_age = 12
teacher_surname = 'FAN'

print(f'{language} is the world no {rank} programming language, {who} should start learning it from age {kids_age}, and they will all learn {language} with Teacher {teacher_surname}.')
print(f'{who} enjoy learning {language}, as {language} is quite fun, and Teacher {teacher_surname} is quite fun!')
