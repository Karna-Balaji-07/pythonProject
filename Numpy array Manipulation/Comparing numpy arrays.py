import numpy as np

print("== operator")
an_array = np.array([[1, 2], [3, 4]])
another_array = np.array([[1, 2], [3, 4]])

comparison = an_array == another_array
equal_arrays = comparison.all()

print(equal_arrays)


print("Relational operators")
a = np.array([101, 99, 87])
b = np.array([897, 97, 111])
print(np.greater(a,b))
print(np.less(a,b))
print(np.greater_equal(a,b))
print(np.less_equal(a,b))

print("\n\nUsing np.array_equal()")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])
x = np.array_equal(arr2,arr1)
if(x==True):
    print(True)
else:
    print(False)