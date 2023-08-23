import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.ndimage import uniform_filter

# Load the data from the CSV file
data = pd.read_excel('R:/Lab Share/Seth/Luminescence Tech/Spatial luminescence/4 metabolites/Processed Data/6.27.23-6.30.23 4 metabolites/6.30.23 4 metabolites 72hr/Lactate 72 hr/6.30.23-4metab-Lactate-72hr-Rep1-9pts.xlsx'
                     , sheet_name='Matrix0', header=None)
# rows_to_read = list(range(20,35))
# selected_rows = data.iloc[rows_to_read]

#print(data)

plt.figure()
sns.heatmap(data, cmap='inferno')
plt.title("Four metabolites: Lactate 72hr Raw")
plt.savefig('4metab_lactate_72hr_heat_raw1.jpg', format='jpeg')
plt.close()

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
z1 = uniform_filter(z, size=3)  # Adjust the size parameter for different levels of smoothing

z2 = uniform_filter(z1, size=3)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x_grid, y_grid, z2, cmap = 'inferno', antialiased=True)
ax.grid(False)

# Set labels and title
ax.view_init(elev=35, azim=45)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('Four metabolites: Lactate 72hr Raw')
plt.savefig('4metab_lactate_72hr_3d_raw1.jpg', format='jpeg')
# Display the plot

plt.show()



