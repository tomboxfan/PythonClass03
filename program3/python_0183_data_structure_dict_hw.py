

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

print('----------------------------------')

print(stupid_dict['a']) # 1

print(stupid_dict[stupid_dict['a']]) # tuple("Hello")
'''
the above line equals to:
print(stupid_dict[1])
'''

print(stupid_dict[stupid_dict[stupid_dict['a']]])
'''
the above line equals to:
print(plane)
'''

print(stupid_dict[stupid_dict[stupid_dict['a']]]['name'])
'''
the above line equals to:
print(plane['name']) # 'Boeing 787'
'''



