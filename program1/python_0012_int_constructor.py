

int_a = int('10')
print(int_a, type(int_a))

# IMPORTANCE !!! ----------------------------------------
# 1) int(...) is called int constructor
# 2) '10' is a str value, you put a str value '10' inside int constructor -> int('10')
# 3) int constructor helps convert str '10' to int 10
# -------------------------------------------------------

int_b = int(1.2)
print(int_b, type(int_b))

# IMPORTANCE !!! ----------------------------------------
# 1) 1.2 is a float value, you put float value 1.2 inside int constructor -> int(1.2)
# 2) int constructor helps convert float 1.2 to int 1
#
# 1.2 and '10' have a name - argument (参数)
# The thing / value you pass to a function (like print() / type() / int()) are called 'argument'
# -------------------------------------------------------

int_c = int()
print(int_c, type(int_c))
# IMPORTANCE !!! ------------------------------------------------
# 1) If you pass nothing to int constructor, then it creates int 0
# ---------------------------------------------------------------

'''
Homework:

print out the following 4 int variables, observe their value
summarize how int constructor works for float value
'''

int_d = int(2.1)
int_e = int(3.9)
int_f = int(-4.1)
int_g = int(-5.9)
'''
Your conclusion: 
'''

