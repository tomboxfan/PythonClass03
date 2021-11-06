#Requirement: Mimic online game user login


# define a multi-line str variable as the welcome message
# a multi-line str is surrounded by a pair of triple quote
welcome_msg = '''
***********************************
    Welcome to King of Glory
***********************************
'''

print(welcome_msg)


user_name = input("User Name: ")
password = input("Password: ")


real_password = "1q9*"

'''
Requirement: 
if user types the correct password, then you let him to continue
otherwise, you should stop the program

HOMEWORK:
Use if / else to check.

If user has given you a correct password, then you say: password is correct
else: 
    password is wrong.
    exit() 
'''



print(f"Welcome, {user_name}! You've successfully logged in the game!")

total_coins = 0

short_of_coins_msg = f"Unfortunately, you have only {total_coins} coins in your account. Please top up your account."
print(short_of_coins_msg)


coins_topup_str = input("Total coins to top up: ") # str type
coins_topup = int(coins_topup_str) # int typ

total_coins += coins_topup

print(f"Now you have coins: {total_coins}. You can continue to play the game.")


'''
Requirement: 
if user tops up coins less than 500, you should tell the user, you still do not have enough coins.
if user tops up coins greater than 500, tell the user, you can continue to play

Use if/else as well.

'''