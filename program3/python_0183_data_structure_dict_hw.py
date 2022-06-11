

plane = {
    'name' : 'Boeing 787',
    'Role' : 'Wide-body jet airliner',
    'National origin' : 'United States',
    'First flight' : 'December 15, 2009',
    'passengers ': 242,
    'long': 57,
    'price': 151.5
}


stupid_dict = {
    'a': 1,
    1: tuple("Hello"),
    tuple("Hello"): plane
}

print(stupid_dict)

'''
Without run my code, tell me the output of these 3 lines:

print(stupid_dict['a'])
print(stupid_dict[stupid_dict['a']])
print(stupid_dict[stupid_dict[stupid_dict['a']]])
print(stupid_dict[stupid_dict[stupid_dict['a']]]['name'])
'''

