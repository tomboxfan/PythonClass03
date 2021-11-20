'''
Requirement:
We have some students, based on their math / science / english score, we will assign them to the following classes.

Elite Class - all 3 subjects should have score higher than 85
Math Elite Class - Math score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
Science Elite Class - Science score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
English Elite Class - English score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
Express Class - average higher than 75 and no subject lower than 65
Normal Class - other students

You need to ask user to input math score / science score / english score from console, then assign them to the correct class.
'''






























# Step 0) Get score from console --------------------
math_score = float(input("Math:"))
science_score = float(input("Science:"))
english_score = float(input("English:"))


# Step 1) calculate the average score ---------------
average_score = (math_score + science_score + english_score) / 3
print(f"Your score: {math_score}, {science_score}, {english_score}. Average score: {average_score}")

# Step 2) Elite Class
if math_score > 85 and science_score > 85 and english_score > 85:
    class_name = 'Elite Class'

# Step 3) Check for Math Elite / Science Elite / English Elite
elif (math_score > 85 or science_score > 85 or english_score > 85) and average_score > 75 and math_score >= 70 and science_score >= 70 and english_score >= 70:

    if math_score > 85:
        class_name = 'Math Elite Class'
    elif science_score > 85:
        class_name = 'Science Elite Class'
    else:
        class_name = 'English Elite Class'


# Step 4) express class
elif average_score > 75 and math_score >= 65 and science_score >= 65 and english_score >= 65:
    class_name = "Express Class"

# Step 5) normal class
else:
    class_name = "Normal Class"

print(f"You are assigned to {class_name}")



