
toms_age = 20

'''
=       assign value on the right to the variable on the left
==      tells you whether the number/str on the left and right are equal to not, and give you a boolean value
toms_age == 20 is a boolean expression, and its value is True
'''
print('Is Tom 20 years old? ', toms_age == 20)

print('Is Tom 13 years old? ', toms_age == 13)

print('Tom is not 20 years old, Right? ', toms_age != 20)



# on the right, boolean expression, which gives you a boolean value
# on the left, boolean variable, which holds the boolean value
a = (toms_age == 20)
b = (toms_age == 13)
c = (toms_age != 20)
d = (toms_age != 13)
e = (toms_age < 30)
f = (toms_age <= 20)
g = (toms_age > 30)
h = (toms_age >= 30)
# print(a,b,c,d,e,f,g,h) # answer is here.
# HOMEWORK: without run my code, write you answer above, compare and tell me how many mistakes you made


# This is rubbish code, don't code in this way.
a = toms_age == 20
b = toms_age == 13
c = toms_age != 20
d = toms_age != 13
e = toms_age < 30
f = toms_age <= 20
g = toms_age > 30
h = toms_age >= 30

# assign operator (=) has a lower priority than the 6 rational operator

my_math_mark = 75

my_math_is_excellent = (my_math_mark > 90)
print("is my math excellent? ", my_math_is_excellent)

failed_in_math = (my_math_mark < 60)
print('Have I failed in Math? ', failed_in_math)

billy_math_mark = 75
billy_has_same_score_as_mine = (my_math_mark == billy_math_mark)
print("Does Billy have same score as mine?", billy_has_same_score_as_mine)

'''
challenging question 1) Without run my code, 
                        For each print statement of my code, 
                        Write on a paper, 
                        Write True if you think it will print True
                        Write False if you think it will print False
                        Then you can run my code, compare and tell me how many mistakes you made
                         
challenging question 2) Define several boolean variables 
                        Use these boolean variables, create boolean expressions as I do in my program
                        Your boolean expression should include ==, >, <, <=, >=, != 
'''



