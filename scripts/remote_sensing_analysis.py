import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

image_2014_path = '../data/p022r033_TC_2005.tif'
image_2024_path = '../data/p022r033_TC_2010.tif'

image_2014 = rasterio.open(image_2014_path)
image_2024 = rasterio.open(image_2024_path)

# Plot images
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

show(image_2014, ax=ax1, title='2005 Image')
show(image_2024, ax=ax2, title='2010 Image')

plt.tight_layout()
plt.savefig('../outputs/remote_sensing_comparison.png')
plt.show()
