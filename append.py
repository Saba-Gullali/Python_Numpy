import numpy as np

# appending 5 in 1D array
arr_1d = np.array([10,20,30,40,50,60])
new_1d = np.append(arr_1d,5)
print(f"original 1D array :\n {arr_1d}\n new 1D array: \n{new_1d}")

# appending 5 in 2D array
arr_2d = np.array([[10,20,30],[40,50,60]])
new_2d = np.append(arr_2d,5)
print(f"original 2D array :\n {arr_2d}\n new 2D array: \n{new_2d}")

# appending 5 in 3D array
arr_3d = np.array([[[10,20],[30,40],[50,60],[70,80]]])
new_3d = np.append(arr_3d,5)
print(f"original 3D array :\n {arr_3d}\n new 3D array: \n{new_3d}")




