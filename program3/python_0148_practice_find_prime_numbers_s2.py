
def s2_check_till_sqrt(upper_bound):

    check_times = 0
    prime_number_list = []

    for prime_candidate in range(2, upper_bound + 1):

        sqrt_of_prime_candidate = int(prime_candidate ** 0.5) + 1

        for potential_factor in range(2, sqrt_of_prime_candidate + 1): # if prime candidate is 41, check from 2 to 7
            check_times += 1
            if prime_candidate % potential_factor == 0:
                break
        else:
            prime_number_list.append(prime_candidate)

        '''
        if break clause is not triggered, else cause will be triggered.
        '''

    print(f"In total, it takes {check_times} times. ")
    return prime_number_list


'''
HOMEWORK:
Explain clearly, why if we check till square root, then it is good enough already? 
'''


l1 = s2_check_till_sqrt(10000)
print(l1)
