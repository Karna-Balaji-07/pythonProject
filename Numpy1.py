import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(f'Array is of type : {type(arr)}')
print(f'Number of Dimensions : {arr.ndim}')
print(f'Shape of array : {arr.shape}')
print(f'Size of array : {arr.size}')
print(f'Type of elements stored in arrays : {arr.dtype}')


# Creating a numpy array
print("\nArray of Rank 1")
arr1 = np.array([1,2,3])
print(arr1)
print("\nArray of Rank 2")
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print("\nCreating an array from tuple")
arr3 = np.array((7,8,9))
print(arr3)



# Accessing the array index
arrs = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("\nInitial Array")
print(arrs)
print("Printing the range of array using slicing methods")
sliced_array = arrs[:2,2:]
print("Array with first 2 rows and alternate columns( 0 and 2) \n" )
print(sliced_array)

print("accessing elements from specified indices")
index = arrs[[1,1,0,3],[3,2,1,0]]
print("\nElements at the indices (1,3),(1,2),(0,1),(3,0) : ",index)


# Basic array Operations

# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])

# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
print("\nAdding 1 to every element",a+1)
print(a)
print("\nSubtracting 2 from every element in b ",b-2)
print(b)
print("\nSum of all elements in the array : ",a.sum())
print("\n Sum of two arrays : ",a+b)
