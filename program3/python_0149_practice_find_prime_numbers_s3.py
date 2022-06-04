
def s3_check_prime_till_sqrt(upper_bound):

    check_times = 0
    prime_number_list = []

    for prime_candidate in range(2, upper_bound + 1): # for example, prime_candidate is 67

        sqrt_of_prime_candidate = int(prime_candidate ** 0.5) + 1  # sqrt_of_prime_candidate is 6.2 -> 6 -> 7


        '''
        traditional way --------------------------------------
        prime_to_be_checked = []
        for prime in prime_number_list:
            if prime <= sqrt_of_prime_candidate:
                prime_to_be_checked.append(prime)       # prime_to_be_checked list contains [2,3,5,7]
        '''

        # list comprehension -----------------------------------
        prime_to_be_checked = [prime        for prime in prime_number_list    if prime <= sqrt_of_prime_candidate]





        # for potential_factor in range(2, sqrt_of_prime_candidate + 1):   this is solution 2
        for potential_factor in prime_to_be_checked:  # if prime candidate is 41, check from 2 to 7
            check_times += 1
            if prime_candidate % potential_factor == 0:
                break
        else:
            prime_number_list.append(prime_candidate)




    print(f"In total, it takes {check_times} times. ")
    return prime_number_list


upper_boundary = 10_000
l1 = s3_check_prime_till_sqrt(upper_boundary)
print(l1)
