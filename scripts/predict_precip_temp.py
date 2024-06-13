import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

precip_temp_data_path = '../data/precip_temp_data.csv'
precip_temp_data_df = pd.read_csv(precip_temp_data_path, encoding='latin1')

precip_temp_data_df.columns = precip_temp_data_df.columns.str.strip().str.replace('"', '')

precip_temp_data_df['Year'] = pd.to_datetime(precip_temp_data_df['Year'], format='%Y')
precip_temp_data_df.set_index('Year', inplace=True)

# Perform Exponential Smoothing
model_precip = sm.tsa.ExponentialSmoothing(precip_temp_data_df['Mean Annual Precipitation (mm)'], trend='add', seasonal=None, seasonal_periods=None).fit()
forecast_precip = model_precip.forecast(steps=5)

model_temp = sm.tsa.ExponentialSmoothing(precip_temp_data_df['Mean Annual Temperature (°C)'], trend='add', seasonal=None, seasonal_periods=None).fit()
forecast_temp = model_temp.forecast(steps=5)

plt.figure(figsize=(10, 6))

# Precipitation
plt.subplot(2, 1, 1)
plt.plot(precip_temp_data_df.index, precip_temp_data_df['Mean Annual Precipitation (mm)'], label='Historical Precipitation')
plt.plot(forecast_precip.index, forecast_precip, label='Forecasted Precipitation', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Mean Annual Precipitation (mm)')
plt.legend()

# Temperature
plt.subplot(2, 1, 2)
plt.plot(precip_temp_data_df.index, precip_temp_data_df['Mean Annual Temperature (°C)'], label='Historical Temperature')
plt.plot(forecast_temp.index, forecast_temp, label='Forecasted Temperature', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Mean Annual Temperature (°C)')
plt.legend()

plt.tight_layout()
plt.savefig('../outputs/precip_temp_forecast.png')
plt.show()
