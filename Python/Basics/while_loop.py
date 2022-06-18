'''
while loop
'''
i = 0
while i < 6:
    i += 1
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("loop finished")