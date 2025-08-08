import numpy as np

array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# iterating using for loop:
# for x in array:
#     for y in x:
#         for z in y:
#             print(z, end = " ")

# nditer()
for x in np.nditer(array):
    print(x, end=" ")
print('\n')
# ndenumerate()
for index , x in np.ndenumerate(array):
    print(index, x)