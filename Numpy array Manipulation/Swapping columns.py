print("Swapping columns in an array")

import numpy as np
arr = np.arange(12).reshape(3,4)
print(f'Original array : {arr}')
arr[:,[2,0]] = arr[:,[0,2]]
print("Array after swapping the first and last column : 0")
print(arr)

arr[:,[0,3]] = arr[:,[1,0]]
print("Array after swapping the first and last column : 0")
print(arr)
