
# EXAMPLE 1: unpacking a tuple -----------------------------

'''
Requirement:
You have a long, sorted tuple, which contains the scores of the whole class
You need to remove the lowest and the highest scores, and get an average score of the whole class
'''

grades = (55, 57, 60, 67, 77, 78, 79, 83, 85, 99, 100)

# Solution 1) Slice

middle_score = grades[1:-1]
print(type(middle_score))
average_score = sum(middle_score) / len(middle_score)
print(average_score)



# Solution 2) unpacking
lowest, *middle_score, higest = grades
print(type(middle_score)) # middle_score is of type list
average_score = sum(middle_score) / len(middle_score)
print(average_score)



# EXAMPLE 2: unpacking a list ------------------------------------------

record1 = ['Tom', 'tomfan@hotmail.com', '91234567', '61234567', '81234567']
name, email, *phone_numbers = record1 # unpacking helps you group some values into a new list
print(phone_numbers)


record2 = ['Billy', 'billy@hotmail.com']
name, email, *phone_numbers = record2 # unpacking here generates an empty list
print(phone_numbers)


record3 = ['Billy', 'billy@hotmail.com', '91234567']
name, email, *phone_numbers = record3 # unpacking here generates a list which contains 1 single value
print(phone_numbers)

