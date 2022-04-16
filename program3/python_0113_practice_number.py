'''
Requirement:

Between 2000 and 3200, find all numbers which can be fully divided by 7 not 5

print them in one line, separated by comma

'''


'''
analysis:

i % 7 == 0 -> can be fully divided by 7
i % 5 != 0 -> cannot be fully divided by 5

'''

l = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        l.append(i)

print(l)

print(*l, sep=",")