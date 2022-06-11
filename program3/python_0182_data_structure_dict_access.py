car = {
    "brand": "BMW",
    "model" : "X5",
    "year": 2022
}

print(car)

print("read value from the dictionary --------------------")

print(car['brand'])
print(car['model'])
print(car['year'])


'''
if it is list, then the code looks like this: 

l = ['a', 'b', 'c']
print(l[0])
print(l[1])
'''


# if key doesn't exist in dictionary, your code will go wrong!
# print(car['price'])


print("Assign new value to the key --------------------------")
car['year'] = 2020 # override existing value
print(car)

car['color'] = 'red' # add new key-value pair
print(car)


print("check if key exists in dictionary or not ---------------------------")

year_in_car = "year" in car
print(f"Does key 'year' exist in car? {year_in_car}")

price_not_in_car = "price" not in car
print(f"key 'price' doesn't exist in car, am I right? {price_not_in_car}")


if 'price' not in car:
    car['price'] = 20000000
print(f"Car price is: {car['price']}")


print('delete key / value pair: use del -------------------------------------')
del car['brand']
print(car)

'''
Homework: type and run this code


'''