'''

Requirement:
implement below function

def find_primes(upper_bound):
    pass


You pass a number, say, 1000, then the function should return a list which contains all prime numbers smaller than upper_bound 1000.
'''

def s1_brute_force(upper_bound):

    check_times = 0
    prime_number_list = []

    for prime_candidate in range(2, upper_bound + 1):

        for potential_factor in range(2, prime_candidate):
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



l1 = s1_brute_force(100000)
print(l1)
