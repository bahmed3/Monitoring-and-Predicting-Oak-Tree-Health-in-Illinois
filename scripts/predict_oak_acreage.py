import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load the data
oak_acreage_data_path = '../data/oak_acreage.csv'
oak_acreage_data_df = pd.read_csv(oak_acreage_data_path, encoding='latin1')

# Ensure proper column names
oak_acreage_data_df.columns = oak_acreage_data_df.columns.str.strip().str.replace('"', '')

# Convert the Year column to datetime
oak_acreage_data_df['Year'] = pd.to_datetime(oak_acreage_data_df['Year'], format='%Y')
oak_acreage_data_df.set_index('Year', inplace=True)

# Perform Exponential Smoothing
model_acreage = sm.tsa.ExponentialSmoothing(oak_acreage_data_df['Total Acreage'], trend='add', seasonal=None, seasonal_periods=None).fit()
forecast_acreage = model_acreage.forecast(steps=5)

# Plot the results
plt.figure(figsize=(10, 6))

# Acreage
plt.plot(oak_acreage_data_df.index, oak_acreage_data_df['Total Acreage'], label='Historical')
plt.plot(pd.date_range(start='2025', periods=5, freq='Y'), forecast_acreage, label='Forecast', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Total Acreage')
plt.legend()
plt.title('Forecasting Oak Acreage for Next 5 Years')

plt.savefig('../outputs/forecast_oak_acreage.png')
plt.show()
