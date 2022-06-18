# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

enm1 = enumerate(l1)
print(enm1)
print(list(enm1))

# printing the tuples in object directly
for elm in enumerate(l1):
    print(elm)

# separate counter and element - normally we use like this
for counter, elm in enumerate(l1):
    print(counter, elm)

# changing index and printing separately
for count, elm in enumerate(l1, 100):
    print(count, elm)
