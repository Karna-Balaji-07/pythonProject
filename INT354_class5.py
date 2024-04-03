import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = np.array([ 258.0, 270.0, 294.0, 320.0, 342.0,
368.0, 396.0, 446.0, 480.0, 586.0]) [:, np.newaxis]

y = np.array([ 236.0, 234.0, 252.0, 298.0, 314.0,
342.0, 360.0, 391.2, 390.8, 312.0]) [:, np.newaxis]

lr = LinearRegression()     # For simple linear Regression
pr = LinearRegression()     # For polynomial regression

quadratic = PolynomialFeatures(degree=2)    # passing degree = 2
X_quad = quadratic.fit_transform(X)

# Training the linear regression model for comparison
lr.fit(X,y)
X_fit = np.arange(200, 600, 10)[:,np.newaxis]
y_lin_fit = lr.predict(X_fit)

# fit the multiple linear regression model considering the polynomial regression
pr.fit(X_quad,y)
y_quad_fit = pr.predict(quadratic.fit_transform(X_fit))


# Plot the results
plt.scatter(X, y, label='Training points')
plt.plot (X_fit, y_lin_fit, label='Linear fit', linestyle='--')
plt.plot (X_fit, y_quad_fit, label='Quadratic fit')
plt.xlabel ('Explanatory variable')
plt.ylabel ('Predicted or known target values')
plt. legend (loc='upper left')
plt.tight_layout ()
plt. show ()


from sklearn.metrics import mean_squared_error, r2_score
y_lin_pred = lr.predict (X)
y_quad_pred = pr.predict (X_quad)
print ('Training MSE linear: %.3f, quadratic: %.3f' % (mean_squared_error(y, y_lin_pred), mean_squared_error (y, y_quad_pred) ) )
# Training MSE linear: 569.780, quadratic: 61.330
print ('Training R^2 linear: %.3f, quadratic: %.3f' % (r2_score (y, y_lin_pred),r2_score (y, y_quad_pred) ) )
#Training R^2 linear: 0.832, quadratic: 0.982