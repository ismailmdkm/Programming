'''
logical and
'''
a, b, c = 0, -5, 10
if a > 0 and b > 0:
    print("Both number greater than zero")
else:
    print("At lease on number is less than zero")
if (b > 0) or (c > 0):
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
if a or b or c:
    print("Atleast one number has boolean value as True")
else:
    print("All the numbers have boolean value as False")
if not a:
    print("Boolean value of a is False")
print(bool(a), bool(b), bool(c))
