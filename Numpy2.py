import asyncio

print("System of linear equations")

import numpy as np
# arr1 = np.array([[0,2],[1,4]])
# print(arr1)
# print(f'The shape of the matrix is {arr1.shape}\n')
#
# arr2 = np.array([[1,2,3],[4,5,6],[-1,-5,-3]])
# arr3 = np.array([[-1,2,-3],[9,2,6],[1,5,-3]])
# print(arr2,end="\n\n")
# print(arr3,end="\n\n")
# print(f'The shape of the matrix is {arr2.shape}\n')
# print(f'The shape of the matrix is {arr3.shape}\n')
# print(f'Addition : \n{arr2+arr3}')
# print(f'Subraction : \n{arr2-arr3}')
#
#
# print("Matrix-vector multiplication")
# arr4 = np.array([[1,4],[2,3]])
# print(f'Vector multiplication matrix-matrix multiplication: \n{arr4 @ arr1}')
# print(np.dot(arr1,arr4))  # Dot product
# print()
# print(np.vdot(arr4,arr1))


a1 = np.array([[1,2,1],[4,4,5],[6,7,7]])
a1_inverse = np.linalg.inv(a1)
print(a1_inverse,end="\n")
I = a1_inverse @ a1
print(np.round(I))

print("Matrix Transpose")
a2 = np.array([[1,2],[3,4],[5,6]])
print(a2.shape)
a2_transpose = a2.T
print(a2_transpose.shape)

print("\n Hadamard product : element wise product")
b1 = b2 = np.array([[0,2],[1,4]])
print(b1 * b2)
print(np.multiply(b1,b2))

print("Gaussian elimination method")
# addition and subraction of two equations,
# multiplication of an equation by a number
# swtiching equations

M = np.array([[1,3,5],[2,2,-1],[1,3,2]])
y = np.array([[-1],[1],[2]])
print(M)
solution = np.linalg.solve(M,y)
print(solution)

# a set of n linearly independent columns vectors with n elements forms a basis
