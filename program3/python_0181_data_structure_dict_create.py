

print(f"1) empty dict ----------------")
dict1 = {}
print(type(dict1))
print(dict1)

print(f"2) with initial value ----------------")
car = {
    "brand": "BMW",
    "model" : "X5",
    "year": 2022
}

print(type(car))
print(car)


plane = {
    'name' : 'Boeing 787',
    'Role' : 'Wide-body jet airliner',
    'National origin' : 'United States',
    'First flight' : '	December 15, 2009',
    'passengers ': 242,
    'long': 57,
    'price': 151.5
}

print(plane)

students = {
    1: 'Tom',
    2: 'Billy',
    3: 'Sandy',
    4: 'Sue'
}

print(students)


print(f"3) with complex keys & values ----------------")

stock_prices = {
    'DBS': ('D05', 30.13, -0.23, 3640.2),
    'UOB': ('U11', 27.68, -0.37, 3621.7),
    'OCBC': ('O39', 11.61, -0.15, 7662.2)
}

print(stock_prices)

stupid_dict = {
    'a': 1,
    1: tuple("Hello"),
    tuple("Hello"): plane
}

print(stupid_dict)

'''
HOMEWORK: 
Please create at least 3 dict; each dict contains at least 3 pairs
'''