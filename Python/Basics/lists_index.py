'''
Lists index usage
'''
this_list = ["apple", "banana", "cherry", "orange", "kiwi"]
print(this_list[1])
print(this_list[-1])
print(this_list[-2])
print(this_list[2:4])
print(this_list[:3])
print(this_list[2:])
print(this_list[-4:-1])
if "apple" in this_list: 
    print("Yes, 'apple' is in the fruits list")
if "mango" not in this_list:
    print("Yes, 'mango' is not in the fruits list")
this_list[1] = "mango"
print(this_list)
this_list[2:5] = ["gauva"]  # items replaced
print(this_list)
this_list.insert(2, "pear")
print(this_list)
this_list.append("orange")
print(this_list)
tropical = ["plum", "papaya"]
this_list.extend(tropical)
print(this_list)
this_list.pop()
print(this_list)
this_list.pop(2)
print(this_list)
new_list1 = this_list  # both list will use same memory
new_list2 = this_list[:]  # new_list2 will be a fresh copy
del this_list[0]
print(this_list)
print("new_list1: " + str(new_list1))
print("new_list2: " + str(new_list2))
new_list1.clear()
print(this_list)
print(new_list1)
print(new_list2)
pop_value = new_list2.pop(2)
print(pop_value)
print(new_list2)
print(new_list2.count('apple'))
new_list2.insert(1, "pear")
print(new_list2)
new_list2.reverse() # reverse the content
print(new_list2)
new_list2.sort()
print(new_list2)
new_list2.sort(reverse=True) # sort in descending
print(new_list2)