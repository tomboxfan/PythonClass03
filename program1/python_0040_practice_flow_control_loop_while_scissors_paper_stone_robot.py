import random





# Step 1) Prepare the data / define the variables ------------------------------
user_a_choice = input("User A's choice (scissors / paper / stone / exit): ")

# Step 2) program begins --------------------------------
while user_a_choice != 'exit':
    
    robot_choice = random.randint(1, 3)
    if robot_choice == 1:
        user_b_choice = 'scissors'
    elif robot_choice == 2:
        user_b_choice = 'paper'
    else:
        user_b_choice = 'stone'

    print(user_a_choice, user_b_choice)

    # HOMEWORK BEGIN ------------------------
    if user_a_choice == 'scissors':
        if user_b_choice == 'scissors':
            print(f"User A {user_a_choice}, User B {user_b_choice}: Draw.")
        elif user_b_choice == 'paper':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User A wins.")
        elif user_b_choice == 'stone':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User B wins.")
        else:
            print(f"User B inputs a wrong choice: {user_b_choice}")
    elif user_a_choice == 'paper':
        if user_b_choice == 'scissors':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User B wins.")
        elif user_b_choice == 'paper':
            print(f"User A {user_a_choice}, User B {user_b_choice}: Draw.")
        elif user_b_choice == 'stone':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User A wins.")
        else:
            print(f"User B inputs a wrong choice: {user_b_choice}")
    elif user_a_choice == 'stone':
        if user_b_choice == 'scissors':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User A wins.")
        elif user_b_choice == 'paper':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User B wins.")
        elif user_b_choice == 'stone':
            print(f"User A {user_a_choice}, User B {user_b_choice}: Draw.")
        else:
            print(f"User B inputs a wrong choice: {user_b_choice}")
    else:
        print(f"User A inputs a wrong choice: {user_a_choice}")
    # HOMEWORK END   ------------------------

    print('-------------------------------------------------')
    user_a_choice = input("User A's choice (scissors / paper / stone / exit): ")