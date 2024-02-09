print("Determinant of a Matrix")

import  numpy as np

arr1 = np.array([[2,6],[7,3]])
det = np.linalg.det(arr1)
print(f'The determinant of matrix {arr1} is \n{det}')

arr2 = np.array([[55, 25, 15],
                    [30, 44, 2],
                    [11, 45, 77]])
det2 = np.linalg.det(arr2)
print(f'The determinant of 3X3 matrix is \n{det2}')