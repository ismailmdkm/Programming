thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
thisset = {"apple", "banana", "cherry","apple"} # duplicate values ignored
print(thisset)
print(len(thisset))
print("banana" in thisset) # check if banana is present in this set
thisset.add("orange")
print(thisset)
tropical = {"pineapple", "mango", "banana","papaya"}
thisset.update(tropical)
print(thisset)
mylist = ["kiwi", "orange"] # add any iterable
thisset.update(mylist)
print(thisset)
thisset.remove("banana")
#thisset.remove("unknown")
print(thisset)
thisset.discard("cherry")
#thisset.discard("unknown")
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
thisset.clear()
print(thisset)
del thisset
#print(thisset)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(x)
print(z)
x.intersection_update(y)
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(x)
print(z)
x.symmetric_difference_update(y)
print(x)
