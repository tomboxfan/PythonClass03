'''
4 data type:
int     -   integer
float   -   decimal
str     -   string of character
bool    -   True / False
'''

# int

# define a new variable h
h = 2 + 3  # h = 5
j = h - 100 # j = -95
k = h * j # k = 5 * -95 = -475

print('variable h type is:', type(h), 'h=', h)
print('variable j type is:', type(j), 'j=', j)
print('variable k type is:', type(k), 'k=', k)

'''
type() is a python built-in function
---------------------------------------------------
what is a function?

function has a pair of parentheses after the function name - type(), print()
sometimes we put a value inside the parentheses - type(h),  print('hello')

function does something for you.
print('hello') is a function, it helps you print 'hello' to the console.
type(h) is a function, it tells you the type of variable h.

what is python bulit-in function?
1) the function is supplied / defined by python.
2) all we need to do, is , call it. (use it)


we will learn user-defined python in the future.
'''


a = 1.2
b = 0.01
c = -12.0
d = a + b + c
print('variable a type is:', type(a), 'a=', a)
print('variable b type is:', type(b), 'b=', b)
print('variable c type is:', type(c), 'c=', c)
print('variable d type is:', type(d), 'd=', d)

e = j / h
print('variable e type is:', type(e), 'e=', e)
