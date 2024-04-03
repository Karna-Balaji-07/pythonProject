import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/rasbt/'
                 'python-machine-learning-book-2nd-edition'
                 '/master/code/ch10/housing.data.txt',
                 sep='\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
              'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV']
sns.pairplot(df[cols], height=2.5)
plt.tight_layout()
plt.show()

import numpy as np
cm = np.corrcoef(df[cols].values.T)   # .T means matrix inclined towards row-wise
                                      # you can use (rowvvar = False/True)
                                      # difference between corr() and corrcoef()
                                      # corr() -- you will get the labelling of the matrix as 1,2,3...
                                      # corrcoef() -- no labelling of the matrix
sns.set(font_scale=1.5)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 15}, yticklabels=cols,
                 xticklabels=cols)
plt.show()


X = df[['RM']]      # Simple linear regression
Y = df[['MEDV']].values    # X - explanatory variable
                    # Y - response variable
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,Y)
print('Slope: %.3f'%lr.coef_[0])
print('Intercept: %.3f'%lr.intercept_)


def lin_regplot(X,Y,model):
    plt.scatter(X,Y,c='green',s=70)
    plt.plot(X,model.predict(X))
    return None
lin_regplot(X,Y,lr)
plt.xlabel("Average number of rooms (RM)")
plt.ylabel("Price in $ ('MEDV')")
plt.show()

# Multiple regression
from sklearn.model_selection import train_test_split
X = df.iloc[:,:-1].values #except the last attribute/col/explanatory variable
Y = df['MEDV'].values #only one col/ response variable



X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)
lr = LinearRegression()
lr.fit(X_train, Y_train)
Y_train_pred = lr.predict(X_train)
Y_test_pred = lr.predict(X_test)
from sklearn.metrics import mean_squared_error, r2_score
print('MSE train: %.3f, test: %.3f'%(mean_squared_error(Y_train,Y_train_pred), mean_squared_error(Y_test,Y_test_pred)))

print('R2_score Train: %.3f, Test: %.3f'%(r2_score(Y_train,Y_train_pred),r2_score(Y_test,Y_test_pred)))
from sklearn.metrics import accuracy_score
print('Accuracy : %.3f' % accuracy_score(Y_train,Y_train_pred))




import numpy as np
from sklearn.linear_model import RANSACRegressor
ransac = RANSACRegressor(LinearRegression(), max_trials=100, min_samples=50, loss = 'absolute_error', residual_threshold=5.0, random_state=0)
ransac.fit(X,Y);

inlier_mask = ransac.inlier_mask
outlier_mask = np.logical_not (inlier_mask)
line_X = np.arange (3, 10, 1)
line_y_ransac = ransac.predict (line_X[:, np.newaxis])
plt.scatter (X[inlier_mask], Y[inlier_mask],
C='steelblue', edgecolor='white',
marker='o', label='Inliers')
plt.scatter (X [outlier_mask], Y[outlier_mask],
C='limegreen', edgecolor='white',
marker='s', label='Outliers')
plt.plot (line_X, line_y_ransac, color='black', lw=2)
plt.xlabel ('Average number of rooms [RM] ')
plt.ylabel ('Price in $1000s [MEDV]')
plt. legend (loc='upper left')
plt. show ()

print('Slope: %.3f' % ransac.estimator_.coef_[0])
print('Intercept: %.3f' % ransac.estimator_.intercept_)