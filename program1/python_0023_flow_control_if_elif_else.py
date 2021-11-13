
# Requirement: based on user input age, and tell whether the current user is a adult, a teenager, a kid or a baby.

age = int(input("How old are you? "))


'''
IMPORTANCE!! -------------------------------
if / elif / elif ... / else gives you multiple choices.
You check one after another, which one suits you.
Once you select a path, all the remaining path will be ignore.
--------------------------------------------
'''

if age >= 20:
    print("You are an adult now.")
    print("You can start a software programmer career.")
elif age >= 13:
    print("You are still a teenager")
    print("You should start taking some Python lesson")
elif age >= 3:
    print("You are still a kid")
    print("Play time at your age! Enjoy!")
else:
    print("You are still a baby")
    print("Eating, Drinking, Sleeping, Pooping, Crying ...")

print(f"You are {age} years old.")
