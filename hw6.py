"""
Daniel Ivan Lewis
SL: Jessie Sumerau
10/11/2018
ISTA 131 Hw6
Summary: This module works with pandas and matplotlib. The module gathers information from an arctic sea ice csv
file and creates two different plots. One plot shows the daily mean of arctic sea ice between 1979 through 2017,
then compares it with the arctic sea ice extent of 2012 and 2018 as well as a shaded area showing +/- 2 standard
deviations from the mean. The second plot shows information about the daily averages of arctic sea ice per decades,
starting from the 1990s up to the 2010s, along with the 2018 data.
"""

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

def get_column_labels():
    """
    Purpose: This function creates and returns list of mmdd formatted strings to use as the column labels
    for a data frame.
    Parameters: None.
    Returns: monthday - a list of mmdd formatted strings for each day in a regular year.
    """
    dates = pd.date_range(start=dt.datetime(1987, 1, 1), end=dt.datetime(1987, 9, 16)) # Non-leap year
    monthday = []
    for d in dates:
        month = str(d.date().month)
        day = str(d.date().day)
        if len(month) < 2:
            month = '0' + month # Creates mm format
        if len(day) < 2:
            day = '0' + day # Creates dd format
        monthday.append(month + day)
    return monthday

def get_2018(csv = 'data_2018.csv'):
    """
    Purpose: This function reads in information from the 'data_2018.csv' file and returns a new Series with the
    information gathered from the file. The index is created by using the get_column_labels function.
    Parameters: csv - default csv file 'data_2018.csv'
    Returns: A cleaned up series with data for 2018 arctic sea ice levels.
    """
    monthday = get_column_labels() # uses function to create index
    df = pd.read_csv(csv, header=None, usecols=[1])
    raw_data = []
    for val in df.values:
        raw_data.append(val[0]) # Extracts the data and appends it to the raw_data list
    return pd.Series(index=monthday, data=raw_data)

def extract_fig_1_frame(df):
    """
    Purpose: This function reads in the data frame from hw5 and creates a new frame with the averages of all the values
    as well as values representing 2 standard deviations from the average of that day.
    Parameters: df - data frame created in hwk5
    Returns: The new data frame generated.
    """
    mean = [] # List to get values
    two_s = []
    columns = df.columns
    for column in columns:
        mean.append(df[column].mean()) # Generates mean for 'column' selected, (mmdd formatted date)
        two_s.append(df[column].std()*2) # Generates 2 * std dev on the average of that day
    return pd.DataFrame(data=[mean,two_s], columns=columns, index=['mean','two_s'])

def extract_fig_2_frame(df):
    """
    Purpose: This function reads in the dataframe from hw5 and creates a new data frame showing the decadal averages
    for arctic sea ice levels starting from the 1990s up to 2010's as well as stand alone values for 2018.
    Parameters: df - data frame created in hwk5
    Returns: The plot generated.The new data frame created.
    """
    mean = []
    for i in range(1, len(df.index), 10):
        temp = []
        for j in range(0, len(df.iloc[i])):
            temp.append(df.iloc[i:i + 10, j].mean())
        mean.append(temp)
    return pd.DataFrame(data=mean, columns=df.columns, index=['1980s','1990s','2000s','2010s'])

def make_fig_1(fig1, hw5):
    """
    Purpose: This function reads in the dataframe from hw5 and creates a plot using matplotlib with data of the daily
    mean of arctic sea ice between 1979 through 2017, arctic sea ice levels of 2012 and 2018, as well as a shaded area
    showing +/- 2 standard from the averages from 1979 to 2017 mean values.
    Parameters: hw5 - data frame created in hwk5
    fig1 - The series created in extract fig1 frame.
    Returns: The plot generated.
    """
    data_2018 = get_2018()
    plt.ylabel('NH Sea Ice Extent $(10^6km^2)$', fontsize=20)
    plt.xticks([0, 50, 100, 150, 200, 250, 300, 350])
    plt.plot(fig1.iloc[0], label='mean')
    plt.plot(hw5.loc[2012], linestyle='--', label='2012')
    plt.plot(data_2018, label='2018')
    two_sdbefore = (fig1.iloc[0] - fig1.iloc[1])
    two_sdafter = (fig1.iloc[0] + fig1.iloc[1])
    plt.fill_between(x=[i for i in range(0, 365)], y1=two_sdbefore, y2=two_sdafter, color='lightgray',
                     label='$\pm$ 2 std devs')
    plt.legend(loc='upper right')

def make_fig_2(fig2):
    """
    Purpose: This function reads in the dataframe from hw5 and creates a plot using matplotlib with data of the daily
    mean of arctic sea ice seperated by decades as well as the information that has been gathered up to current time in
    2018.
    Parameters: fig2 - data frame created in hwk5
    Returns: The plot generated.
    """
    data_2018 = get_2018()
    plt.ylabel('NH Sea Ice Extent $(10^6km^2)$', fontsize=20)
    plt.xticks([0, 50, 100, 150, 200, 250, 300, 350])
    plt.plot(fig2.loc['1980s'], label='1980s', linestyle='--')
    plt.plot(fig2.loc['1990s'], label='1990s', linestyle='--')
    plt.plot(fig2.loc['2000s'], label='2000s', linestyle='--')
    plt.plot(fig2.loc['2010s'], label='2010s', linestyle='--')
    plt.plot(data_2018, label='2018')
    plt.legend(loc='lower left')

def main():
    """
    Purpose: This function reads in the data from hw5 and uses the extract_fig functions to create new data frames, one
    showing all average data and one with decadal average information. The function then uses that data and the make fig
    functions to plot and display the data.
    Parameters: None
    Returns: None, shows the plots generated.
    """
    hw5 = pd.read_csv('data_79_17.csv', index_col=[0])
    fig1 = extract_fig_1_frame(hw5)
    fig2 = extract_fig_2_frame(hw5)
    make_fig_1(fig1,hw5)
    plt.figure()
    make_fig_2(fig2)
    plt.show()

main()
