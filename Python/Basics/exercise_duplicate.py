some_list = ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'f', 'c']
new_list = []
for var1 in some_list:
    if some_list.count(var1) > 1 and new_list.count(var1) <= 0:
        new_list.append(var1)
print(new_list)
new_list.clear()
# another solution from ZTM tutorial
for var1 in some_list:
    if some_list.count(var1) > 1:
        if var1 not in new_list:
            new_list.append(var1)
print(new_list)
