
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Example: Loading data from a CSV file
df = pd.read_csv('your_time_series_data.csv', parse_dates=True, index_col='date_column_name')

# Plotting the time series
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['value_column_name'], label='Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Data')
plt.legend()
plt.show()


decomposition = sm.tsa.seasonal_decompose(df['value_column_name'], model='additive')
decomposition.plot()
plt.show()

from statsmodels.tsa.stattools import adfuller

result = adfuller(df['value_column_name'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])

# Example: Differencing to make the data stationary
df['stationary_data'] = df['value_column_name'].diff().dropna()

from statsmodels.tsa.statespace.sarimax import SARIMAX

# Example: Fit a SARIMA model
model = SARIMAX(df['value_column_name'], order=(p, d, q), seasonal_order=(P, D, Q, s))
results = model.fit()

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['value_column_name'], label='Observed Data')
plt.plot(forecast_mean.index, forecast_mean, label='Forecast')
plt.fill_between(forecast_mean.index, forecast.conf_int()['lower_value_column_name'], forecast.conf_int()['upper_value_column_name'], color='gray', alpha=0.3)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Forecast')
plt.legend()
plt.show()
