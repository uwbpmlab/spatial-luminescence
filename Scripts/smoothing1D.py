import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.ndimage import uniform_filter1d
from scipy.ndimage import uniform_filter

# Load the data from the CSV file
data = pd.read_csv('C:/Users/HP/Documents/Python/Research/Glucose/NewGlucoseData/0hr_gluc_6_4_redone.csv')

# Extract the x, y, and z values from the data
y = list(range(1, len(data) + 1))
x = list(range(1, len(data.columns) + 1))
x = np.flip(x)
z = data.values

# Apply moving average smoothing in the x direction
smoothed_z = uniform_filter(z, size=5)  # Adjust the size parameter for different levels of smoothing

smoothed_x_z = uniform_filter1d(z, size=5, axis=1)
# Create a meshgrid for the x and y values
x_grid, y_grid = np.meshgrid(x, y)

# Create a figure and subplot for the plots
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')  # Subplot 1 for the original surface plot
ax2 = fig.add_subplot(122, projection='3d')  # Subplot 2 for the smoothed surface plot

# Plot the original surface
ax1.plot_surface(x_grid, y_grid, smoothed_z, cmap='inferno', antialiased=True)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Smoothed')

# Plot the smoothed surface
ax2.plot_surface(x_grid, y_grid, smoothed_x_z, cmap='inferno', antialiased=True)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Smoothed x')

# Adjust the layout to make room for both subplots
plt.tight_layout()

# Display the plot
plt.show()
