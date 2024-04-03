import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df = pd.read_csv('https://raw.githubusercontent.com/rasbt/'
'python-machine-learning-book-3rd-edition'
'/master/ch10/housing.data.txt', header=None,sep='\s+')

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS','NOX', 'RM', 'AGE', 'DIS', 'RAD',
'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

print(df.head())

X = df[['LSTAT']].values
y = df['MEDV']

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
reg = LinearRegression()

# Creating Quadratic Features
quadratic = PolynomialFeatures(degree=2)
cubic = PolynomialFeatures(degree=3)

X_quad = quadratic.fit_transform(X)
X_cubic = cubic.fit_transform(X)


# Fit the features
X_fit = np.arange(X.min(), X.max(), 1)[:, np.newaxis]
reg = reg.fit(X,y)
y_lin_fit = reg.predict(X_fit)
linear_r2 = r2_score(y, reg.predict(X))


reg = reg.fit(X_quad, y)
y_quad_fit = reg.predict(quadratic.fit_transform(X_fit))
quadratic_r2 = r2_score(y, reg.predict(X_quad))


reg = reg.fit(X_cubic, y)
y_cubic_fit = reg.predict(cubic.fit_transform(X_fit))
cubic_r2 = r2_score(y, reg.predict(X_cubic))


plt.scatter(X,y, label = 'Training Points', color = 'black')
plt.plot (X_fit, y_lin_fit,
label='Linear (d=1), $R^2=%.2f$' % linear_r2,color='orange',lw=2,linestyle=':')


plt.plot (X_fit, y_quad_fit,label='Quadratic (d=2), $R^2=%.2f$' % quadratic_r2,color='red',lw=2,linestyle='-')
plt.plot (X_fit, y_cubic_fit,label='Cubic (d=3), $R^2=%.2f$' % cubic_r2,color='blue',lw=2,linestyle='--')


plt.xlabel ('% lower status of the population [LSTAT]')
plt.ylabel ('Price in $1000s [MEDV] ')
plt. legend (loc='upper right')
plt. show ()

