import pandas as pd
import os

data_folder = "../data"
tree_cover_loss_path = os.path.join(data_folder, "tree_cover_loss.csv")
monthly_avg_temp_path = os.path.join(data_folder, "monthly_avg_temp.csv")
monthly_avg_precip_path = os.path.join(data_folder, "monthly_avg_precip.csv")
soil_temp_data_path = os.path.join(data_folder, "soil_temp_data.csv")
oak_stems_data_path = os.path.join(data_folder, "oak_stems_data.csv")
oak_acreage_data_path = os.path.join(data_folder, "oak_acreage_data.csv")

print(f"Tree Cover Loss Path: {tree_cover_loss_path}, Exists: {os.path.exists(tree_cover_loss_path)}")
print(f"Monthly Avg Temp Path: {monthly_avg_temp_path}, Exists: {os.path.exists(monthly_avg_temp_path)}")
print(f"Monthly Avg Precip Path: {monthly_avg_precip_path}, Exists: {os.path.exists(monthly_avg_precip_path)}")
print(f"Soil Temp Data Path: {soil_temp_data_path}, Exists: {os.path.exists(soil_temp_data_path)}")
print(f"Oak Stems Data Path: {oak_stems_data_path}, Exists: {os.path.exists(oak_stems_data_path)}")
print(f"Oak Acreage Data Path: {oak_acreage_data_path}, Exists: {os.path.exists(oak_acreage_data_path)}")

tree_cover_loss_df = pd.read_csv(tree_cover_loss_path, encoding='latin1')
monthly_avg_temp_df = pd.read_csv(monthly_avg_temp_path, encoding='latin1')
monthly_avg_precip_df = pd.read_csv(monthly_avg_precip_path, encoding='latin1')
soil_temp_data_df = pd.read_csv(soil_temp_data_path, encoding='latin1')
oak_stems_data_df = pd.read_csv(oak_stems_data_path, encoding='latin1')
oak_acreage_data_df = pd.read_csv(oak_acreage_data_path, encoding='latin1')

print(tree_cover_loss_df.head())
print(monthly_avg_temp_df.head())
print(monthly_avg_precip_df.head())
print(soil_temp_data_df.head())
print(oak_stems_data_df.head())
print(oak_acreage_data_df.head())
