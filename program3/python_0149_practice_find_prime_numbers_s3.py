
def s3_check_prime_till_sqrt(upper_bound):

    check_times = 0
    prime_number_list = []

    for prime_candidate in range(2, upper_bound + 1):

        sqrt_of_prime_candidate = int(prime_candidate ** 0.5) + 1

        for potential_factor in range(2, sqrt_of_prime_candidate + 1): # if prime candidate is 41, check from 2 to 7


            # We only check prime numbers

            # HOMEWORK:
            # Enhance this program, so that we won't check 2,3,4,5,6,7 for 41,
            # we check only 2,3,5,7 for 41

            pass # replace your actual code with 'pass'

        else:
            prime_number_list.append(prime_candidate)

        '''
        if break clause is not triggered, else cause will be triggered.
        '''

    print(f"In total, it takes {check_times} times. ")
    return prime_number_list


upper_boundary = 1000
l1 = s3_check_prime_till_sqrt(1000)
print(l1)
