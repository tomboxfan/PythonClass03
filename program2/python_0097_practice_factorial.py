'''
================
Homework
================
1) read from console for numbers
2) As long as it is greater than 0, calculate its factorial value.
3) Plus together, print the result


================
I expect to see:
================

Next number: 1
Factorial for 1 is: 1
Total factorial is: 1
------------------------------------
Next number: 2
Factorial for 2 is: 2
Total factorial is: 3
------------------------------------
Next number: 3
Factorial for 3 is: 6
Total factorial is: 9
------------------------------------
Next number: 4
Factorial for 4 is: 24
Total factorial is: 33
------------------------------------
Next number: -1
Quit!



================
Notes
================
A number's factorial value is continuous multiplication, from 1 to the number itself.
For example,
3's factorial is 1 * 2 * 3 = 6                  -> 3!
5's factorial is 1 * 2 * 3 * 4 * 5 = 120        -> 5!
'''


total = 0

while True:

    # read x from console
    x = int(input("Next number:"))

    # check x parameter
    if x <= 0:
        print("Quit!")
        exit()

    # calculate factorial of x
    factorial = 1
    for i in range(2, x+1):
        factorial *= i

    print(f"Factorial for {x} is: {factorial}")

    # calculate total factorials
    total += factorial
    print(f"Total factorial is: {total}")
    print("-----------------------------------")

