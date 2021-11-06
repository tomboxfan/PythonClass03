'''
Requirement:
1) Ask user to input a number from console
2) Then you need to tell whether the number is a square number or not
'''

user_input_str = input("Please input a number: ")
number_a = int(user_input_str)

number_a_square_root = number_a ** (1/2)  # float type
print(f"{number_a}'s square root is {number_a_square_root:.2f}")

number_a_square_root_int = int(number_a_square_root)
print(f"After I convert {number_a_square_root:.2f} to integer, its value is {number_a_square_root_int}")

if number_a_square_root == number_a_square_root_int:
    print(f"{number_a} is a square number.")
else:
    print(f"{number_a} is not a square number.")

'''
We replace {number_a_square_root} to {number_a_square_root:.2f}, to format the float number on the console.

':.2f' has 3 parts:
:       means   I want to format the number
.2      means   keep 2 digits after the decimal point
f       means   this is a float number
'''