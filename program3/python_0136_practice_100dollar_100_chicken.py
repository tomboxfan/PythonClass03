'''

rooster $5 each
hen     $3 each
chick   3 for $1

You need to spend exactly $100, buy exactly 100 rooster / hen / chick in total.
Print out all possibilities.
'''


'''
Thinking logic:

$100, if we use all the money to buy rooster, we can buy 20
$100, if we use all the money to buy hen, we can buy 33 
So we can use nested loop to cover all situations
'''

for rooster_count in range(21): # to cover situation from 0 rooster to 20 rooster
    for hen_count in range(34): # to cover situation from 0 hen to 33 hen
        chick_count = 100 - rooster_count - hen_count

        # check no.1 chick_count has to be multiple of 3
        if chick_count % 3 != 0:
            continue

        # check no.2 all cost equals to $100
        if rooster_count * 5 + hen_count * 3 + chick_count // 3 == 100:
            print(f"Rooster: {rooster_count}, Hen: {hen_count}, Chick: {chick_count}")

'''
This algorithm is called 'Complete Search', also known as 'Brute Force'.
It means: try all possibilities
It simply takes advantage of the computer power to exhaust all situations.

Many Q in Competitive Programming are of this type. 
'''

