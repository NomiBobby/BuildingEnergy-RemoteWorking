import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def print_df_info(df):
    """
    Prints the shape of the DataFrame and its first few rows.
    """
    print("Data shape:", df.shape)
    print("Data head:")
    print(df.head())
    
        
def summary(df, col):
    """
    run a simple summary analysis
    """  
    # summarize the df
    df[col] = pd.to_numeric(df[col], errors='coerce')
    print("NaN: ", df[col].isna().sum())
    print(df[col].describe())
    
    
# def discri_analysis(df, col):
#     """
#     run a simple discptive analysis
#     """  
#     # NaN
#     print("NaN: ", df[col].isna().sum())
#     print(df[col].describe())
    
#     df2 = df.dropna(subset=[col])
#     df2['Borough'] = df2['Borough'].fillna('Not Specified')

#     plt.hist(df2[col], bins=50)
#     # add labels and title
#     plt.suptitle('Histogram of ' + col)
#     plt.xlabel(col)
#     plt.ylabel('Frequency')  
#     plt.show()

#     # Plot histograms for each borough with different colors
#     colors = ['red', 'green', 'blue', 'orange', 'purple', 'gray']
#     for i, borough in enumerate(df['Borough'].unique()):
#         plt.hist(df2[df2['Borough'] == borough][col], bins=50, color=colors[i], alpha=0.5, label=borough)
        
#     # Add labels and title
#     plt.title('Histogram of ' +col+' by Borough')
#     plt.xlabel(col)
#     plt.ylabel('Frequency')
#     plt.legend()
#     plt.show()
    

# def discri_analysis(df, col):
#     """
#     run a simple discptive analysis grouped by borough
#     and draw a histogram
#     """  
#     # overall descriptive analysis
#     print("NaN: ", df[col].isna().sum())
#     print(df[col].describe())
    
#     df2 = df.dropna(subset=[col])
#     df2['Borough'] = df2['Borough'].fillna('Not Specified')

#     plt.hist(df2[col], bins=50)
#     # add labels and title
#     plt.suptitle('Histogram of ' + col)
#     plt.xlabel(col)
#     plt.ylabel('Frequency')  
#     plt.show()

#     # Plot histograms for each borough with different colors
#     colors = ['red', 'green', 'blue', 'orange', 'purple', 'gray']
#     for i, borough in enumerate(df['Borough'].unique()):
#         plt.hist(df2[df2['Borough'] == borough][col], bins=50, color=colors[i], alpha=0.5, label=borough)
        
#     # Add labels and title
#     plt.title('Histogram of ' +col+' by Borough')
#     plt.xlabel(col)
#     plt.ylabel('Frequency')
#     plt.legend()
#     plt.show()
    
    
def filter_month(df, month):
    """
    filter out one month in montly ll84 data with column "Month"
    Example for 2020 Nov: Nov-20
    """  
    filter_df = df[(df['Month'] == month)]
    return filter_df
