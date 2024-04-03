# using cancer dataset
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

x_train,x_test, y_train, y_test = train_test_split(cancer.data, cancer.target,stratify=cancer.target, random_state=0)

training_Accuracy = []
test_accuracy = []
neighbors_settings = range(1,11)
for n_neighbors in neighbors_settings:
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(x_train, y_train)
    training_Accuracy.append(clf.score(x_train, y_train))
    test_accuracy.append(clf.score(x_test, y_test))

for i in training_Accuracy:
    print(i*100, end=" ")
print()
for j in test_accuracy:
    print(j*100,end=" ")

plt.plot(neighbors_settings, training_Accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label = "test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.show()