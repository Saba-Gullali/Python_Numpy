"""
stacking: joining multiple arrays along a new axis
concatenate : joining arrays along axis
"""
import numpy as np

array1  = np.array([1,2,3,4,5])
array2 = np.array([6,7,8,9,10])

# 1Dimensional array:
# joining using concatenate()
new_array = np.concatenate((array1,array2))
print(new_array)

# joining using stack
new_array_stack = np.stack((array1,array2),axis=1)
print(new_array_stack)

# 2d array
array3 = np.array([[10,11,12,13],[14,15,16,17]])
array4 = np.array([[18,19,20,21],[22,23,24,25]])
new_array_stack2 = np.stack((array3,array4))
print(new_array_stack2)
# vertical stacking
print("vertical stacking: \n",np.vstack((array3,array4)))
# horizontal stacking
print("horizontal stacking: \n",np.hstack((array3,array4)))
# depth stacking
print("depth stacking: \n",np.dstack((array3,array4)))
