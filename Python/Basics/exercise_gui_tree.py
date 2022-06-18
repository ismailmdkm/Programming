# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
for row in picture:
    for column in row:
        if column: # if picture[row][column] == 0: # didn't work since row is a list
            print("*", end="")
        else:
            print(" ", end="")
    print() # for new line after every row is printed

# print(type(row))
# print(type(column))
# Below is my first solution
# for x in range(len(picture)):
#     for y in range(7):
#         if picture[x][y] == 0:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()
# else:
#     print("All done")
