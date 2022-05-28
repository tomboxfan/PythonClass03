tup_1 = 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'

#Requirement: tell me the index of value 'a'

index_of_a = tup_1.index('a')
print(index_of_a) # 0

# index(value) finds the index of the 1st appearance of the value


index_of_a = tup_1.index('a', index_of_a + 1)
print(index_of_a) # 2


index_of_a = tup_1.index('a', index_of_a + 1)
print(index_of_a) # 4

