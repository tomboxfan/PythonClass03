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


print('\n\n--------------------------------\n\n')


'''
parallelogram
1st line: 9 ' ' + 10 '*'
2nd line: 8 ' ' + 10 '*'
...
10th line: 0 ' ' + 10 '*'

Summary: 
Loop 0 - 9: print 9,8,7,6...0 ' ' + then print 10 '*'
'''

for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * 10)


print('\n\n--------------------------------\n\n')

'''
obtuse 1
'''

for line_number in range(10):
    print(' ' * line_number + '*' * (line_number + 1))


print('\n\n--------------------------------\n\n')

'''
obtuse 2
read for 10th line:
10th line: 0 ' ' + 10 '*'
9th line: 2 ' ' + 9 '*'
...
1st line: 18 ' ' + 1 '*'

Summary: 
Loop 0 - 9: print 18,16...0 ' ' + then print 1,2,3..10 '*'
'''

for line_number in range(10):
    print(' ' * (18 - line_number * 2) + '*' * (line_number + 1))


print('\n\n--------------------------------\n\n')

'''
hourglass
19 lines in total
read from 1st line:
1st line: 0 ' ' + 19 '*'
2nd line: 1 ' ' + 17 '*'
....
9th line: 8 ' ' + 3 '*'
10th line: 9 ' ' + 1 '*'
11th line: 8 ' ' + 3 '*'
...
19th line: 0 ' ' + 19 '*'

summary:
because it is symmetrical, so I loop in range(-9,10)
Loop -9 to 9: print 0,1,2,3....8,9,8....1,0 ' '; then print 19,17,15....3,1,3,...15,17,19 '*'
'''

for line_number in range(-9, 10):
    print(' ' * (9 - abs(line_number)) + '*' * (abs(line_number * 2) + 1))


print('\n\n--------------------------------\n\n')

'''
pinetree

we know how to print single isosceles:

for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * (line_number * 2 + 1))

how to print triple isosceles triangle in 1 single for loop?
single isosceles triangle loop in range(10) -> 10 numbers, 0 - 9
triple isosceles triangle loop in range(30) -> 30 numbers, 0 - 9 and 10 - 19 and 20 - 29

Question: how to make 10 -19 and 20 - 29 similar to 0 - 9
Answer: Use % 10
'''


for line_number in range(30):
    print(' ' * (9 - line_number % 10) + '*' * (line_number % 10 * 2 + 1))

print('\n\n--------------------------------\n\n')

'''
rhombus
19 lines in total
read from 1st line:
1st line: 9 ' ' + 1 '*'
2nd line: 8 ' ' + 3 '*'
...
9th line: 1 ' ' + 17 '*'
10th line: 0 ' ' + 19 '*'
...
19th line: 9 ' ' + 1 '8'
'''

for line_number in range(-9, 10):
    print(' ' * abs(line_number) + '*' * (19 -abs(line_number) * 2))
