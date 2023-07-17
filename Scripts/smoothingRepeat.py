import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.ndimage import uniform_filter1d
from scipy.ndimage import uniform_filter

# Load the data from the CSV file
data = pd.read_csv('C:/Users/HP/Documents/Python/Research/Viability/viability_6_4_t72hr.csv')

# Extract the x, y, and z values from the data
y = list(range(1, len(data) + 1))
x = list(range(1, len(data.columns) + 1))
x = np.flip(x)
z = data.values

# Apply moving average smoothing in the x direction
smoothed_z = uniform_filter(z, size=3)  # Adjust the size parameter for different levels of smoothing

smoothed_z_2 = uniform_filter(smoothed_z, size=3)

smoothed_z_size5 = uniform_filter(z, size=5)

smoothed_z_size5_2 = uniform_filter(smoothed_z_size5, size=5)

# Create a meshgrid for the x and y values
x_grid, y_grid = np.meshgrid(x, y)

# Create a figure and subplot for the plots
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')  # Subplot 1 for the original surface plot
ax2 = fig.add_subplot(122, projection='3d')  # Subplot 2 for the smoothed surface plot
# ax3 = fig.add_subplot(223, projection='3d')
# ax4 = fig.add_subplot(224, projection='3d')
# Plot the original surface
ax1.plot_surface(x_grid, y_grid, smoothed_z, cmap='inferno', antialiased=True)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Glucose 1hr: Smoothed 3')

# Plot the smoothed surface
ax2.plot_surface(x_grid, y_grid, smoothed_z_2, cmap='inferno', antialiased=True)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Glucose 1hr: Smoothed Twice 3')

# ax3.plot_surface(x_grid, y_grid, smoothed_z_size5, cmap='inferno', antialiased=True)
# ax3.set_xlabel('X')
# ax3.set_ylabel('Y')
# ax3.set_zlabel('Z')
# ax3.set_title('Glucose 1hr: Smoothed 5')

# ax4.plot_surface(x_grid, y_grid, smoothed_z_size5_2, cmap='inferno', antialiased=True)
# ax4.set_xlabel('X')
# ax4.set_ylabel('Y')
# ax4.set_zlabel('Z')
# ax4.set_title('Glucose 1hr: Smoothed Twice 5')

# Adjust the layout to make room for both subplots
fig.tight_layout()

# Display the plot
plt.show()
