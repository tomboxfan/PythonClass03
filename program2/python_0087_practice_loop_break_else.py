'''
Requirement: find all prime numbers less than 100, using loop break else
'''





























# Step 1) I need to loop from 2 to 100, check all thsse numbers one by one
for prime_candidate in range(2, 101):

    # Step 2) For each number prime_candidate, I will loop from 2 to prime_candidate(exclusive)
    for potential_factor in range(2, prime_candidate):
        if prime_candidate % potential_factor == 0:
            print(f"{prime_candidate} is not a prime number")
            break
    else:
        print(f"{prime_candidate} is a prime number")

