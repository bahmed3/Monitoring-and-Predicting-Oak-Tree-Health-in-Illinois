import pandas as pd
import matplotlib.pyplot as plt

tree_cover_loss_df = pd.read_csv('../data/tree_cover_loss.csv', encoding='latin1')
monthly_avg_temp_df = pd.read_csv('../data/monthly_avg_temp.csv', encoding='latin1')
monthly_avg_precip_df = pd.read_csv('../data/monthly_avg_precip.csv', encoding='latin1')
soil_temp_data_df = pd.read_csv('../data/soil_temp_data.csv', encoding='latin1')
oak_stems_data_df = pd.read_csv('../data/oak_stems_data.csv', encoding='latin1')
oak_acreage_data_df = pd.read_csv('../data/oak_acreage_data.csv', encoding='latin1')

soil_temp_data_df.columns = soil_temp_data_df.columns.str.strip().str.replace('"', '')
soil_temp_data_df['Year'] = soil_temp_data_df['Year'].astype(int)

# Clean oak_stems_data_df
oak_stems_data_df.columns = oak_stems_data_df.columns.str.strip()
oak_stems_data_df = oak_stems_data_df.replace({'~': '', '\t': ''}, regex=True)
oak_stems_data_df['Oak (Stems per Acre)'] = pd.to_numeric(oak_stems_data_df['Oak (Stems per Acre)'], errors='coerce')
oak_stems_data_df['Native Non-oak (Stems per Acre)'] = pd.to_numeric(oak_stems_data_df['Native Non-oak (Stems per Acre)'], errors='coerce')
oak_stems_data_df['Non-native (Stems per Acre)'] = pd.to_numeric(oak_stems_data_df['Non-native (Stems per Acre)'], errors='coerce')

print("Oak Stems DataFrame:")
print(oak_stems_data_df.head())
print(oak_stems_data_df.dtypes)

# Plotting the data
tree_cover_loss_df.plot(kind='line', x='Year', y='Tree Cover Loss (ha)', figsize=(10, 6))
plt.title('Tree Cover Loss Over Years')
plt.ylabel('Tree Cover Loss (ha)')
plt.savefig('../outputs/tree_cover_loss_over_years.png')
plt.show()

monthly_avg_temp_df.plot(kind='line', x='Year', y='Annual Avg Temperature (°F)', figsize=(10, 6))
plt.title('Annual Average Temperature Over Years')
plt.ylabel('Annual Avg Temperature (°F)')
plt.savefig('../outputs/annual_avg_temp_over_years.png')
plt.show()

monthly_avg_precip_df.plot(kind='line', x='Year', y='Annual Precipitation (inches)', figsize=(10, 6))
plt.title('Annual Precipitation Over Years')
plt.ylabel('Annual Precipitation (inches)')
plt.savefig('../outputs/annual_precip_over_years.png')
plt.show()

soil_temp_data_df.plot(kind='line', x='Year', y=['2-Inch Bare Soil Temperature (°F)', '4-Inch Bare Soil Temperature (°F)', '8-Inch Under Sod Soil Temperature (°F)'], figsize=(10, 6))
plt.title('Soil Temperature Over Years')
plt.ylabel('Soil Temperature (°F)')
plt.savefig('../outputs/soil_temp_over_years.png')
plt.show()

oak_stems_data_df.plot(kind='bar', x='DBH Class (in)', figsize=(10, 6))
plt.title('Number of Stems per Hectare by Size Class')
plt.ylabel('Stems per Acre')
plt.savefig('../outputs/number_of_stems_per_hectare.png')
plt.show()

oak_acreage_data_df.plot(kind='bar', x='County', y=['1939', '2010'], figsize=(10, 6))
plt.title('Acreage of Oak Ecosystems by County (1939 vs 2010)')
plt.ylabel('Acreage')
plt.savefig('../outputs/acreage_of_oak_ecosystems_by_county.png')
plt.show()
