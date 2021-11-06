
years_learning_python = int(input("How many years have you been learning Python? "))


'''

if <boolean expression>:
    <statement>  <block 1>
    <statement>
    <statement>
else:
    <statement>  <block 2>
    <statement>
    
1) block 1 will be executed if boolean expression is True
2) block 2 will be executed if boolean expression is False
'''

if years_learning_python > 5:
    print(f"Not bad! {years_learning_python} years is quite a long time, you've already been a Python Guru!")
    print(f"I am sure you can earn a lot of money in the market!")
else:
    print(f"{years_learning_python} years is still quite short.")
    print("I know it is hard, just hang in there! Not everybody has the opportunity to learn Python!")
    print("You are really lucky")

print("Python is the future! You are on the right track!")