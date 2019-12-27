"""
Daniel Ivan Lewis
SL: Jessie Sumerau
09/27/2018
ISTA 131 Hw4
Summary: This module includes various functions working with pandas dataFrame structures and SQL subqueries. The main
function works with a dataframe created from a countries csv file and prints out the five countries with the lowest
amount of time left before estimated extinction.
"""
import pandas as pd
import numpy as np
import sqlite3

def csv_to_dataframe(csv):
    """
    Purpose: This function opens a csv file with pandas.read_csv function and swaps out
    european style "," decimal character for traditional American decimal character.
    Parameters: csv - the name of a csv file.
    Returns: A DataFrame object from the csv file passed in.
    """

    return pd.read_csv(csv, header=0, index_col=0, decimal=',')

def format_df(df):
    """
    Purpose: This function uses the same dataframe created from the CSV file passed in previously,
    it strips off the extra whitespace from the values in the region column and the index.
    Parameters: df - A dataframe object created in the previous function.
    Returns: None - Only updates the dataframe.
    """

    new_idx = []
    for idx in df.index:
        clean = df.loc[idx, 'Region'].strip() # Strips the region values
        clean = clean.title() # Sets titlecase for the values in region column
        df.at[idx, 'Region'] = clean
        new_idx.append(idx.strip())
    df.index = new_idx # Replaces index with new "clean" index.

def growth_rate(df):
    """
    Purpose: This function adds a growth rate column to the dataframe previously used.
    Parameters: df - A dataframe object.
    Returns: None - The function does not return anything, only updates dataframe passed in.
    """

    cols = df.columns
    for i in range(0, len(cols)):
        if cols[i] == 'Birthrate': # Gathers the index for the birthrate column
            br_index = i
        if cols[i] == 'Deathrate': # Gathers index for the deathrate column
            dr_index = i
    df.loc[:,'Growth Rate'] = df.iloc[:,br_index] - df.iloc[:,dr_index]

def dod(p, r):
    """
    Purpose: This function takes a population and a negative growth rate in order to calculate
    the estimated number of years that population has until it is extinct.
    Parameters: p - an integer representing population
    r - A negative growth rate produced in the Growth Rate column from the previous function.
    Returns: num_yrs - The estimated amount of time in years that a population has until extinction.
    """
    num_yrs = 0
    while p > 2:
        p = p + p * r / 1000
        num_yrs += 1
    return num_yrs
    # Growth rate must be negative since people are dying every day and the population is decreasing.

def years_to_extinction(df):
    """
    Purpose: This function creates a new column for the existing dataframe. The column is called years to
    extinction and shows the amount of time that populations have until they are estimated to go extinct.
    Parameters: df - A dataframe object.
    Returns: None - Creates a new column called years to extinction within the dataframe passed in.
    """

    df.loc[:,'Years to Extinction'] = np.nan
    for row in df.index:
        growth_rate = df.loc[row,'Growth Rate']
        pop = df.loc[row, 'Population']
        if growth_rate < 0:
            df.at[row,'Years to Extinction'] = dod(pop ,growth_rate)

def dying_countries(df):
    """
    Purpose: This function returns a sorted series from the dataframe with all Nan values dropped.
    Parameters: df - A dataframe object.
    Returns: A cleaned up series of the countries that are expected to have a negative growth rate value.
    """

    return df.loc[:,'Years to Extinction'].dropna().sort_values(axis=0)

def class_performance(conn, tbl_name = 'ISTA_131_F17'):
    """
    Purpose: This function returns a dictionary of the percentages of grades that are achieved throughout a course.
    The function returns a dictionary with a capitalized letter grade as the key and the percentage of students who
    received said grade as a value.
    Parameters: conn - An sqlite connection object.
    tbl_name - Name of the table in a dataframe, initialized to ISTA_131_F17.
    Returns: grades - A dictionary containing distribution of grades in a class.
    """

    c = conn.cursor()
    conn.row_factory = sqlite3.Row
    q = "SELECT grade, COUNT(*) AS num_studs, ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM " + tbl_name
    q += "), 1) AS percent FROM " + tbl_name + " GROUP BY grade ORDER BY grade;"
    data = c.execute(q).fetchall()
    grades = {}
    for grade in data:
        grades[grade[0]] = grade[2]
    return grades

def improved(conn, tbl_one, tbl_two):
    """
    Purpose: This function returns a list of last names in sorted order of the students who improved their
    grade score from a first class to a second class.
    Parameters: conn - An sqlite connection object.
    tbl_one - Name of the first class table in a dataframe.
    tbl_two - Name of the second class table in a dataframe.
    Returns: names - a list of last names of all the students with improved scores in sorted order.
    """

    c = conn.cursor()
    conn.row_factory = sqlite3.Row
    q = "SELECT tbl1.last FROM " + tbl_one + " as tbl1, " + tbl_two
    q += " AS tbl2 WHERE tbl1.id = tbl2.id AND tbl2.grade > tbl1.grade ORDER BY tbl1.last;"
    names = [name[0] for name in c.execute(q).fetchall()] # Creates a list a list extracting values from tuples.
    return names

def main():
    """
    Purpose: This function creates a dataframe using the csv_to_dataframe function created and formats it, adds a
    "growth rate" column and a "years to extinction" column to the dataframe. From the dataframe it then creates a new
    Series specifying all of the countries with a dying population and prints five countries sorted in order by highest
    dying population.
    Parameters: conn - An sqlite connection object.
    tbl_one - Name of the first class table in a dataframe.
    tbl_two - Name of the second class table in a dataframe.
    Returns: names - a list of last names of all the students with improved scores in sorted order.
    """

    df = csv_to_dataframe('countries_of_the_world.csv')
    format_df(df)
    growth_rate(df)
    years_to_extinction(df)
    dying = dying_countries(df)
    for i in range (0,5):
        print (dying.index[i] + ': ' + str(dying.iloc[i]) + ' Years to Extinction')