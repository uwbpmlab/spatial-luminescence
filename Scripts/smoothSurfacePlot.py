import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.ndimage import uniform_filter

# Load the data from the CSV file
data = pd.read_csv('C:/Users/HP/Documents/Python/Research/Lactate/6_3_Lactate_1_WELL_arranged_csv.csv')
# rows_to_read = list(range(20,35))
# selected_rows = data.iloc[rows_to_read]

#print(data)

#sns.heatmap(data, cmap='viridis')

# Extract the x, y, and z values from the data
y = list(range(1, len(data) + 1))
x = list(range(1, len(data.columns) + 1))
x = np.flip(x)
z = data.values
#print(x, y)

# Create a meshgrid for the x and y values
x_grid, y_grid = np.meshgrid(x, y)

#print(x_grid)
# Reshape the z values to match the shape of the meshgrid
#z_grid = z.reshape(x_grid.shape)

# Apply moving average smoothing
z1 = uniform_filter(z, size=5)  # Adjust the size parameter for different levels of smoothing

z2 = uniform_filter(z1, size=5)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x_grid, y_grid, z2, cmap = 'inferno', antialiased=True)


# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Lactate 1hr')

# Display the plot
plt.show()