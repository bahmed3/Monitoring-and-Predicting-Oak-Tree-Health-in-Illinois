import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

tree_cover_loss_df = pd.read_csv('../data/tree_cover_loss.csv', encoding='latin1')
monthly_avg_temp_df = pd.read_csv('../data/monthly_avg_temp.csv', encoding='latin1')
monthly_avg_precip_df = pd.read_csv('../data/monthly_avg_precip.csv', encoding='latin1')
soil_temp_data_df = pd.read_csv('../data/soil_temp_data.csv', encoding='latin1')
oak_stems_data_df = pd.read_csv('../data/oak_stems_data.csv', encoding='latin1')
oak_acreage_data_df = pd.read_csv('../data/oak_acreage_data.csv', encoding='latin1')

soil_temp_data_df.columns = soil_temp_data_df.columns.str.strip().str.replace('"', '')

merged_df = pd.merge(tree_cover_loss_df, monthly_avg_temp_df, on='Year', how='inner')
merged_df = pd.merge(merged_df, monthly_avg_precip_df, on='Year', how='inner')
merged_df = pd.merge(merged_df, soil_temp_data_df, on='Year', how='inner')

correlation_matrix = merged_df.corr()

# Plot correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('../outputs/correlation_heatmap.png')
plt.show()

correlation_matrix.to_csv('../outputs/correlation_matrix.csv')

X = merged_df[['Annual Avg Temperature (°F)', 'Annual Precipitation (inches)']]
y = merged_df['Tree Cover Loss (ha)']

X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

print(model.summary())

with open('../outputs/regression_summary.txt', 'w') as f:
    f.write(model.summary().as_text())

# Scatter plot with trend line for temperature vs tree cover loss
plt.figure(figsize=(10, 6))
sns.regplot(x='Annual Avg Temperature (°F)', y='Tree Cover Loss (ha)', data=merged_df, ci=None, scatter_kws={'color':'blue'}, line_kws={'color':'red'})
plt.xlabel('Annual Avg Temperature (°F)')
plt.ylabel('Tree Cover Loss (ha)')
plt.title('Regression Analysis: Tree Cover Loss vs. Annual Avg Temperature')
plt.savefig('../outputs/regression_temp_vs_loss.png')
plt.show()

# Scatter plot with trend line for precipitation vs tree cover loss
plt.figure(figsize=(10, 6))
sns.regplot(x='Annual Precipitation (inches)', y='Tree Cover Loss (ha)', data=merged_df, ci=None, scatter_kws={'color':'blue'}, line_kws={'color':'red'})
plt.xlabel('Annual Precipitation (inches)')
plt.ylabel('Tree Cover Loss (ha)')
plt.title('Regression Analysis: Tree Cover Loss vs. Annual Precipitation')
plt.savefig('../outputs/regression_precip_vs_loss.png')
plt.show()
