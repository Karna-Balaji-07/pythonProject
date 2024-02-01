import numpy as np

print("Splitting numnpy arrays into equal parts using np.split()")
a = np.arange(6)
aa = np.split(a,3)
print(f'Original array : \n{a}')
print(f'splitted array : \n{aa}')

print("\n\nUnequal splitting of arrays using np.array_split()")
b = np.arange(13)
bb = np.array_split(b,4)
print(f'Original array : \n{b}')
print(f'splitted array : \n{bb}')

print("\n\nSplitting numpy 2D arrays")
c = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])
cc = np.split(c,3,1)
print(f'Original array : \n{c}')
print(f'splitted array : \n{cc}')
cc = np.array_split(c,4,1)
print(f'Original array : \n{c}')
print(f'splitted array : \n{cc}')

print("\n\nVertical splitting of arrays using vsplit()")
d = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9],
                            [10, 11, 12]])
dd = np.vsplit(d,2)
print(f'Original array : \n{d}')
print(f'splitted array : \n{dd}')

print("\n\nHorizontal splitting of arrays using hsplit()")
e = np.array([[1, 2, 3,0],
                            [4, 5, 6,0],
                            [0,7, 8, 9],
                            [10,0, 11, 12]])
ee = np.hsplit(e,2)
print(f'Original array : \n{e}')
print(f'splitted array : \n{ee}')