'''
Requirement:
1) Let user to input a number from console
2) Print out a) How many digits the number has.
             b) the reverse number
'''


def answer():
    num = input("Show me the number: ")
    print(f"The number has {len(num)} digits")
    print(f"The reverse number is: {num[::-1]}")

answer()