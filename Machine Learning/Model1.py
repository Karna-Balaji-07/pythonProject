import pandas as pd
import numpy as np

# Data PreProcessing

dataset = pd.read_csv("autompg.csv",sep='\s+', header=None, na_values='?')
print(dataset.shape)
print(dataset.isna().sum())

dataset = dataset.dropna()
print(dataset.shape)
print(dataset.head())

print()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dataset[8] = le.fit_transform(dataset[8])
print(dataset.head())
#
# import matplotlib.pyplot as plt
# # import seaborn as sns
# # sns.pairplot(dataset)
# # #plt.show()
#
# # corr = np.corrcoef(dataset.values.T)
# # hm = sns.heatmap(corr,annot=True)
# # #plt.show()

dataset = dataset.drop(columns=[6,8])
print(dataset.shape)

target = dataset[1]
features = dataset.drop(columns=[1])
print(features.head())

# Splitting the dataset into test train dataset
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(features, target, test_size=0.15, random_state=42)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
xtrain_std = sc.fit_transform(xtrain)
xtest_std = sc.transform(xtest)

print(pd.DataFrame(xtrain_std).describe())


print("\n Linear Regression \n")
# Choose a machine learning model based on the problem type (regression in this case)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(xtrain_std, ytrain)
# Evaluate model performance on the testing set
lr_train_result = lr.predict(xtrain_std)
lr_test_result = lr.predict(xtest_std)

from sklearn.linear_model import RANSACRegressor
ransac = RANSACRegressor(LinearRegression(), max_trials=100, min_samples=50, loss = 'absolute_error', residual_threshold=5.0, random_state=0)
ransac.fit(xtrain_std,ytrain    );



from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(ytrain, lr_train_result)
r2 = r2_score(ytrain, lr_train_result)
print("\nTraining Results: ")
print(f"Mean Squared Error: {mse*100}")
print(f"R-squared: {r2*100}")
#
# mse = mean_squared_error(ytest, lr_test_result)
# r2 = r2_score(ytest, lr_test_result)
# print("\nTesting Results: ")
# print(f"Mean Squared Error: {mse*100}")
# print(f"R-squared: {r2*100}")
#

#
# print()
# print("model creation")
# print()
# # Beyond Data Preprocessing - Model Training
#
# print("KNN Classifier")
# from sklearn.neighbors import KNeighborsClassifier
# training_Accuracy = []
# test_accuracy = []
# neighbors_settings = range(1,11)
# for n_neighbors in neighbors_settings:
#     clf = KNeighborsClassifier(n_neighbors=n_neighbors)
#     clf.fit(xtrain, ytrain)
#     training_Accuracy.append(clf.score(xtrain, ytrain))
#     test_accuracy.append(clf.score(xtest, ytest))
#
# for i in training_Accuracy:
#     print(i*100, end=" ")
# print()
# for j in test_accuracy:
#     print(j*100,end=" ")
#
# plt.plot(neighbors_settings, training_Accuracy, label="training accuracy")
# plt.plot(neighbors_settings, test_accuracy, label = "test accuracy")
# plt.ylabel("Accuracy")
# plt.xlabel("n_neighbors")
# plt.legend()
# plt.show()

# Perceptron model
# print("Perceptron")
# print()
#
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler() # Normalization means to make data in between 0 and 1
# sc.fit(xtrain)         # Training data fed for standardization
# X_train_std = sc.transform(xtrain) # Transforming the train data standardized
# X_test_std = sc.transform(xtest)   # Transforming the test data standardized
#
# from sklearn.linear_model import Perceptron
# ppn = Perceptron(eta0=0.1 , random_state=1)
# ppn.fit(X_train_std, ytrain)
#
# y_pred = ppn.predict(X_test_std)
# print('Misclassified examples: %d' % (ytest != y_pred).sum())
#
# from sklearn.metrics import accuracy_score
# print('Accuracy : %.3f' % accuracy_score(ytest,y_pred))
# print('Accuracy : %.3f' % ppn.score(X_test_std,ytest))
#
#
