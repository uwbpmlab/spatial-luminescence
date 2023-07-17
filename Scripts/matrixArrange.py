import numpy as np
import pandas as pd

data = np.genfromtxt('C:/Users/HP/Documents/Python/Research/matrix_testing.csv')



# Print the matrix dimensions
num_rows, num_columns = data.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_columns)


for i in range(0, num_rows):
    for j in range(num_columns):
        element = data[i][j]
        print(i, j, element)