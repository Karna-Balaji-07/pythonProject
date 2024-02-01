print("Insert a new axisw within a numpy array")
import numpy as np

print("\nUsing Numpy array : ")
arr = np.arange(25).reshape(5,5)
print(arr.shape)
arr_5D = arr[np.newaxis, ..., np.newaxis,np.newaxis]
print(arr_5D)

print("\n Using expand_dims")
x = np.zeros((3, 4))
y = np.expand_dims(x, axis=1).shape
print(y)

arr = np.arange(5 * 5).reshape(5, 5)
print(arr.shape)

print("\n Simulataneous insert many axes in the array")
newaxes = (0, 3, -1)
arr_5D = np.expand_dims(arr, axis=newaxes)
print(arr_5D.shape)

print("\nUsing reshape() for a single axis")
import numpy as np
arr = np.arange(6)
arr_reshape = arr.reshape((2, 3))
print(arr_reshape.shape)
