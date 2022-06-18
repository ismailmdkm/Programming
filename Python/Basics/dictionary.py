'''
Dictionary
'''
print("*" * 80)
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2009,
    "autogear": True
}
print(car)
print(car.keys())
print(car.values())
print(car["brand"])
x = car["model"]
print(x)
y = car.get("year")
print(y)
z = car.get("invalidkey")
print(z)
items_list = car.items()
print(items_list)
car["color"] = "grey"
car["autogear"] = False
print(items_list)
car.update({"year": 2010})
car.update({"cruise": False, "year": 2011})
print(car)
z = car.pop("model")
print(z)
print(car)
car.popitem()
print(car)
del car["autogear"]
print(car)
car1 = car
car2 = car.copy()
car3 = dict(car)
car.pop("year")
print("Car:" + str(car))
print("Car1:" + str(car1))
print("Car2:" + str(car2))
print("Car3:" + str(car3))
del car1
car3.clear()
print("Car3:" + str(car3))
# print("Car3:" + str(car1))
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary")
print("*" * 80)
