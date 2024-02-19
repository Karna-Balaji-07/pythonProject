import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

np.random.seed(42)
X = np.random.randn(20,2)
y = np.where(X[:,0]+X[:,1] > 0,1,-1)
C_value = 1e6
clf = svm.SVC(kernel='linear',C=C_value)
clf.fit(X,y)
plt.scatter(X[:,0],X[:,1], c =y, cmap=plt.cm.Paired)

ax = plt.gca()
xlin = ax.get_xlim()
ylin = ax.get_ylim()

xx,yy = np.meshgrid(np.linspace(xlin[0], xlin[1], 50),
                    np.linspace(ylin[0],ylin[1],50))
Z = clf.decision_function(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)

ax.contour(xx,yy,Z,colors='k',levels=[-1,0,1],alpha=0.5,linestyles=['--','-','--'])

ax.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1],s=100,linewidth=1,facecolors='none',edgecolors='k')

plt.title("Maximum Margin Classifier with SVM")
plt.show()