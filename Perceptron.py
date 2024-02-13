import numpy as np
import math
class Perceptron(object):
    def __init__(self,eta=0.01, n_iter=50, random_state = 1):
        self.eta = eta                                                  # Learning rate by default
        self.n_iter = n_iter                                            # Epochs
        self.random_state = random_state                                # Supports shuffling of training data

    def fit(self,X,y):                                                  # Gradient Descent to decrease the error
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size= 1 + X.shape[1])
        self.errors_ = []                                               # Stepwise determine he error value by gradient

        for _ in range(self.n_iter):
            errors = 0
        for xi, target in zip(X,y) :                                    ## Adjusting weights to reduce error
            update = self.eta * (target - self.predict(xi))
            self.w_[1:] += update * xi
            self.w_[0] += update
            errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self,X):
        return np.dot(X,self.w_[1:])+self.w_[0]

    def predict(self,X):
        return np.where(self.net_input(X) >= 0.0,1,-1)



from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, [2,3]]
y = iris.target
print('Class labels: ',np.unique(y))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1,stratify=y)

print('Labels counts in y: ',np.bincount(y))
print('Labels counts in y_train: ',np.bincount(y_train))
print('Labels counts in y_test: ',np.bincount(y_test))


from sklearn.preprocessing import StandardScaler
sc = StandardScaler() # Normalization means to make data in between 0 and 1
sc.fit(X_train)         # Training data fed for standardization
X_train_std = sc.transform(X_train) # Transforming the train data standardized
X_test_std = sc.transform(X_test)   # Transforming the test data standardized

from sklearn.linear_model import Perceptron
ppn = Perceptron(eta0=0.1 , random_state=1)
ppn.fit(X_train_std, y_train)

y_pred = ppn.predict(X_test_std)
print('Misclassified examples: %d' % (y_test != y_pred).sum())

