import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
#### simple discreptive analysis ####
#####################################    
def discri_analysis(df, col):
    """
    Prints simple discptive analysis results and histogram
    """  
    print(df[col].describe())
    plt.hist(df[col], bins=50)
    plt.show()
    print(df[col].isna().sum())
