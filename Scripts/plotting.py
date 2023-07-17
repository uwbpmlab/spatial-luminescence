import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
from scipy.ndimage import uniform_filter
import seaborn as sns

# Load the data from the CSV file
data = pd.read_csv('C:/Users/HP/Documents/Python/Research/Lactate/6-4-23_Lactate-100pts-72hrs_CSV.csv')
# rows_to_read = list(range(20,35))
# selected_rows = data.iloc[rows_to_read]

#print(data)

# sns.heatmap(data, cmap='inferno')
# plt.title('Glucose 72hr Media')
# plt.show()

# Extract the x, y, and z values from the data
y = list(range(1, len(data) + 1))
x = list(range(1, len(data.columns) + 1))
x = np.flip(x)
z = data.values
smoothed_z = uniform_filter(z, size=5)  # Adjust the size parameter for different levels of smoothing

smoothed_z_2 = uniform_filter(smoothed_z, size=3)

# Create a meshgrid for the x and y values
x_grid, y_grid = np.meshgrid(x, y)

# Reshape the z values to match the shape of the meshgrid
#z_grid = z.reshape(x_grid.shape)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x_grid, y_grid, smoothed_z, cmap = 'inferno', antialiased=True)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Viability')

# Display the plot
plt.show()

