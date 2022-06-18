'''
'is' vs '=='
'''
list1 = [1, 2]
list2 = list1.copy()
list3 = list1
if list1 == list1:  print("True")
else:               print("False")
if list1 is list1:  print("True")
else:               print("False")
if list1 == list2:  print("True")
else:               print("False")
if list1 is list2:  print("True")
else:               print("False")
if list1 is list3:  print("True")
else:               print("False")
list3 = list3 + list2
if list1 is list3:  print("True")
else:               print("False")