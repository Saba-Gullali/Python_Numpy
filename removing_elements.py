import  numpy as np

# 1D array
arr_1d = np.array([1,2,3,4,5,6,7,8,9])
delete_no = np.delete(arr_1d,8,axis=0)
print(delete_no)

# 2D array
arr_2d = np.array([[1,2,3],[4,5,6]])
del_no = np.delete(arr_2d,0,axis=0)
print(del_no)
