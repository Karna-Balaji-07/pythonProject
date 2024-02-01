# Syntax: numpy.unique()
#
# Parameter:
#
# ar: array
# return_index: Bool, if True return the indices of the input array
# return_inverse: Bool, if True return the indices of the input array
# return_counts: Bool, if True return the number of times each unique item appeared in the input array
# axis: int or none, defines the axis to operate on

# import library
import numpy as np

# Create a 2D numpy array
arr2D = np.array([[11, 11, 12, 11],
                  [13, 11, 12, 11],
                  [16, 11, 12, 11],
                  [11, 11, 12, 11]])

uniqueRows = np.unique(arr2D)
print('Unique Rows:',uniqueRows, sep='\n')


arr2D = np.array([[11, 11, 12, 11],
                  [13, 11, 12, 11],
                  [16, 11, 12, 11],
                  [11, 11, 12, 11]])

uniqueRows = np.unique(arr2D, axis=0)
print('Unique Rows:',uniqueRows, sep='\n')


arr2D = np.array([[11, 11, 12, 11],
                  [13, 11, 12, 11],
                  [16, 11, 12, 11],
                  [11, 11, 12, 11]])

uniqueRows = np.unique(arr2D, axis=1)
print('Unique Rows:',uniqueRows, sep='\n')


arr2D = np.array([[11, 11, 12, 11],
                  [13, 11, 12, 11],
                  [16, 11, 12, 11],
                  [11, 11, 12, 11]])

uniqueRows = np.unique(arr2D, return_index=True)

print('Unique Rows:', uniqueRows, sep='\n')

