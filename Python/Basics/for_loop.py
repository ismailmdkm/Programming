'''
for loop
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print("-" * 80)
for x in "ibu":
    print(x)
print("-" * 80)
for x in fruits:
    if x == "banana":
        break
    print(x)
else:
    print("Finally finished!")
print("-" * 80)
for x in fruits:
    if x == "banana":
        continue
    print(x)
print("-" * 80)
adj = ["red", "big", "tasty"]
for x in adj:
    for y in fruits:
        print(x, y)
