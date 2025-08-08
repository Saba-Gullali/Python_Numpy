import numpy as np

arr_1d = np.array([1,2,3,4,5,6,7])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# accesing the elements 6 from all the arrays
print(arr_1d[5])
print(arr_2d[1,2])
print(arr_3d[0,1,2])

# fancy indexing
indices = [1,2,3]
row = [0]
cols = [0,1,2]
print(arr_1d[indices])
print(arr_2d[row,cols])

# masking or filtering
print(arr_1d[arr_1d > 5])