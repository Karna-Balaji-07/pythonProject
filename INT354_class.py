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
print("\n",p,"\n")
#p = Pipeline(steps=[('sc',StandardScaler()),('pca1',PCA(n_components=2)), ('p',Perceptron(penalty='l2'))])
train_predict = p.predict(x_train)
val_pred1 = p.predict(x_val)
from sklearn.metrics import accuracy_score
print("Training Accuracy of train_preict: ",accuracy_score(train_predict,y_train)*100)
print("Validation Accuracy of val_pred1: ",accuracy_score(val_pred1,y_val)*100)

p1 = Pipeline([('sc',StandardScaler()),('pca1',PCA(n_components=3)),('p',Perceptron(penalty='l2'))])
p1.fit(x_train,y_train)
train_predict2 = p1.predict(x_train)
val_pred2 = p1.predict(x_val)
print()
print("Training Accuracy of train_predict2: ",accuracy_score(train_predict2,y_train)*100)
print("Validation Accuracy of val_pred2: ",accuracy_score(val_pred2,y_val)*100)
print()
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
p3 = Pipeline([('sc',StandardScaler()),('lda',LDA(n_components=2)),('p',Perceptron(penalty='l2'))])
p3.fit(x_train,y_train)

train_pred4 = p3.predict(x_train)
val_pred4 = p3.predict(x_val)
print()
print("Training Accuracy of train_pred4: ",accuracy_score(train_pred4,y_train))
print("Validation Accuracy of val_pred4: ",accuracy_score(val_pred4,y_val))
print()
p4 = Pipeline([('sc',StandardScaler()),('lda',LDA(n_components=2)),('p',Perceptron(penalty='l2'))])
p4.fit(x_train,y_train)


train_pred5 = p4.predict(x_train)
val_pred5 = p4.predict(x_val)
print()
print("Training Accuracy of train_pred5: ",accuracy_score(train_pred5,y_train))
print("Validation Accuracy of val_pred5: ",accuracy_score(val_pred5,y_val))
print()

# First method of Kfold

from sklearn.model_selection import KFold
k = 5
kf = KFold(n_splits=k,shuffle=True)
acc_score = []
for train_index, test_index in kf.split(x):
    x_train = []
    x_test = []
    y_train = []
    y_test = []
    for i in train_index:
        x_train.append(x[i])
        y_train.append(y[i])
    for i in test_index:
        x_test.append(x[i])
        y_test.append(y[i])
    p.fit(x_train,y_train)
    test_pred = p.predict(x_test)
    acc_score.append(accuracy_score(test_pred,y_test))
print(acc_score)
print()

# Second method of Kfold

from sklearn.model_selection import cross_val_score
k = 5
kf= KFold(n_splits=5,shuffle=True)
result = cross_val_score(p,x,y,cv=kf)
print(result)
print()
import numpy as np
print("Average Accuracy : ",np.average(acc_score)*100,end="\n\n")
