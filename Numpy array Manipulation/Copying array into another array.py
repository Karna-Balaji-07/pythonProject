print("Using np.copy() function")
import numpy as np
org_array = np.array([1.54, 2.99, 3.42, 4.87, 6.94,
                      8.21, 7.65, 10.50, 77.5])
print(f'The original array : {org_array}')

copy_array = np.copy(org_array)
print(f'The copy array : {copy_array}')

copy_array[0] = 3.12
print(f'The updated copy array : {copy_array}')


print("***************************************\n")
print("Copy given 2d array into another array using np.copy function")
org_array1 = np.array([[23, 46, 85],
                      [43, 56, 99],
                      [11, 34, 55]])
print(f'The original array : {org_array1}')
copy_array1 = np.array(org_array1)
print(f'The copy array : {copy_array1}')


print("******************************************\n")
print("Numpy copy array using assignment operator")
print("Similar to no copy : any changes made to copy array or original array will be reflected to both arrays")
org_array2 = np.array([[99, 22, 33],
                      [44, 77, 66]])
copy_array2 = org_array2
print(f'The original array : {org_array2}')
print(f'The copy array : {copy_array2}')
copy_array2[0][0] =111
org_array2[1][1] =22
print(f'The updated original array : {org_array2}')
print(f'The updated copy array : {copy_array2}')