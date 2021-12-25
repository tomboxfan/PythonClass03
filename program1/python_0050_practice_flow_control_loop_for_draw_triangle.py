'''
Right triangle 1
1st line: 1 '*'
2nd line: 2 '*'
...
10th line: 10 '*'

Summary:
Loop 0 - 9: print 1,2,3...10 '*'
'''

for line_number in range(10):
    print('*' * (line_number + 1))

print('\n\n--------------------------------\n\n')


'''
Right triangle 2
1st line: 9 ' ' + 1 '*'
2nd line: 8 ' ' + 2 '*'
...
10th line: 0 ' ' + 10 '*'

Summary: 
Loop 0 - 9: print 9,8,7,6...0 ' ' + 1,2,3...10 '*'
'''

for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * (line_number + 1))

print('\n\n--------------------------------\n\n')

'''
isosceles triangle
1st line: 9 ' ' + 1 '*'
2nd line: 8 ' ' + 3 '*'
...
10th line: 0 ' ' + 19 '*'

Summary: 
Loop 0 - 9: print 9,8,7,6...0 ' ' + 1,3,5...19 '*'
'''

for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * (line_number * 2 + 1))
