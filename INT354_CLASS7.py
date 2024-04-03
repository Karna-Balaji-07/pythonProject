#Decision Treee Regressor
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/rasbt/'
 'python-machine-learning-book-3rd-edition'
 '/master/ch10/housing.data.txt',
 header=None,
 sep='\s+')

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS','NOX', 'RM', 'AGE', 'DIS', 'RAD',
'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

import matplotlib.pyplot as plt
X = df[['LSTAT']].values
y = df['MEDV'].values
tree = DecisionTreeRegressor(max_depth=3)

#Training the model
tree.fit(X,y)
sort_idx=X.flatten().argsort()
plt.scatter(X,y,color='lightgray')
plt.plot(X[sort_idx], tree.predict(X)[sort_idx],
         color='blue',
         lw=2,   #LineWidth
         linestyle='--')
plt.xlabel('% lower status of the population [LSTAT]')
plt.ylabel('Price [MEDV]')
plt.show()

#RandomForest Regressor .. define non-linearity assumptions
from sklearn.model_selection import train_test_split
X=df.iloc[:,:-1].values
y=df['MEDV'].values
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
forest = RandomForestRegressor(n_estimators=1000,
                               criterion='squared_error',
                               random_state=1,
                               n_jobs=-1)  #-1, means no limit for processor to do the prediction

#Training the model based on feature of x and y
forest.fit(X_train,y_train)
y_train_pred = forest.predict(X_train)
y_test_pred = forest.predict(X_test)
print('MSE Train : %.3f, Test : %.3f' % (mean_squared_error(y_train,y_train_pred),
                                         mean_squared_error(y_test,y_test_pred)))
print('R^2 Score Train: %.3f, Test : %.3f' % (r2_score(y_train,y_train_pred),
                                         r2_score(y_test,y_test_pred)))

#Plotting the graph based on prediction
plt.scatter(y_train_pred,y_train_pred-y_train,
            c='steelblue',edgecolors='black',
            marker='o',label='Training points')
plt.scatter(y_test_pred,y_test_pred-y_test,
            c='limegreen',edgecolors='blue',
            marker='s',
            alpha=0.9,
            label='Testing points')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals') #residuals  = vertical offset ---> |y-y^|
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=-10,xmax=50, lw=2, colors='red')
plt.xlim([-10,50]) #setting the limits for x axis
plt.show()

# from sklearn.metrics import * # for importing all metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn. metrics import mean_absolute_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import explained_variance_score

r2=r2_score(y_test, y_test_pred)
print("R2-Squared Error", r2)

# R2-Squared Error 0.6733825506400171

mse= mean_squared_error(y_test, y_test_pred)
print("Mean squared error", mse)

# Mean squared error 27.195965766883415

mae=mean_absolute_error(y_test, y_test_pred)
print("Mean absolute error of regression model", mae)

msle=mean_squared_log_error(y_test, y_test_pred)
print("Mean squared logarithmic error of regression model", msle)

mape=mean_absolute_percentage_error(y_test, y_test_pred)
print("mean absolute percentage error of regression model", mape)

exp_var=explained_variance_score(y_test, y_test_pred)
print("explained variance score of model", exp_var)