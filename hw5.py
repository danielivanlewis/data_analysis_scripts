"""
Daniel Ivan Lewis
SL: Jessie Sumerau
10/4/2018
ISTA 131 Hw5
Summary: This module pulls information from an arctic sea ice csv file and manipulates the data to clean
and format it using pandas. The module then uses the clean data and creates two new CSV files, one for an arctic sea
ice data frame with dates ranging from 1979 - 2017, and a csv file containing a series with arctic sea ice information
for 2018.
"""

import pandas as pd
import numpy as np
from datetime import timedelta
import datetime as dt

def get_data(csv = 'N_seaice_extent_daily_v3.0.csv'):
    """
    Purpose: This function reads in a csv file and returns a series with date objects
    as the index and the values extracted from the csv file as the data, representing arctic sea ice extent
    float values.
    Parameters: csv - 'N_seaice_extent_daily_v3.0.csv' as default.
    Returns: A Series with date objects as an index and data from the csv file passed in.
    """

    df = pd.read_csv(csv, skiprows=2, usecols=[0,1,2,3],
                     parse_dates={'Dates':[0,1,2]}, header=None, index_col=0)
    new_index = pd.date_range(df.index[0], df.index[-1]) # Creates list of date objects needed for index.
    df = df.reindex(new_index)
    return pd.Series(index=df.index, data=df.iloc[0:,0]) # Returns new Series from data collected above

def clean_data(frame):
    """
    Purpose: This function takes the Series created from the get_data function and cleans it up by
    replacing the NaN values with the average of the surrounding values. For longer portions of missing
    data, it uses the previous and following year to create averages and replace NaN values.
    Parameters: frame - the series created from the get_data function.
    Returns: None, modifies the frame passed in.
    """

    for i in range (1,len(frame),2):
        if np.isnan(frame.iloc[i]):
            frame.iat[i] = ((frame.iloc[i-1] + frame.iloc[i+1]) / 2) # uses average of previous and following values.
    for idx in frame.index:
        if np.isnan(frame.loc[idx]):
            one_before = idx - timedelta(days=365)
            one_after = idx + timedelta(days=366) # Since data is looking at a leap year, following year has 366 days
            frame.at[idx] = (frame.loc[one_after] + frame.loc[one_before]) / 2 #Uses previous and following year for averages

def get_column_labels():
    """
    Purpose: This function creates and returns list of mmdd formatted strings to use as the column labels
    for a data frame.
    Parameters: None.
    Returns: monthday - a list of mmdd formatted strings for each day in a regular year.
    """

    dates = pd.date_range(start=dt.datetime(1987, 1, 1), end=dt.datetime(1987, 12, 31)) # Non-leap year
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

def extract_df(frame):
    """
    Purpose: This function takes the clean Series created from the get_data and clean_data function. The function then
    creates a new data frame with values ranging from 1979 - 2017 with the column labels generated from the get_column_labels
    function and years as ints ranging from 1979 to 2017 as the index.
    Parameters: frame - the cleaned series created from the clean_data function.
    Returns: df - the data frame created.
    """

    monthday = get_column_labels() # gets list of mmdd formatted strings
    years = [1979+i for i in range (0,39)] # creates index labels
    df = pd.DataFrame(index=years, columns=monthday, dtype=np.float64)
    leaps = [1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016] # List of all leap years
    i = 67 # Skips first 67 rows of frame to skip 1978 values
    for row in range (0,len(df)):
        for col in range (0,len(df.iloc[row])):
            if df.index[row] in leaps and col == 59: # Checks to see if year is a leap year to skip feb 29th values
                i += 1
            df.iat[row,col] = frame.values[i]
            i += 1
    return df

def extract_2018(frame):
    """
    Purpose: This function extracts the portion from the cleaned series created that represents values from 2018 only.
    Parameters: frame - the series created from the clean_data function.
    Returns: A series with all the 2018 values from the frame passed in.
    """

    values = [] # Container for data for 2018 arctic ice extent
    index = [] # Container for date objects to be used as the index for the series
    for i in range (0,len(frame)):
        if frame.index[i].date().year == 2018:
            values.append(frame.iloc[i]) # Adds value to a list of data
            index.append(frame.index[i]) # Adds dateobject range to a list containing index labels
    return pd.Series(data=values,index=index,dtype=np.float64)

def main():
    """
    Purpose: The main function uses the previous functions to pull in the data, clean it, and create the new data frame
    of arctic sea ice extent information from 1979 to 2017 and the new series of 2018 values. The function then creates
    two new csv files with the corresponding data frame and series generated.
    Parameters: None.
    Returns: Creates two new csv files, 'data_79_17.csv' with data frame information and 'data_2018.csv' with series
    information.
    """

    frame = get_data() # Pulls data
    clean_data(frame) # Cleans the data
    df = extract_df(frame) # Creates the data frame
    frame_18 = extract_2018(frame) # Creates the 2018 info series
    df.to_csv('data_79_17.csv') # Creates new csv file for data frame
    frame_18.to_csv('data_2018.csv') # Creates new csv file for series info