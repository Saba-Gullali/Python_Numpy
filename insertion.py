import numpy as np

# insertion in 1d array
arr_1d = np.array([1,2,3,4,5,6,7,8,9])
new_1d = np.insert(arr_1d,3,100,axis=0)
print(f"original 1D array: {arr_1d}")
print(f"new 1D array: {new_1d}")

# insertion in 2D array:
arr_2d = np.array([[1,2,3,4],[5,6,7,8]])
new_2d = np.insert(arr_2d,0, [9,10], 1)
print(f"original 2D array:\n  {arr_2d}")
print(f"new 2D array: \n {new_2d}")

# insertion in 3d array

arr_3d = np.array([[[1,2,3],[4,5,6],[7,8,9],[4,7,9]]])
new_3d =  np.insert(arr_3d,2,[4,5,6],axis=1)
print(f"original array: \n {arr_3d}")
print(f"new array :  \n {new_3d}")