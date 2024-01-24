import numpy as np

# np.empty...creates an array of given size with random values as its elements
print("np.empty()\n")
arr1 = np.empty(2,dtype=int)
print("Array 1 : \n",arr1)
arr2 = np.empty([2,2],dtype=int)
print("\n2 Dimension array : \n")
print(arr2)
arr3 = np.empty([3,3],dtype=int)
print("\n3-D array : \n")
print(arr3)


# np.zeros - creates an array of given size and type with zeros as its elements
a = np.zeros(2,dtype=int)
print("Array 1 : \n")
print(a)
b = np.zeros([2,2],dtype=int)
print("\n2-D 0 array : \n")
print(b)
c = np.zeros([3,3],dtype=float)
print("\n3-D 0 array : \n")
print(c)

import numpy as geek

array = geek.arange(8)
print("Original array : \n", array)

# shape array with 2 rows and 4 columns
array = geek.arange(8).reshape(2, 4)
print("\narray reshaped with 2 rows and 4 columns : \n", array)

# shape array with 2 rows and 4 columns
array = geek.arange(8).reshape(4, 2)
print("\narray reshaped with 2 rows and 4 columns : \n", array)

# Constructs 3D array
array = geek.arange(8).reshape(2, 2, 2)
print("\nOriginal array reshaped to 3D : \n", array)
