def square(x):
    return x*x


f = square(5)

print(square)
print(f)

f = square

print(square)
print(f)

print(square(4))
print(f(4))

del square 
# print(square)
print(f)
