# Requirement: get input from the user about his height in meters and weight in kg.
# Calculate his bmi based on this formula:
# bmi = weight / (height ** 2)
# Print information based user's bmi value
# bmi in [0, 16)    : You are severely underweight
# bmi in [16, 18.5) : You are underweight
# bmi in [18.5, 25) : You are healthy
# bmi in [25, 30)   : You are overweight
# bmi in [30, max)  : You are severely overweight

height = float(input("Height in meters: "))

weight_str = input("Weight in kg: ")
weight = float(weight_str)

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.3f}")

if bmi < 16:
    print("You are severely underweight")
elif 16 <= bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You are healthy")
elif 25 <= bmi < 30:
    print("You are overweight")
else:
    print("You are severely overweight")