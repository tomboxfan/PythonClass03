normal_dict= {}

for i in range(10):

    if i not in normal_dict:
        normal_dict[i] = 0

    normal_dict[i] += 1

print(normal_dict)







from collections import defaultdict

default_dict = defaultdict(int)

for i in range(10):
    default_dict[i] += 1 # You don't need to check, whether the key in the dict or not. You can directly use it.

print(default_dict)