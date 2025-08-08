import numpy as np

# splitting 1 D array
# using array_split()
arr_1d = np.array([1,2,3,4,5,6])
split_array = np.array_split(arr_1d,5)
print(split_array)

# using split()
split= np.split(arr_1d,3)
print(split)

# vertical splitting:
arr_2d = np.array([[1,2,3],[4,5,6]])
vertical_split = np.vsplit(arr_2d,2)
print(f"vertical split: \n {vertical_split}")

# horizontal splitting:
horizontal_split = np.hsplit(arr_2d,3)
print(f"horizontal split: \n {horizontal_split}")