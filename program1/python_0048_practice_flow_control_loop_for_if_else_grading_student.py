'''
https://www.hackerrank.com/challenges/grading/
'''

'''
Requirement:
Step 1) Get student count from console. Ask user to tell you how many students in total. 
Step 2) For each student, let user to input the student score.
Step 3) If the difference between the score and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
        If the score is less than 58, no rounding occurs, as it is a failing score.
        For example: score = 84, round to 85 (because 85 - 84 less than 3)
                     score = 57, no rounding (because 57 is less than 58)
                     score = 67, no rounding ( because 70 - 67 is 3 or greater)
Step 4) Print the final score for the student
'''
































student_count = int(input("How many student: "))

for student_no in range(student_count):

    score = int(input("Score is: "))

    if score % 5 >= 3 and score >= 58:
        score = score + (5 - score % 5)

    print(score)

