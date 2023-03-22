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