import numpy as np
from sklearn.linear_model import RANSACRegressor
ransac = RANSACRegressor(LinearRegression(), max_trials=100, min_samples=50, loss = 'absolute_error', residual_threshold=5.0, random_state=0)
ransac.fit(X,y);

inlier_mask = ransac.inlier_mask
outlier_mask = np.logical_not (inlier_mask)
line_X = np.arange (3, 10, 1)
line_y_ransac = ransac.predict (line_X[:, np.newaxis])
plt.scatter (X[inlier_mask], y[inlier_mask],
C='steelblue', edgecolor='white',
marker='o', label='Inliers')
plt.scatter (X [outlier_mask], y[outlier_mask],
C='limegreen', edgecolor='white',
marker='s', label='Outliers')
plt.plot (line_X, line_y_ransac, color='black', lw=2)
plt.xlabel ('Average number of rooms [RM] ')
plt.ylabel ('Price in $1000s [MEDV]')
plt. legend (loc='upper left')
plt. show ()