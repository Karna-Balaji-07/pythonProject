print("Operations on Matrix")

import numpy as np

# Add() - The function used to perform element wise  matrix addition
# sub() = the function performs element wise subraction
# divide() = the function used to perform element wise matrix division
# multiply() = performs element wise matrix multiplication
# dot() = compute the matrix multiplication rather than matrix wise multiplication
# sqrt() = computes the square root of each element in the matrix
# sum(x,axis) = adds all the elements in the matrix. column size if axis =0 and axis =1
# T = transpose of the specified matrix

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
add = np.add(arr2,arr1)
sub = np.subtract(arr2,arr1)
divide = np.divide(arr2,arr1)
multiply = np.multiply(arr1,arr2)
dot = np.dot(arr2,arr1)
root = np.sqrt(arr1)
sum = np.sum(arr1,axis=1)
summ = np.sum(arr2,axis=0)
print(f'Addition of two matrixes : \n{add}')
print(f'Subtraction of two matrixes : \n{sub}')
print(f'Division of two matrices : \n{divide}')
print(f'Multiplication of two matrices : \n{multiply}')
print(f'Dot product of two matrices : \n{dot}')
print(f'Root of all elements in the matrix : \n{root}')
print(f'Sum of the element in matrix : \n {sum} \n{summ}')
print(f'Transpose of a matrix : \n{arr1.T}')
