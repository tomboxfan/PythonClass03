
'''
------------------------------------------------
Requirement
------------------------------------------------
There are 2 table tennis teams.
1st team has 3 players: A / B / C
2nd team has 3 players: X / Y / Z

We know the following facts:

A's opponent is not X.
C's opponent is neither X or Z.

Please write a program to find out A/B/C's opponents.
'''

'''
Logic:
based on several rules we need to match:
a/b/c vs x/y/z

1) a not vs x
2) c not vs x
3) c not vs z

because c is the most restrictive, so let's figure out c's opponent first.
a is less restrictive, so let's figure out a's opponent next.
b is the least restrictive, so let's figure out c's opponent last.
'''
























# Step 1) let's define 3 variables
a_opponent = ''
b_opponent = ''
c_opponent = ''




# Step 2) Let's figure out c_opponent
for i in 'xyz':
    if i != 'x' and i != 'z':
        c_opponent = i

print(f"c vs {c_opponent}")


# Step 3) Let's figure out a_opponent
for i in 'xyz':
    if i != 'x' and i != c_opponent:
        a_opponent = i

print(f"a vs {a_opponent}")



# Step 4) Let's figure out b_opponent
for i in 'xyz':
    if i != a_opponent and i != c_opponent:
        b_opponent = i

print(f"b vs {b_opponent}")

