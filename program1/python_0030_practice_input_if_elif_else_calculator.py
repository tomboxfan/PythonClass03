# Requirement: implement a calculator which supports + - * / ** between 2 numbers.

float_a = float(input("A: "))
float_b = float(input("B: "))
operator = input("Operator: ")

if operator == '+':
    result = float_a + float_b
elif operator == '-':
    result = float_a - float_b
elif operator == '*':
    result = float_a * float_b
elif operator == '/':
    if float_b == 0:
        print("Wrong input!")
        exit()
    else:
        result = float_a / float_b
elif operator == '**':
    result = float_a ** float_b
else:
    print(f"Unrecoginized operator {operator}")
    exit()


print(f"{float_a} {operator} {float_b} = {result:.2f}")