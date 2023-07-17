#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 00:37:09 2023

@author: Janmesh
"""

import numpy as np
import pandas as pd

# Read the Excel file containing the matrices
data_frame = pd.read_excel('C:/Users/HP/Documents/Python/Research/Glucose/72HRS_Raw_data.xlsx', sheet_name='Raw', header=None)

#Variable Definitions
NumOfRows = 4
NumOfColumns = 3
MatrixNum = 0

# Create a dictionary to define the total number of matrices that we will end up with. In this case we will have 12.
d_array = {}
d_matrix = {}

#Goes through the number of rows in orginial matrix
for i in range (NumOfRows):
    #Goes through the number of rows in orginial matrix
    for j in range(NumOfColumns):
        #Count the number of values in the original 4x3 matrix
        MatrixNum += 1
        #Create new lists for the matrices generated, based on the number of values in the original matrix. Original matrix has 12 values (4x3), so 12 new lists will be made.
        #remember to adjust j if some wells are cut off
        d_array["array_data{0}".format(MatrixNum)] = data_frame.iloc[i + 24::9, j + 11].values[:9]

for key, array in d_array.items():
    print("Contents of", key, "array:")
    print(array)
    print()

# Reshape the data into a 3x3 matrix
for k in range (MatrixNum):

   d_matrix["matrix_data{0}".format(k)] = np.reshape(d_array["array_data" + str(k + 1)], (3, 3))



for z in range (MatrixNum):
    
    print (d_matrix["matrix_data" + str(z)])


#modify this portion to adjust how the data is printed into the excel file

#change based on the number of wells scanned
# Create a Pandas DataFrame for each matrix
#change this to match data shape
df0 = pd.DataFrame(d_matrix["matrix_data0"])
df1 = pd.DataFrame(d_matrix["matrix_data1"])
df2 = pd.DataFrame(d_matrix["matrix_data2"])
df3 = pd.DataFrame(d_matrix["matrix_data3"])
df4 = pd.DataFrame(d_matrix["matrix_data4"])
df5 = pd.DataFrame(d_matrix["matrix_data5"])
df6 = pd.DataFrame(d_matrix["matrix_data6"])
df7 = pd.DataFrame(d_matrix["matrix_data7"])
df8 = pd.DataFrame(d_matrix["matrix_data8"])
df9 = pd.DataFrame(d_matrix["matrix_data9"])
df10 = pd.DataFrame(d_matrix["matrix_data10"])
df11 = pd.DataFrame(d_matrix["matrix_data11"])
df12 = pd.DataFrame(d_matrix["matrix_data12"])
df13 = pd.DataFrame(d_matrix["matrix_data13"])
df14 = pd.DataFrame(d_matrix["matrix_data14"])
df15 = pd.DataFrame(d_matrix["matrix_data15"])
df16 = pd.DataFrame(d_matrix["matrix_data16"])
df17 = pd.DataFrame(d_matrix["matrix_data17"])
#df18 = pd.DataFrame(d_matrix["matrix_data18"])
#df19 = pd.DataFrame(d_matrix["matrix_data19"])


# Create an Excel writer object
excel_writer = pd.ExcelWriter('72hr_gluc.xlsx')

# Write each DataFrame in the Excel file
# df0.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False)
# df1.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startcol=4)
# df2.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startcol=8)
# df3.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startcol=12)

# df4.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=4)
# df5.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=4, startcol=4)
# df6.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=4, startcol=8)
# df7.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=4, startcol=12)

# df8.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=8)
# df9.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=8, startcol=4)
# df10.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=8, startcol=8)
# df11.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=8, startcol=12)

# df12.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=12)
# df13.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=12, startcol=4)
# df14.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=12, startcol=8)
# df15.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=12, startcol=12)

# df16.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=16)
# df17.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=16, startcol=4)
#df18.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=16, startcol=8)
#df19.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=16, startcol=12)

#change based on how we want the data displayed in the Excel file
# Write each DataFrame in the Excel file
df0.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False)
df1.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startcol=4)
df2.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startcol=8)

df3.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=4)
df4.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=4, startcol=4)
df5.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=4, startcol=8)


df6.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=8)
df7.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=8, startcol=4)
df8.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=8, startcol=8)


df9.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=12)
df10.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=12, startcol=4)
df11.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=12, startcol=8)


df12.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=16)
df13.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=16, startcol=4)
df14.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=16, startcol=8)


df15.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=20)
df16.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=20, startcol=4)
df17.to_excel(excel_writer, sheet_name='Matrix0', header=None, index=False, startrow=20, startcol=8)


# Save the Excel file
excel_writer.save()