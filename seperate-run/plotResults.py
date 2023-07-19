import matplotlib.pyplot as plt
import pandas as pd

def plot_residual(vardata, residuals_normalized, title, xlabel):

    # Create a scatter plot of the normalized residuals
    ylabel = 'Normalized Residuals'
    plt.scatter(vardata, residuals_normalized, alpha=0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(y=0, color='r', linestyle='-') # This line indicates where residuals would be 0
    plt.title(title)
    plt.show()

    # Define the number of bins
    n_bins = 10

    # Create bins for '% Population with Bachelor Degree or Better'
    bins = pd.cut(vardata, bins=n_bins)

    # Compute bin centers
    bin_centers = (bins.cat.categories.right + bins.cat.categories.left) / 2

    # Group by the bins and calculate the mean and standard deviation of the normalized residuals
    mean_residuals = residuals_normalized.groupby(bins).mean()
    std_residuals = residuals_normalized.groupby(bins).std()

    # Create a DataFrame that stores the bin centers, mean residuals, and standard deviation of the residuals
    data = pd.DataFrame({
        'BinCenters': bin_centers,
        'MeanResiduals': mean_residuals,
        'StdResiduals': std_residuals
    }).dropna()

    # Plot the mean normalized residuals for each bin as points with error bars
    plt.errorbar(data['BinCenters'], data['MeanResiduals'], yerr=data['StdResiduals'], fmt='o', alpha=0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(y=0, color='r', linestyle='-') # This line indicates where residuals would be 0
    plt.title('Error Bar of ' + title)
    plt.show()