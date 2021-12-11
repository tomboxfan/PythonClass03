# Requirement:
# Continuously get user input from console, ask user to input a number
# If the number is divisible by 7, then tell the user "The number is divisible by 7! Program exit!"
# Otherwise, ask user to try again.

















'''
----------------
Thinking Logic
----------------
The requirement is to continuously get a number from user.
We first work out a simple version, no loop at all, read 1 number from user.
'''

while True:

    # step 1) define the variable
    input_number = int(input("Please input a number: "))

    # step 2) use the variable
    if input_number % 7 == 0:
        print(f"{input_number} is divisible by 7! Program exit!")
        break
    else:
        print(f"{input_number} is NOT divisible by 7! Please try again!")


print("Program exit!")






