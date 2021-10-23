'''

bool is the 4th data type in Python. Sometimes, we call it boolean.
It has only 2 value - True / False
It means something is True of False

For example:
1) Is today a sunny day? True
2) Is Singapore a European country? False

And I can define boolean variables which hold the above 2 bool result.

'''

# Step 1) define variable
is_sunny_day = True
is_european_country = False

# Step 2) Use variable
print('Is today a sunny day?', is_sunny_day)
print('Is Singapore a European country?', is_european_country)

print('Variable is_sunny_day type is:', type(is_sunny_day), '. Its value is:', is_sunny_day)
print('Variable is_european_country type is:', type(is_european_country), '. Its value is:', is_european_country)


# Compare 2 numbers, get a True / False bool value, assign the bool value to the a bool variable
# It is separated by '='
# on the left: variable
# on the right: 'boolean expression', which result in a boolean value.

# 1 > 2 is a boolean expression, and its value is False
# 1 < 2 is a boolean expression, and its value is True
bool3 = (1 > 2) # 1 > 2 is False, bool3's value is False
bool4 = (1 < 2) # 1 < 2 is True, bool4's value is True

print('bool3 type is:', type(bool3), '. bool3=', bool3)
print('bool4 type is:', type(bool4), '. bool4=', bool4)
