# 125 * 3 + 125 * 5 + 25 * 3 + 25

# Step 1) define variables
# I see there are following numbers in the expression:
# 125 / 3 / 5/ 25
# So I need to define 4 variables
a = 125
b = 3
c = 5
d = 25

# Step 2) use the variables
answer_of_q1 = a * b + a * c + d * b + d
print("125 * 3 + 125 * 5 + 25 * 3 + 25", "=", answer_of_q1)

# Question 2) 9999 * 3 + 101 * 11 * (101 - 92)
a = 9999
b = 3
c = 101
d = 11
e = 92

answer_of_q2 = a * b + c * d * (c - e)
print("9999 * 3 + 101 * 11 * (101 - 92)", "=", answer_of_q2)
