'''
Requirement:
Babylonian square-root algorithm is very famous!
中文叫作巴比伦算法

Here it is how it works to calculate the square root of any number x:

Step 1) define variable a = 1
Step 2) define variable b = x / a

Step 3) assign variable a = (a + b) / 2     -   Now a stands in the mid point of a and b. This is to move a closer to b
Step 4) assign variable b = x / a

Because square_root * square_root = x; so a and b, one is smaller than square_root, another is bigger than square_root
We move a to the mid point between a and b, so we make a closer to the square_root
because a * b = x, if a is closer to the square_root, b is also closer to the square_root


Step 5) assign variable a = (a + b) / 2
Step 6) assign variable b = x / a

Step 7) assign variable a = (a + b) / 2
Step 8) assign variable b = x / a

repeat..repeat..

until a and b are close enough, say abs(b - a) < 0.000000000001
Then a is equal to b (almost)
Then a or b is the square root of x


Example:
Let's calculate the square root of 25
a = 1
b = 25 / 1 = 25

a = (1 + 25) / 2 = 13             b = 25 / 13 = 1.923             diff = 11.077
a = (13 + 1.923) / 2 = 7.462      b = 25 / 7.462 = 3.351          diff = 4.111
a = (7.462 + 3.351) / 2 = 5.406   b = 25 / 5.406 = 4.624          diff = 0.782
... ...

'''