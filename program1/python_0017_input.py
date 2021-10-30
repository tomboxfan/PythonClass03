


# IMPORTANCE !!! ------------------------------------------------
# built-in function input(): accept user input from console, as some variable's value
# so we don't know your_name's value until program runs to below line
# As soon as the program runs to the line input(), program halts. The control goes to you - the user.
# it waits until user type his name and 'ENTER' in the console.
# Then the control goes back to the program immediately, program proceeds.
#
# Summary:
# input() function will read user input value as a 'str' / as a 'str' / as a 'str', assign it to your_name variable.
#----------------------------------------------------------------
your_name = input('Your name:')



print(f"Hello, {your_name}")

print(f"Variable your_name's type is: {type(your_name)}")