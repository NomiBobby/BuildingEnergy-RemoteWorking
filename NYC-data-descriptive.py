import pandas as pd
import numpy as np
from helper import *


#####################################
#### read cleaned csv data to df ####
#####################################

# read csv
# nsi_all = pd.read_csv('/Users/luchen/Documents/MSUA/2023Spring/Capstone/datasets/nyc_nsi.csv')
# print_df_info(nsi_all)

ll84_all = pd.read_csv('/Users/luchen/Documents/MSUA/2023Spring/Capstone/datasets/nyc_energy.csv')
ll84_all['NYC Borough, Block and Lot (BBL)'] = ll84_all['NYC Borough, Block and Lot (BBL)'].apply(lambda x: pd.to_numeric(x, errors='coerce') if x != 'Not Available' else np.nan)
# print_df_info(ll84_all)

pluto = pd.read_csv('/Users/luchen/Documents/MSUA/2023Spring/Capstone/datasets/PLUTO/Primary_Land_Use_Tax_Lot_Output__PLUTO_.csv')
# print_df_info(pluto)

# merge pluto and ll84 data on BBL
joined_df = pd.merge(ll84_all, pluto, how='left', left_on='NYC Borough, Block and Lot (BBL)', right_on='bbl')
joined_df = joined_df.drop(columns=['bbl'])
print_df_info(joined_df)

# merged_df = nsi_all.merge(ll84_all, left_on=['x', 'y'], right_on=['Longitude', 'Latitude'])
# print_df_info(merged_df)

office_ll84 = filter_df(ll84_all, 'Office', 'Largest Property Use Type', '2nd Largest Property Use Type', '3rd Largest Property Use Type')
print_df_info(office_ll84)
office_joined = filter_df(joined_df, 'Office', 'Largest Property Use Type', '2nd Largest Property Use Type', '3rd Largest Property Use Type')
print_df_info(office_joined)






