import pandas as pd
from helper import *


#####################################
#### read cleaned csv data to df ####
#####################################

# read csv
nsi_all = pd.read_csv('/Users/luchen/Documents/MSUA/2023Spring/Capstone/datasets/nyc_nsi.csv')
print_df_info(nsi_all)

ll84_all = pd.read_csv('/Users/luchen/Documents/MSUA/2023Spring/Capstone/datasets/nyc_energy.csv')
print_df_info(ll84_all)

# # filter - office buildings
# df_office_primarytype_energy = df_energy[df_energy['Primary Property Type - Self Selected'] == 'Office']
# num_rows, num_cols = df_office_primarytype_energy.shape
# print(df_office_primarytype_energy.head())
# print(f"The DataFrame has {num_rows} rows and {num_cols} columns.")

# df_office_primarytype_energy.to_csv('/Users/luchen/Documents/MSUA/2023Spring/Capstone/datasets/nyc_energy.csv', index=False)




