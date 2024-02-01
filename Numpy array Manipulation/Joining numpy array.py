print("Joining numpy array : ")

import numpy as np


print("Using np.concatenate()")
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.concatenate((a,b),axis=0)
print(f'Concatenation along the axis 0 i.e x axis \n: {c}')
a = np.array([[1,2,3],[9,8,7]])
b = np.array([[4,5,6],[2,7,0]])
d = np.concatenate((a,b),axis=1)
print(f'Concatenation along the axis 1 :\n {d}')

a = np.array([[1,2,3],[9,8,7]])
b = np.array([[4,5,6],[2,7,0]])
d = np.concatenate((a,b),axis=0)
print(f'Concatenation along the axis 0 :\n {d}')

print("**********************\n")
print("Using np.stack())")
array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([5, 6, 7, 8])
new = np.stack((array_1,array_2),axis=1)
print(f'Stacked array : \n{new}')

array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([5, 6, 7, 8])
new = np.stack((array_1,array_2),axis=0)
print(f'Stacked array :\n {new}')


print("************************\n")
print("using np.block()")
block_1 = np.array([[1, 1], [1, 1]])
block_2 = np.array([[2, 2, 2], [2, 2, 2]])
block_3 = np.array([[3, 3], [3, 3], [3, 3]])
block_4 = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])

block_new = np.block([
    [block_1, block_2],
    [block_3, block_4]
])

print(block_new)