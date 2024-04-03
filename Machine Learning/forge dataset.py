import mglearn
import matplotlib.pyplot as plt

x,y = mglearn.datasets.make_forge()
mglearn.discrete_scatter(x[:,0],x[:,1],y)
plt.legend(["class0","class1"],loc=4)
plt.xlabel("first feature")
plt.ylabel("Second feature")
print(f'X.shape : {x.shape}')
plt.show()

