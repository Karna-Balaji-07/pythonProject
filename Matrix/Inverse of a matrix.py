print("Inverse of a matrix")

import numpy as np

arr1 = np.array([[7,4,7],[1,2,9],[0,5,0]])
invarr1 = np.linalg.inv(arr1)
print(f'The inverse of Matrix : \n{invarr1}')

arr2 = np.array([[1, 2, 3],
                [4, 9, 6],
                [7, 8, 9]])
invarr2 = np.linalg.inv(arr2)
print(f'The inverse of matrix : \n{invarr2}')

