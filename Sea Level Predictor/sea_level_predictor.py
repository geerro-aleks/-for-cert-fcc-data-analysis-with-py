import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.scatter(x, y, color='brown', label='Data Points')

    # Create first line of best fit
    res = linregress(x, y)
    print(res)
    x_fit = pd.Series(range(1880, 2051))
    y_fit = res.intercept + res.slope * x_fit
    plt.plot(x_fit, y_fit, color='blue', label='Best Fit Line (1880-2050)')

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    res2 = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x_fit2 = pd.Series(range(2000, 2051))
    y_fit2 = res2.intercept + res2.slope * x_fit2
    plt.plot(x_fit2, y_fit2, color='green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()