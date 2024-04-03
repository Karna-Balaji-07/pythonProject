# ARIMA MODEL

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.stattools import adfuller

# Generating the sample data
np.random.seed(0)
dates = pd.date_range(start='2024-01-01', end = '2024-12-31')
data = np.random.randn(len(dates))
data = np.cumsum(data) # cumulativee sum to make random data
df = pd.DataFrame(data, index=dates, columns=['Value'])

#Split the data into train and test sets
train_size = int(len(df)*0.8)
train,test = df[:train_size], df[train_size:]

#Check stationary
def check_stationarity(timeseries):
    #Perfrom adfuller
    result = adfuller(timeseries)
    print('ADF Statistics:',result[0])
    print('p-value:',result[1])
    print('Critical value:')
    for key, value in result[4].items():
        print('\t%s: %.3f'% (key, value))

check_stationarity(train['Value'])
# If data is not stationary, then take first difference
train_diff = train.diff().dropna()
check_stationarity(train_diff['Value'])
# It is a linear regression model based on train and test dataset
X_train = np.arange(len(train)).reshape(-1,1)
y_train = train['Value']
regressor = LinearRegression()
regressor.fit(X_train,y_train)
trend = regressor.predict(X_train)

# Fit ARIMA model on residuals
model = ARIMA(train_diff, order = (5,1,0))  #ARIMA p = 4, d=1, q=0
fitted_model = model.fit()

#Predit using fitted ARIMA model
predictions_diff = fitted_model.forecast(steps=len(test))[0]
predictions_diff = pd.Series(predictions_diff, index=test.index)

# Add trend for obtaining the final predictions
predictions = predictions_diff + trend[-1]

# plotting the graph
plt.figure(figsize=(12,6))
plt.plot(train.index, train['Value'], label = 'Training Data')
plt.plot(test.index, test['Value'],label = 'Testing Data')
plt.plot(predictions.index, predictions, label = 'Predictions')
plt.title("ARIMA model with linear regression")
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

