car = {
    "brand": "BMW",
    "model": "X5",
    "year": 2021
}


print("pop(key) - remove key / value pair from dict -------------------------------")
car_model = car.pop("model")
print(car_model) # X5
print(car) # {'brand': 'BMW', 'year': 2021}                 model is gone


print("popitem() - remove the last key / value pair from dict ---------------------")
item = car.popitem() # item is a tuple
print(item) # ('year', 2021)
print(car) # {'brand': 'BMW'}


print("clear() - remove all from the dict -----------------------------------------")
car.clear()
print(car) # {}