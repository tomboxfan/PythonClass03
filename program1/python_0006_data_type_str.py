# step 1) define 3 str variables
str1 = "hello python!"
str2 = 'str value surrounded by single quote.'
str3 = "str value surrounded by double quotes."

'''
IMPORTANCE!!! ---------------------------
You can use either single quote or double quotes in str
-----------------------------------------
'''

# step 2) I use the 3 variables
print('variable str1 type is:', type(str1), 'str1=', str1)
print('variable str2 type is:', type(str2), 'str2=', str2)
print('variable str3 type is:', type(str3), 'str3=', str3)




'''
IMPORTANCE!!! ---------------------------
'+' sign joins multiple str values and gives you a new str value
-----------------------------------------
'''
first_name = 'Tom'
last_name = 'Hanks'
full_name = first_name + " " + last_name
print('My favourite actor is:', full_name)

a = 1       # int variable
b = 2       # int variable
c = a + b   # int variable
print(c) # 3

a = '1'     # str variable
b = '2'     # str variable
c = a + b   # str variable
print(c)    # 12

'''
IMPORTANCE!!! ---------------------------
'*' sign duplicates str value and gives you a new str value
-----------------------------------------
'''
separate_line = '*' * 50
print(separate_line)


a = 2       # int variable
b = a * 3   # int variable
print(b)    # 6

a = '2'     # str variable
b = a * 3   # str variable
print(b)    # 222
