import pandas as pd

#####################################
#### print shape of df ####
#####################################

def print_df_info(df):
    """
    Prints the shape of the DataFrame and its first few rows.
    """
    print("Data shape:", df.shape)
    print("Data head:")
    print(df.head())
    
    
#####################################
#### filter office buildings? ####
#####################################

def filter_df(df, value, col1, col2=None, col3=None):
    """
    filter df based on a value in a column.
    """
    condition = (df[col1] == value) | (df[col2] == value) | (df[col3] == value)
    df_filter = df[condition]
    return df_filter
