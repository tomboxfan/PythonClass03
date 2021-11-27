age = 15

if age < 18:
    kids_or_adult = 'kids'
else:
    kids_or_adult = 'adult'

# can be simplfied into

kids_or_adult = 'kids' if age < 18 else 'adult'
print(kids_or_adult)

'''
IMPORTANT!!! ----------------------------------------------------------------------------
<value_when_true>      if  <boolean expression>  else          <value_when_false>
-----------------------------------------------------------------------------------------
'''

fruit = 'Apple'
isApple = True if fruit == 'Apple' else False
print(isApple)

x = 18
result = 'High' if x > 10 else 'Low'
print(result)