# Numpy
import numpy as np
arr = np.array([[1,2,3],[5,5,6]])
print(arr,end="\n")

#Scipy : Scientific Computing in Python
from scipy import sparse
eye = np.eye(4)
print(eye,end="\n")

import matplotlib.pyplot as plt
x = np.linspace(-10,10,100)
y = np.sin(x)
plt.plot(x,y,marker="x")
plt.title("Code1")
plt.show()



