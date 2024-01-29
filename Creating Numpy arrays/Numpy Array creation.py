#Array creation using lists

print("Array creation using lists")
arr = [1,2,3,4,5]
for i in range(len(arr)):
    print(arr[i],end=" ")
print("\n")


import numpy as np
l = [1,2,3,4,5,6]
ll = np.array(l)
print(ll)
print("Arrays using random modules")
r = np.random.rand(3,3)
print(r,end="\n\n")
r2 = np.random.randint(1,100,[3,3])
print(r2,end="\n\n")
print("Full array : fills the array with the given fill value")
r3 =np.full([4,4],10)
print(r3,end="\n\n")



arr17 = np.eye(2,dtype=int)
print(arr17,end="\n\n")
arr18 = np.eye(4,4,k=1,dtype=int)
print(arr18,end="\n\n")
arr19 = np.eye(4,4,k=-1,dtype=int)
print(arr19,end="\n\n")
arr20 = np.eye(4,4,k=0,dtype=int)
print(arr20,end="\n\n")

arr15 = np.ones(2,dtype=int)
arr16= np.ones([3,3],dtype=float)
print("ones method that returns an array filled with ones")
print(arr15,end="\n\n")
print(arr16,end="\n\n")



arr14 = np.array(([2,4],[5,6]))
print(arr14,end="\n\n")
print("Flatten by row wise")
print(arr14.flatten(),end="\n\n")
print("Flatten by column wise")
print(arr14.flatten('F'),end="\n\n")




arr12 = np.arange(8).reshape(2,4)
arr13 = np.arange(12).reshape(4,3)
print("Reshaping array")
print(arr12,end="\n\n")
print(arr13,end="\n\n")

print("Linespace method")
arr10 = np.linspace(1,10,2,retstep=True)
print(arr10,end="\n\n")
arr11 = np.linspace(1,20,5,retstep=True)
print(arr11,end="\n\n")


print("Array of sequence numbers")
arr7 = np.arange(2,11,2)
arr8 = np.arange(1,7)
arr9 = np.arange(1,20,3,dtype=float)
print(arr7,end="\n\n")
print(arr8,end="\n\n")
print(arr9,end="\n\n")


print("empty method that returns an array of random values")
arr1 = np.empty(2,dtype=int)
arr2 = np.empty([3,4],dtype=int)
arr3 = np.empty([3,3],dtype=float)
print(arr1,end="\n\n")
print(arr2,end="\n\n")
print(arr3,end="\n\n")

print("zeros method that returns an array of zeros as its values")
arr4 = np.zeros(2)
arr5 = np.zeros([3,4])
arr6 = np.zeros([4,4])
print(arr4,end="\n\n")
print(arr5,end="\n\n")
print(arr6,end="\n\n")
