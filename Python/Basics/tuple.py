fruits = ("apple", "banana", "cherry", "apple", "pear")
print(len(fruits))
fruits = ("apple",)
print(type(fruits))
fruits = ("apple")
print(type(fruits))
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
fruits = tuple(("apple", 'banana', "cherry"))  # note the double round-brackets
print(fruits)
fruits = ("apple", "banana", "cherry", "plum", "pear")
print(fruits[1])
print(fruits[-1])
print(fruits[2:4])
print(fruits[:4])
print(fruits[2:])
print(fruits[-4:-1])
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits tuple")
y = list(fruits)
y[1] = "kiwi"
# tuple[1] = "kiwi"
print(y)
print(fruits)
fruits = ("apple", "banana", "cherry")
(green, yellow,red) = fruits
print(green)
print(yellow)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
print(type(green))
print(type(yellow))
print(type(red))
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
