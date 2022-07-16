car = {
    "brand": "BMW",
    "model": "X5",
    "year": 2021
}

print("Solution 1) .values() --> loop through a dict's values --------------------------")
for value in car.values():
    print(value, end = ' ')

print("\n\nSolution 2) .keys() --> loop through a dict's values --------------------------")
for key in car.keys():
    print(key, '->', car[key])

print("\nSolution 3) .items() --> Loop through a dict's key and value ---------------------")
for key, value in car.items():
    print(key, '->', value)


print("\nSolution 4) if you put nothing behind, it equals to loop dict key ---------------------")
for key in car:
    print(key)






'''
car.items() returns a list of tuple
so here, car.items() returns:
[("brand", "BMW"),("model", "X5"),("year", 2021)]
'''

print("\n\nuse function len() to tell dict's size")
print(f"size of dict car is: {len(car)}")