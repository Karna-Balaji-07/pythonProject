print("No copy")
import numpy as np
arr = np.array([2,4,6,8,10])
nc = arr
print(f'ID of nc is {id(nc)}')
print(f'ID of arr is {id(arr)}')
print(f'the values of nc : {nc}')
print(f'the values of arr : {arr}')

print("\nUpdating the value of nc\n")
nc[2] = 43
nc[0] = 1
print(f'the values of nc : {nc}')
print(f'the values of arr : {arr}')

print("***********************************************\n")

print("view  / shallow copy")
arr1 = np.array([1,2,3,4,5,6,7,8])
v = arr1.view()
print(f'ID of v is {id(v)}')
print(f'ID of arr1 is {id(arr1)}')

print(f'the values of v : {v}')
print(f'the values of arr1 : {arr1}')
print("\nUpdating the value of v\n")
v[2] = 43
v[0] = 12
print(f'the values of v : {v}')
print(f'the values of arr1 : {arr1}')

print("***********************************************\n")


print("Copy  / Deep copy")
arr2 = np.array([11,12,13,14,15,16])
c = arr2.copy()
print(f'The id of arr2 : {id(arr2)}')
print(f'The ID of c : {id(c)}')
print(f'The values of arrr2 : {arr2}')
print(f'The values of c : {c}')
arr2[0] = 10
c[3] = 100
print(f'The values of arrr2 : {arr2}')
print(f'The values of c : {c}')