'''
Requirement:
Step 1) Ask player_a to input 'scissors', 'paper', 'stone', 'exit'.
Step 2) Use while loop, loop as long as player_a's input is NOT 'exit'.
Step 3) Inside the while loop body, you ask player_b to input 'scissors', 'paper', 'stone'.
Step 4) Use if / elif / else or nested if / elif / else to check who wins, print the result.
'''

# Step 1) Prepare the data / define the variables ------------------------------
user_a_choice = input("User A's choice (scissors / paper / stone / exit): ")

# Step 2) program begins --------------------------------
while user_a_choice != 'exit':
    user_b_choice = input("User B's choice (scissors / paper / stone): ")
    print(user_a_choice, user_b_choice)

    # HOMEWORK BEGIN ------------------------

    # HOMEWORK END   ------------------------

    print('-------------------------------------------------')
    user_a_choice = input("User A's choice (scissors / paper / stone / exit): ")