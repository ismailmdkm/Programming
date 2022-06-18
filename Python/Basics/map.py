list1 = [1, 2, 3, 4]


def multiply_by_two(x):
    return x*2


# new_list = []
# for x in list1:
#     new_list.append(multiply_by_two(x))

# print(new_list)
# print(tuple(new_list))

print(list(map(multiply_by_two, list1)))
print(tuple(map(multiply_by_two, list1)))