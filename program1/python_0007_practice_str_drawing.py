# Requirement: print a square with length=5


# Example 1)
# Let's print a small square 2 * 2
star_line = '*' * 2
print(star_line)
print(star_line)


print('-------------------------------------------')


star_line = '*' * 5
print(star_line)
print(star_line)
print(star_line)
print(star_line)
print(star_line)

print('-------------------------------------------')

'''
IMPORTANCE!!! -----------------------------------------
Q) How to adjust line spacing in PyCharm Console? 
A) double click 'shift' -> type 'Console Font' -> Tick 'Use Console font instead of the default' -> Adjust 'line spacing' to 0.8
-------------------------------------------------------
'''

# I want the square do not close to the far left, I want it move to the middle. So,
# Step 1) 5 ' ' in the front.
# Step 2) 5 '*' follows the 5 spaces

star_line = ' ' * 5 + '*' * 5
print(star_line)
print(star_line)
print(star_line)
print(star_line)
print(star_line)

print('-------------------------------------------')

# I want to print a hollow square
# between the upper border and lower border, each line is
# 1) 5 ' ' in the left
# 2) 1 '*' (left border) + (5 - 2) spaces, and 1 '*' (right border)
# how many rows should I print? 5 - 2 = 3
left_star_right_star = ' ' * 5 + '*' + ' ' * 3 + '*'

print(star_line)
print(left_star_right_star)
print(left_star_right_star)
print(left_star_right_star)
print(star_line)

print('-------------------------------------------')


'''
HOMEWORK: 
According to python_0007_practice_str_drawing_to_students.xlsx
print P Y T H O N 6 letters in the pycharm console.
'''