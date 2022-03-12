'''
Print all 3 digits 'daffodil numbers'.
A 'daffodil number' means
the cube of the number's unit digit +
the cube of the number's tens digit +
the cube of the number's hundreds digit = the number itself

For example:
153 = 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3
'''

'''
Logic:
1) 3 digits numbers range from 100 to 999.
   So I just need to try them all, check them one by one, see whether they are daffodil numbers or not.
   So I need to loop in range(100, 1000)
   

'''


for i in range(100, 1000):

    # // : floor division - find quotient
    # %  : modulus        - find remainder

    # 213 // 100 = 2
    # 213 % 100 = 13

    hundreds_digit = i // 100
    tens_digit = i % 100 // 10
    unit_digit = i % 10

    if hundreds_digit ** 3 + tens_digit ** 3 + unit_digit ** 3 == i:
        print(i)

'''
Our first algo - Complete Search / 枚举算法 / 枚举搜索.  (枚举 in English - Enum)  

'''