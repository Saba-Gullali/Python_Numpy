import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])
print(array.reshape(2,5 ))
"""
the reshape returns a view not a copy.
the view is just a b=view of original data while the copy is a new array.
the changes made to copy, doesn't reflect in the original array
the changes made to the view,  reflects in the original array
"""
# copy()
array_copy = array.copy()
array[0] = 42
print(array_copy)

# view()

array_view = array.view()
array[0] = 50
print(array_view)

# original array
print(array_copy.base)
print(array_view.base)

"""
ravel --> view
flatten --> copy
"""
arr_2d = np.array([[1,2,3,4],[5,6,7,8]])
print(arr_2d.ravel())
print(arr_2d.flatten())