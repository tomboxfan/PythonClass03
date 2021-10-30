


# IMPORTANCE !!! ----------------------------------------------------
# YOU MUST BE CRYSTAL CLEAR OF THE VARIABLE TYPE IN YOUR MIND
# -------------------------------------------------------------------

a_int_var = 1
a_float_var = 1.0
a_str_var = 'hello'
a_bool_var = True

print(a_int_var, a_float_var, a_str_var, a_bool_var)
print('---------------------------------------------------------')

str_a = '10'
str_b = "10.2"
print(str_a, str_b)

str_c = str_a + str_b  # str + str gives you another str. So str_c is of type 'str'
print(f"Join 2 str: '{str_a}' + '{str_b}' = '{str_c}'")
print('---------------------------------------------------------')

int_a = int(str_a)          # convert str '10' to int 10
float_b = float(str_b)      # convert str '10.2' to float 10.2
print(f'{int_a} is of type : {type(int_a)}')
print(f'{float_b} is of type : {type(float_b)}')

float_c = int_a + float_b # int + float gives you another float. So float_c is of type 'float'
print(f'Plus 2 numbers : {int_a} + {float_b} = {float_c}')
print('---------------------------------------------------------')


# int constructor will remove everything after decimal points

int_a = int(2.1) # 2
int_b = int(3.9) # 3
int_c = int(-4.1) # -4
int_d = int(-5.9) # -5
int_e = int('6')
print(int_a, int_b, int_c, int_d, int_e)


float_a = float(2)
float_b = float(3)
float_c = float('4')
print(float_a, float_b, float_c)