import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the vegetation cover area
def calculate_vegetation_area(image_path, threshold):
    with rasterio.open(image_path) as src:
        image = src.read(1)  
        vegetation_mask = image > threshold
        vegetation_area = np.sum(vegetation_mask)
        return vegetation_area, vegetation_mask

image_2005_path = '../data/p022r033_TC_2005.tif'
image_2010_path = '../data/p022r033_TC_2010.tif'

# Threshold value to identify vegetation
vegetation_threshold = 50

# Calculate vegetation area for each image
area_2005, mask_2005 = calculate_vegetation_area(image_2005_path, vegetation_threshold)
area_2010, mask_2010 = calculate_vegetation_area(image_2010_path, vegetation_threshold)

print(f"Vegetation area in 2005: {area_2005} pixels")
print(f"Vegetation area in 2010: {area_2010} pixels")
print(f"Change in vegetation area: {area_2010 - area_2005} pixels")

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(mask_2005, cmap='Greens')
ax[0].set_title('Vegetation Mask 2005')
ax[1].imshow(mask_2010, cmap='Greens')
ax[1].set_title('Vegetation Mask 2010')
plt.show()
