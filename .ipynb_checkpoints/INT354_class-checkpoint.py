# K4 cross validation with the pipelining function

from sklearn.datasets import load_iris;
dataset = load_iris()
x = dataset.data
y = dataset.target

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
x_val,x_test,y_val,y_test = train_test_split(x_test,y_test,test_size=0.5)
#
# Training data = 70% and testing data = 30%
# from the testing data,15% for validation anc 15% for testing


from sklearn.decomposition import PCA  # Dimensionality reduction technique
from sklearn.preprocessing import StandardScaler  # Normalization
from sklearn.linear_model import Perceptron    # 2-class classifier
from sklearn.pipeline import Pipeline    # for streaming all the phases in one module together

p = Pipeline([('sc',StandardScaler()),('pca1',PCA(n_components=2)),('p',Perceptron(penalty='l2'))])
p.fit(x_train,y_train)

#p = Pipeline(steps=[('sc',StandardScaler()),('pca1',PCA(n_components=2)), ('p',Perceptron(penalty='l2'))])
train_predict = p.predict(x_train)
val_pred1 = p.predict(x_val)
from sklearn.metrics import accuracy_score
print("Training Accuracy : ",accuracy_score(train_predict,y_train))
print("Validation Accuracy : ",accuracy_score(val_pred1,y_val))

p1 = Pipeline([('sc',StandardScaler()),('pca1',PCA(n_components=2)),('p',Perceptron(penalty='l2'))])
p1.fit(x_train,y_train)
