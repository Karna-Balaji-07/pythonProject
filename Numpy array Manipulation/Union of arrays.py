import numpy as np

a = np.array([1,2,34,54])
b = np.array([3,4,5,6])
print(np.union1d(a,b))

c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([0,5,10])
print(np.union1d(c,d))

