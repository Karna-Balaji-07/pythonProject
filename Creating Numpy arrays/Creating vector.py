import numpy as np

list1 = [1,2,3,4,5]
list2 = [[11],[22],[33]]
print("Horizontal array")
print(np.array(list1))
print("Vertical array")
print(np.array(list2))


print("Basic Arithmetic Operations : ")
list3 = [1,2,3,4,5]
list4 = [9,8,7,6,5]
a = np.array(list3)
b = np.array(list4)
print(f'Vector 1 : {a}')
print(f'Vector 2 : {b}\n')
print(f'Addition of two vectors : {a + b}')
print(f'Subraction of two vectors : {a - b}')
print(f'Multiplication of two vectors : {a * b}')
print(f'Divisiom of two vectors : {a / b}\n')

print("Vector Dot product")
d = a.dot(b)
print(f'Vector dot product of two vectors : {d}\n')

print("Vector Scalar multiplication")
scalar = 5
scal_mul = scalar * a
print(scal_mul,end="\n")
