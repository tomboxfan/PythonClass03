'''
Requirement:
factorize number x (1 <= x <= 1000), print out the result.

For example:
When user inputs 90, your program should print:
90 = 2 * 3 * 3 * 5
'''

'''
Key Logic:
Find out all prime numbers below 1000, try all prime numbers smaller than x.
Then I can find all the prime factors of x.

Step 1) Find out all prime numbers within 1000, put into a list prime_list
        I define a function:
        def find_all_primes(upper_boundary):
            pass

Step 2) Find out all prime factors of X using prime_list, put the prime factors into list prime_factors
        I define a function:
        def find_all_prime_factors(x, prime_list):
            pass
            
Step 3) Print out the result using number x and its prime_factors
        I define a function:
        def print_result(x, prime_factors):
            pass
'''

def find_all_primes(upper_boundary):
    '''
    This finds all prime numbers smaller than upper_boundary
    :param upper_boundary: the upper boundary
    :return: a list of prime numbers smaller than the upper boundary
    '''
    prime_list = []

    for prime_candidate in range(2, upper_boundary+1):
        # I can define another function, to tell whether the prime_candidate is prime or not
        if is_prime(prime_candidate):
            prime_list.append(prime_candidate)

    return prime_list


def is_prime(prime_candidate):
    '''
    tell whether the prime_candidate is prime number or not

    :param prime_candidate:
    :return: True if prime_candidate is a prime number
    '''
    for potential_factor in range(2, prime_candidate):
        if prime_candidate % potential_factor == 0:
            return False
    return True


# Do some coding, do some testing
# prime_list = find_all_primes(1000)
# print(prime_list)



def find_all_prime_factors(x, prime_list):

    prime_factors = []

    for prime in prime_list:
        # because x can contain multiple same prime factors, so we have to use 'while'
        while x % prime == 0:
            # prime is a prime factor of x, so add prime to list prime_factors
            prime_factors.append(prime)
            # remove prime from x
            x = x // prime

    return prime_factors


# Do some coding, do some testing
# prime_factors = find_all_prime_factors(8, prime_list)
# print(prime_factors)


def print_result(x, prime_factors):
    print(x, "=", end = ' ')

    # Solution 1 star unpacking
    print(*prime_factors, sep = ' * ')

    # Solution 2 list comprehension
    # print(' * '.join([str(elem) for elem in prime_factors]))


# Do some coding, do some testing
# print_result(100, prime_factors)


'''
-------------------------------------------------
Now all basic functions have been defined
Let's start our real code!
-------------------------------------------------
'''

# Step 1) Find out all prime numbers within 1000, put into list prime_list
prime_list = find_all_primes(1000)

# Step 2) Find out all prime factors of x using prime list, put the prime factors into list prime_factors
x = int(input("X = "))
prime_factors = find_all_prime_factors(x, prime_list)

# Step 3) Print out the result using number x and its prime factors
print_result(x, prime_factors)

