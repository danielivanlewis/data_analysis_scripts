"""
Daniel Ivan Lewis
SL: Sebastian
10/25/2018
ISTA 131 Hw7
Collaborator(s): Logan Forsythe
Summary: This module works with pandas and matplotlib. The module passes in a March and September frame and collects the
averages of each year from 1980 to 2015, it also generates the anomaly information for those months and creates a summary
of the information for each month as well as visual representations using Matplotlib.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import math
import matplotlib.pyplot as plt

def get_Mar_Sept_frame():
    """
    Purpose: This function grabs information from the csv file 'data_79_17.csv' and creates a new dataframe with the
    averages of arctic sea ice extent for March and September for each year from 1979 to 2017. The data frame also
    includes columns with the anomalies for both months, which are calculated by substracting the average of each year
    with the overall mean for all years.
    Parameters: None
    Returns: Data frame including averages of arctic sea ice for March and September as well as the anomalies of both
    months from the year 1979 to 2017.
    """
    df = pd.read_csv('data_79_17.csv', index_col = 0)
    march = df.loc[:,'0301':'0331']  # Gets all values for month of March
    sept = df.loc[:, '0901':'0931']  # Gets all values for month of September
    mar_avg = []  # Creates an empty list to keep the averages for March
    for i in range (0,len(march.index)):
        mar_avg.append(march.iloc[i].mean())  # Calculates the average for the month of march for each year, appends to mar_avg list
    mar_avg = np.array(mar_avg)  # Converts to an np array to perform calculation on all values.
    mar_anom = mar_avg - mar_avg.mean()
    # The following block of code repeats the process for the month of september
    sept_avg = []
    for i in range (0,len(sept.index)):
        sept_avg.append(sept.iloc[i].mean())
    sept_avg = np.array(sept_avg)
    sept_anom = sept_avg - sept_avg.mean()

    cols = ['March_means', 'March_anomalies', 'September_means', 'September_anomalies']
    data = []
    for i in range (0,len(mar_avg)):
        data.append([list(mar_avg)[i], list(mar_anom)[i], list(sept_avg)[i], list(sept_anom)[i]])  # Converts data to
    return pd.DataFrame(index=df.index, columns=cols, data=data, dtype=np.float64)                 # proper format

def get_ols_parameters(srs):
    """
    Purpose: This function passes in a series and returns the slope, intercept, rsquared value, and p value for that
    series, returns it in form of a list in that order.
    Parameters: srs - A series passed in
    Returns: a list of the following values in order: [slope, intercept, rsquared, p value]
    """

    x = srs.index.values # gets years from September_March series created above.
    x = sm.add_constant(x)
    model = sm.OLS(srs,x) # creates stats model
    line = model.fit() # fits a line of regression
    return [line.params[1], line.params[0], line.rsquared, line.f_pvalue]  # Returns values specified above

def make_prediction(params, description='x-intercept:', x_name='x', y_name='y', ceiling=False):
    """
    Purpose: This function passes in information from the get_ols_parameter function and returns a summary of the
    information gathered. Other parameters add information to summary but are not required to be passed in.
    Parameters: params - list with following information [slope, intercept, rsquared, p value],
    description - set to x-intercept as default
    x_name - name of x label, set to 'x' as default
    y_name - name of y label, set ot 'y' as default
    ceiling - set to False as default, if set to True, uses math.ceiling to round X-intercept, does not otherwise.
    Returns: None, prints a summary of the params information generated from the get_ols_params function.
    """

    x_int = -(params[1]) / params[0]  # Calculates the x intercept using the slope and the Y intercept.
    if ceiling == True: # Rounds the x int if ceiling param set to True
        x_int = math.ceil(x_int)
    print (description + ' ' + str(x_int))  # Prints first line of summary
    print (str(int(round(params[2] * 100))) + '% of variation in ' + y_name + ' accounted for by ' +
           x_name + ' (linear model)')
    print ('Significance level of results: ' + str(round(params[3] * 100,1)) + '%')
    if params[3] > 0.05:  # checks to see if p-value is above 0.05, to show significance level.
        print ('This result is not statistically significant.')
    else:
        print ('This result is statistically significant.')

def make_fig_1(frame):
    """
    Purpose: This function creates a figure to plot information of the averages of arctic sea ice extent for the months
    of March and September, it also adds 'best fit line' to the data by using the slope from the get_ols_params func.
    Returns: None, plots data for first figure displayed (info mentioned above).
    """

    mm = frame['March_means']
    plt.ylabel('NH Sea Ice Extent $(10^6km^2)$', fontsize=20)
    plt.xticks([i for i in range(1980,2020, 5)])
    plt.yticks([i for i in range(4, 18, 2)])
    plt.title('The Anomaly', fontsize=20)
    # Generates info on march mean column and creates points for abline using slope and intercept from get_ols function
    params_m = get_ols_parameters(mm)
    abline_m = [params_m[0] * i + params_m[1] for i in range (mm.index[0],mm.index[-1])]
    ablinesrs_m = pd.Series(index=[i for i in range (mm.index[0],mm.index[-1])], data=abline_m)
    # Repeats the above steps for the september mean column
    sepm = frame['September_means']
    params_s = get_ols_parameters(sepm)
    abline_s = [params_s[0] * i + params_s[1] for i in range (sepm.index[0],sepm.index[-1])]
    ablinesrs_s = pd.Series(index=[i for i in range (sepm.index[0],sepm.index[-1])], data=abline_s)
    # Plots all of the information gathered above
    plt.plot(mm)
    plt.plot(sepm)
    plt.plot(ablinesrs_m)
    plt.plot(ablinesrs_s)

def make_fig_2(frame):
    """
    Purpose: This function creates a figure to plot information of the anomalies of arctic sea ice extent for the months
    of March and September, it also adds 'best fit line' to the data by using the slope from the get_ols_params func.
    Returns: None, plots data for second figure displayed (info mentioned above).
    """

    ma = frame['March_anomalies']
    plt.ylabel('NH Sea Ice Extent $(10^6km^2)$', fontsize=20)
    plt.xticks([i for i in range(1980,2020, 5)])
    plt.yticks([-2,-1,0,1])
    # Generates info on march anomalies column and creates data for best fit line using slope from get_ols_params func.
    params_m = get_ols_parameters(ma)
    abline_m = [params_m[0] * i + params_m[1] for i in range (ma.index[0],ma.index[-1])]
    ablinesrs_m = pd.Series(index=[i for i in range (ma.index[0],ma.index[-1])], data=abline_m)
    # Repeats the above steps for the september anomalies column
    sepa = frame['September_anomalies']
    params_s = get_ols_parameters(sepa)
    abline_s = [params_s[0] * i + params_s[1] for i in range (sepa.index[0],sepa.index[-1])]
    ablinesrs_s = pd.Series(index=[i for i in range (sepa.index[0],sepa.index[-1])], data=abline_s)
    # Plots all of the data generated above.
    plt.plot(ma)
    plt.plot(sepa)
    plt.plot(ablinesrs_m)
    plt.plot(ablinesrs_s)

def main():
    """
    Purpose: The main function creates the March september frame using the get_Mar_Sept_frame function and uses
    get_ols_params function to print out a summary of the month of March, then repeats step for the month of September.
    Then creates and plots two figures, one with the averages of arctic sea ice for the month of March and Sept. as well
    as one for the anomaly info for both March and Sept.
    Returns: None, prints out two summaries, one of March data and one of Sept. data, then plots both figures created
    with the make_fig_1 function and the make_fig_2 function.
    """

    msframe = get_Mar_Sept_frame()  # Creates the data frame from CSV file
    params = get_ols_parameters(msframe['March_means'])  # Gets param info for March
    make_prediction(params)  # Prints out March info.
    print ()
    params = get_ols_parameters(msframe['September_means'])  # Gets param info for Sept.
    make_prediction(params)  # Prints out Sept. info
    make_fig_1(msframe)  # Creates March and Sept. mean figure.
    plt.figure()
    make_fig_2(msframe)  # Creates March and Sept. anomaly figure.
    plt.show()

main()