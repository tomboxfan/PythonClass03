'''
Input a student's score.
if it is equals to 90 or above, your program prints 'A'
if it is equals to 60 or above, your program prints 'B'
other score, print 'C'
'''

score = int(input("Your score:"))

if score >= 90:
    print('A')
elif score >= 60:
    print('B')
else:
    print('C')