import pandas as pd

#read csv to df
df_all = pd.read_csv('/Users/luchen/Documents/MSUA/2023Spring/Capstone/datasets/nsi_nystate.csv')
# print(df_all.head())
# num_rows, num_cols = df_all.shape
# print(f"The DataFrame has {num_rows} rows and {num_cols} columns.")

#cut west
df = df_all[df_all['x'] > -74.6949225]
# print(df.head())
# num_rows1, num_cols1 = df.shape
# print(f"The DataFrame has {num_rows1} rows and {num_cols1} columns.")

#cut up
df2 = df[df['y'] < 40.9275715]
print(df2.head())
num_rows, num_cols = df2.shape
print(f"The DataFrame has {num_rows} rows and {num_cols} columns.")

#csv
df2.to_csv('/Users/luchen/Documents/MSUA/2023Spring/Capstone/datasets/nyc_nsi_rough.csv', index=False)