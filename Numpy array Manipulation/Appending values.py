print("Appending a single value at the end of 1-D array")
import numpy as np
arr1 = np.array([1,2,3,4])
print(f'Original array : {arr1}')
arr11 = np.append(arr1,[5])
print(f'The updated array : {arr11}')

print("*******************************************\n")

print("Appending another array at the end of 1_D array")
arr2 = np.array([6,7,8,9])
print(f'Original array : {arr2}')
arr22 = np.append(arr11,arr2)
print(f'The updated array : {arr22}')

print("*********************************************\n")

print("Appending values at the end using concatenation")
arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[5,3]])
combined = np.concatenate((arr3,arr4),axis=0)
print(f'The combined array : {combined}')

print("*********************************************\n")

print("Appending with different array type")
arr5 = np.array([1,2,3])
arr6 = np.array([1.1,2.2,3.3])
arr_float = np.append(arr6,arr5)
print(f'The floating array : {arr_float}')

print("*********************************************\n")

print("Appending using list comprehension and np.concatenate() function")

arr = np.array([1, 2, 3, 4, 5])
values_to_append = [np.array([6, 7]), np.array([8, 9])]
combined = np.concatenate([arr] + values_to_append)
print(combined)

print("*********************************************\n")

print("Appending values to the end of N-Dimensinal array")
arr0 = np.arange(1,13).reshape(2,6)
print("Original array : ")
print(arr0)
arr01 = np.arange(5,11).reshape(1,6)
print("The array 2 : ")
print(arr01)

arr00 = np.append(arr0,arr01,axis=0)
print("Row wise appending : ")
print(arr00)
arr02 = np.array([5,6]).reshape(2,1)
arr03 = np.append(arr0,arr02,axis=1)
print("Column wise appending")
print(arr03)