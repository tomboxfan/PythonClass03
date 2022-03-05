



# example 1: there is no break inside the for loop, so 'break' can not be triggered
# 'break' is not triggered -> 'else' clause will be triggered

for i in range(5):
    print(i)
else:
    print("For loop finished all iterations, no break happens! Else clause is triggered!")


print('-----------------------------------------')


# example 2 - 'break' will be triggered when i = 3
# 'break' is triggered -> 'else' clause will not be triggered.

for i in range(5):
    print(i)
    if i > 2:
        print('i is greater than 2 now!')
        break
else:
    print("For loop finished all iterations, no break happens! Else clause is triggered!")