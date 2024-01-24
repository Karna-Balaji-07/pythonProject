import numpy as np

x = np.array(([1],[2],[3]))
y = np.array(([6],[7],[8]))
print(x.shape)
print(y.shape)
print()
print(f'3-D vector {x}')
print()
print(x+y)
print()
a = np.add(y,x)
print(a)