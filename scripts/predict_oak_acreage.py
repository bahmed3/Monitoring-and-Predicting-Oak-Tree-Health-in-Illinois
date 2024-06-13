import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

oak_acreage_data_df = pd.read_csv('../data/oak_acreage_data.csv', encoding='latin1')

oak_acreage_data_df = oak_acreage_data_df[['County', '1939', '2010']]

oak_acreage_data_df.set_index('County', inplace=True)
oak_acreage_data_df = oak_acreage_data_df.transpose()

oak_acreage_data_df['Total'] = oak_acreage_data_df.sum(axis=1)

# Interpolate the data for the years between 1939 and 2010
interpolated_years = pd.date_range(start='1939', end='2010', freq='Y')
interpolated_acreage = np.interp(np.arange(len(interpolated_years)), [0, len(interpolated_years)-1], oak_acreage_data_df['Total'].values)

# Create a DataFrame for the interpolated data
interpolated_df = pd.DataFrame(data={'Year': interpolated_years, 'Total': interpolated_acreage})
interpolated_df.set_index('Year', inplace=True)

# Create a simple linear regression model
X = np.array(interpolated_df.index.year).reshape(-1, 1)
y = interpolated_df['Total']
model = LinearRegression()
model.fit(X, y)

# Predict for the next 5 years
future_years = pd.date_range(start='2011', end='2015', freq='Y')
future_X = np.array(future_years.year).reshape(-1, 1)
future_predictions = model.predict(future_X)

plt.figure(figsize=(10, 6))
plt.plot(interpolated_df.index, interpolated_df['Total'], label='Historical')
plt.plot(future_years, future_predictions, label='Forecast', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Total Acreage')
plt.title('Forecasting Oak Acreage for Next 5 Years')
plt.legend()
plt.savefig('../outputs/forecast_oak_acreage.png')
plt.show()
