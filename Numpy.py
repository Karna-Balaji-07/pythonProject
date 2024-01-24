import numpy as np  # numerical python

x = np.array(([1],[2],[3]))
y = np.array(([6],[7],[8]))
print(x.shape)
print(y.shape)
print()

print(f'3-D vector {x}')
print()
print(f'3-D vector {y}')
print()

print("Addition")
print(x+y)
print()
a = np.add(y,x)
print(a)
print()

print("Scalar product")
alpha = 2;
s = alpha * y
print(s)
print()
d = np.multiply(alpha,x)
print(d)
print()


a,b = 2,3
x,y = np.array(([2],[3])),np.array(([9],[83]))
f = a*x + b*y
print(f)
print()

print("Dot product")
print(x.T@y)
print()

print("Vector Norms")
print("1. Eculidian Norms")
x = np.array(([3],[4]))
q = np.linalg.norm(x,2)
print(q)
print("2. Manhattan norm l1 norm")
x = np.array(([3],[-4]))
w = np.linalg.norm(x,1)
print(w)
print("3. Infinity norm")
x = np.array(([3],[-4]))
e = np.linalg.norm(x,np.inf)
print(e)

print("\nDistance between two vectors")
x,y = np.array(([0],[2])),np.array(([2],[0]))
distance = np.linalg.norm(x-y,2)
print(distance)

print("\nVector angles")
x,y = np.array(([2],[-3])),np.array(([2],[3]))
cos_thetta = (x.T@y) / ((np.linalg.norm(x,2)) * (np.linalg.norm(y,2)))
print(cos_thetta)
r = np.round(cos_thetta,3)
print(r)
cos_inverse = np.arccos(cos_thetta)
print(cos_inverse)
degree = cos_inverse * ((180)/np.pi)
print(degree)
print()
x,y = np.array(([2],[0])),np.array(([0],[2]))
cos_thetta = (x.T@y) / ((np.linalg.norm(x,2)) * (np.linalg.norm(y,2)))
print(cos_thetta)
r = np.round(cos_thetta,3)
print(r)
cos_inverse = np.arccos(cos_thetta)
print(cos_inverse)
degree = cos_inverse * ((180)/np.pi)
print(degree)