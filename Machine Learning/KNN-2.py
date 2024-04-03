from sklearn.model_selection import train_test_split
import mglearn
import matplotlib.pyplot as plt

x,y = mglearn.datasets.make_forge()
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=0)    # splitting data into training and testing

# import and instantiate the class
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)

# fit the classifier using training set
clf.fit(x_train, y_train)

# to make predictions to dataset, we call the predict model
# For each data pointin the test set, this computes its nearest neighbors in the training set and finds themost common class among these
print(f'Model test set prediction : {clf.predict(x_test)}')

# To evaluate how well our model generalizes, we can call the score method with the
# test data together with the test labels
print(f'Test accuracy : {clf.score(x_test, y_test)*100}%')

