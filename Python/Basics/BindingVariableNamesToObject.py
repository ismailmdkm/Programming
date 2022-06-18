a = "first"
b = "first"
print(id(a))
print(id(b))
print(id("first"))
print(a is b)
print(a is "first")
print(a == b)
print(a == "first")

a = [10, 20, 30]
b = [10, 20, 30]
print(id(a))
print(id(b))
print(id([10, 20, 30]))
print(a is b)
print(a is [10, 20, 30])
print(a == b)
print(a == [10, 20, 30])