print("numpy.hstack()")

import numpy as np
arr = np.array([1,2,3])
arr2 = np.array([4,5,6])
arra = np.hstack((arr,arr2))
print(f'hstack()  array : {arra}')

a = np.array([[1,2,3],[-1,-3,-5]])
b = np.array([[-1,-4,-8],[7,6,9]])
c = np.hstack((a,b))
print(f'hstack1() array : {c}')
print("*****************************\n")

print("vstack()")
x = np.array([1,2,3])
y = np.array([5,6,7])
z = np.vstack((x,y))
print(f'vstack1 array : {z}')
a = np.array([[1,2,3],[-1,-3,-5]])
b = np.array([[-1,-4,-8],[7,6,9]])
s = np.vstack((a,b))
print(f'vstack2 array : {s}')
