print("Bitwise Operations in Numpy")

import numpy as np

#umpy.bitwise_and() : This function is used to Compute the bit-wise AND of two array element-wise. This function computes the bit-wise AND of the underlying binary representation of the integers in the input arrays
n1 = 10
n2 = 11
out1 = np.bitwise_and(n1,n2)
print(f'Bitwise add operator : \n{out1}')

in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]
out11 = np.bitwise_and(in_arr2,in_arr1)
print(f'Bitwise add : \n{out11}')


# numpy.bitwise_or() : This function is used to Compute the bit-wise OR of two array element-wise. This function computes the bit-wise OR of the underlying binary representation of the integers in the input arrays.
n1 = 10
n2 = 11
out2 = np.bitwise_or(n1,n1)
print(f'Bitwise OR operator : \n{out2}')

in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]
out_arr = np.bitwise_or(in_arr1, in_arr2)
print("Output array after bitwise_or: ", out_arr)

# numpy.bitwise_xor() : This function is used to Compute the bit-wise XOR of two array element-wise. This function computes the bit-wise XOR of the underlying binary representation of the integers in the input arrays.
in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]
out3 = np.bitwise_xor(in_arr1,in_arr2)
print(f'Bitwise XOR operator : \n{out3}')

# numpy.invert() : This function is used to Compute the bit-wise Inversion of an array element-wise. It computes the bit-wise NOT of the underlying binary representation of the integers in the input arrays. For signed integer inputs, the two’s complement is returned. In a two’s-complement system negative numbers are represented by the two’s complement of the absolute value.
in_arr1 = [2, 8, 125]
in_arr2 = [-3, -3, -115]
out4 = np.invert(in_arr1)
out44 = np.invert(in_arr2)
print(f'Inverse or NOT operator : \n{out44}')
print(f'Inverse or NOT operator : \n{out4}')

# numpy.left_shift() : This function is used to Shift the bits of an integer to the left.The bits are shifted to the left by appending arr2 0s(zeroes) at the right of arr1. Since the internal representation of numbers is in binary format, this operation is equivalent to multiplying arr1 by 2**arr2. For example, if the number is 5 and we want to 2 bit left shift then after left shift 2 bit the result will be 5*(2^2) = 20

n5 = 5
left_shift = 2
out5 = np.left_shift(n5,left_shift)
print(f'Left shift operator : \n{out5}')

# numpy.right_shift() : This function is used to Shift the bits of an integer to the right.Because the internal representation of numbers is in binary format, this operation is equivalent to dividing arr1 by 2**arr2. For example, if the number is 20 and we want to 2-bit right shift then after right shift 2-bit the result will be 20/(2^2) = 5.

n5 = 20
right_shift = 2
out5 = np.right_shift(n5,right_shift)
print(f'Right shift operator : \n{out5}')

# numpy.binary_repr(number, width=None) : This function is used to represent binary form of the input number as a string.For negative numbers, if width is not given, a minus sign is added to the front. If width is given, the two’s complement of the number is returned, with respect to that width.
# In a two’s-complement system, negative numbers are represented by the two’s complement of the absolute value.

n6 = 12
n66 = -24
out6 = np.binary_repr(n6)
out66 = np.binary_repr(n66)
out61 = np.binary_repr(n6,width=8)
out661 = np.binary_repr(n66,width=8)
print(f'The binary representation of {n6} is {out6}')
print(f'The binary representation of {n66} is {out66}')
print(f'The binary representation of {n6} is {out61}')
print(f'The binary representation of {n66} is {out661}')