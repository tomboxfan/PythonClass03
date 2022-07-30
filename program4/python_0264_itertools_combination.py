from itertools import combinations

combi_set = set(combinations(range(1, 6), 3)) # pass a range to combinations function, which gives you a combination object
print(combi_set)

combi_tuple = tuple(combinations({1, 2, 3}, 2)) # pass a set to combinations function, which gives you a combination object
print(combi_tuple)

combi_list = list(combinations({1:'a', 2:'b', 3:'c'}, 2)) # pass a dict to combinations function, which gives you a combination object
print(combi_list)

