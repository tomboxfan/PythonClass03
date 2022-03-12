

'''
Logic:

i is of type int
we can use str(i) to convert int i to str i_str

str is quite similar to list

i                is  int 123

i_str            is  str '123'

i_str[0]         is  str '1'
i_str[1]         is  str '2'
i_str[2]         is  str '3'

int(i_str[0])    is  int 1
int(i_str[1])    is  int 2
int(i_str[2])    is  int 3



Block Edit mode: Alt + Shift + Insert (Win) / Command + Shift + 8 (Mac)


'''



for i in range(100, 1000):

    i_str = str(i)
    hundreds_digit = int(i_str[0])
    tens_digit = int(i_str[1])
    unit_digit = int(i_str[2])

    if hundreds_digit ** 3 + tens_digit ** 3 + unit_digit ** 3 == i:
        print(i)


'''
What we've learnt:
1) str is quite similar to list
2) int can be easily converted to str, and back forth
'''