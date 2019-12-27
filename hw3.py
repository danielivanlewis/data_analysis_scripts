"""
Daniel Ivan Lewis
SL: Jessie Sumerau
09/20/2018
ISTA 131 Hw3
Summary: This module includes various functions working with pandas and SQL.
"""
import pandas as pd
import sqlite3
import datetime as dt
from datetime import timedelta

def student_report(db, student_id):
    """
    Purpose: This function connects to a database and returns a string for the student containing his grade info for
    each class within the database.
    Parameters: db - The name of a database connection.
    student_id - A unique int for each student within the database.
    Returns: A String containing class and grade information.
    """
    conn = sqlite3.connect(db) # Connects to database passed in.
    c = conn.cursor()
    q = "select name from sqlite_master where type = 'table';"
    tables = c.execute(q).fetchall()
    grades = [] # Initializes an empty list to keep clean strings of grades and classes.
    name = '' # Initializes an empty string for 'last name, first name, student id' format.
    for table in tables: # Loops through each table in database.
        table = table[0] # Pulls out table name from tuple returned by execute command
        q = 'SELECT last, first, grade FROM ' + table + ' where id = ' + str(student_id) + ';'
        info = c.execute(q).fetchall() # Pulls query from database.
        if len(info) != 0: # Makes sure info collected contains student information.
            if name == '': # Initializes name once, thereafter skips step.
                name = str(info[0][0]) + ', ' + str(info[0][1]) + ', ' + str(student_id) # Creates name format needed.
            cls_name = table.replace('_', ' ') # Cleans up class name by replacing '_' to spaces in class name.
            grades.append(cls_name + ': ' + str(info[0][2])) # Adds students grade to class name
    returnval = name + '\n' + (len(name) * '-') + '\n'
    for grade in sorted(grades):
        returnval += grade + '\n'
    conn.close()
    if returnval.strip('\n') == '': # If student not found in database, returns empty string.
        return ''
    else:
        return returnval

def A_students(conn, tbl_name = 'ISTA_131_F17', standing = None, max_num = 10):
    """
    Purpose: This function connects to a database and returns a list of the names of the students who recived
    an A in that course, up to *max_num* rows.
    Parameters: db - The name of a database connection.
    standing - A students grade level.
    tbl_name - the name of a table, set to ISTA_131_F17 as default.
    Returns: A String containing class and grade information.
    """
    c = conn.cursor()
    conn.row_factory = sqlite3.Row
    names = [] # Empty list that will hold all the names of students who got A's
    if standing == None: # Creates query that does not search on standing.
        query = 'SELECT last, first FROM ' + tbl_name + " WHERE grade = 'A' ORDER BY last, first LIMIT "
        query += str(max_num) + ';'
    else: # Creates a query including standing passed in by user.
        query = 'SELECT last, first FROM '  + tbl_name + " WHERE grade = 'A' AND standing LIKE '" + standing.lower()
        query += "' ORDER BY last, first LIMIT " + str(max_num) + ';'
    try: #Checks to see if level is used instead of standing for table column name.
        data_from_tbl = c.execute(query).fetchall() # Collects all the data from query passed in.
    except sqlite3.OperationalError: # Changes standing to level in query.
        query = 'SELECT last, first FROM ' + tbl_name + " WHERE grade = 'A' AND level LIKE '" + standing.lower()
        query += "' ORDER BY last, first LIMIT " + str(max_num) + ';'
        data_from_tbl = c.execute(query).fetchall()  # Collects all the data from query passed in.

    for name in data_from_tbl: # Goes through each item in list and converts to string in 'last, first' format.
        names.append(name[0] + ', ' + name[1])
    return names

def class_performance(conn, tbl_name = 'ISTA_131_F17'):
    """
    Purpose: This function connects to a database returns the percentages of students who recieved an A in that course.
    Parameters: conn - A connection to a database.
    tbl_name - set to ISTA_131_F17 as default.
    Returns: A dictionary mapping course names to the percentage of students who recieved A's in that class.
    """
    c = conn.cursor()
    conn.row_factory = sqlite3.Row
    grades = c.execute('SELECT DISTINCT grade FROM ' + tbl_name).fetchall()  # Pulls each distinct grade from table.
    grades_avail = [grade[0] for grade in grades]  # Gives a cleaned up list of all available grades throughout course.
    grade_counts = {}
    total_student_num = c.execute('SELECT COUNT(*) FROM ' + tbl_name + ';').fetchone()[0]
    for grade in grades_avail:
        count = c.execute('SELECT COUNT(*) FROM ' + tbl_name + " WHERE grade ='" + grade + "';").fetchone()[0]
        percent = round(((int(count) / total_student_num) * 100), 1)
        grade_counts[grade.upper()] = percent
    return grade_counts

def read_frame(csv = 'sunrise_sunset.csv'):
    """
    Purpose: This function opens a csv file with pandas.read_csv function. Returns the data collected.
    Parameters: csv - the name of a csv file.
    Returns: A DataFrame object from the csv file passed in.
    """
    months = ['Jan_r', 'Jan_s', 'Feb_r', 'Feb_s', 'Mar_r', 'Mar_s', 'Apr_r', 'Apr_s', 'May_r', 'May_s',
              'Jun_r', 'Jun_s', 'Jul_r', 'Jul_s', 'Aug_r', 'Aug_s', 'Sep_r', 'Sep_s', 'Oct_r', 'Oct_s',
              'Nov_r', 'Nov_s', 'Dec_r', 'Dec_s'] # Creates column names for database.
    return pd.read_csv(csv, names=months, dtype = str) # Returns values as str.

def get_series(df):
    """
    Purpose: This function splits the previous DataFrame into two seperate categories, sunrise, and sunset. .
    Parameters: df - A DataFrame object.
    Returns: Two DataFrame objects, one for sunrise info and one for sunset info.
    """
    first_day_of_yr = dt.datetime(year = 2018, month = 1, day = 1) # Creates first day of year
    final_day_of_yr = dt.datetime(year = 2018, month = 12, day = 31) # Creates final day of year
    dates = pd.date_range(first_day_of_yr, final_day_of_yr) # Creates range of dates throughout year / index for Series.
    info = [] # Create empty list that will store data pulled by data frame by column.
    for cols in df:
        raw_data = (df[cols])  # Pulls data from data frame including NaN values.
        data = raw_data.dropna().values # Removes NaN values from each column.
        info.append(data) # Appends cleaned up values for each column.
    sunrise_data = [] # Empty list will hold sunrise values.
    sunset_data = [] # Sunset values
    for i in range(0, len(info)):
        if i % 2 == 0: # If even index, values go towards sunrise data.
            for val in info[i]:
                sunrise_data.append(val)
        else:
            for val in info[i]: # If odd index, values go towards sunset data.
                sunset_data.append(val)
    rise = pd.Series(data = sunrise_data, index = dates)  # Creates final series
    set = pd.Series(data = sunset_data, index = dates)
    return rise, set

def longest_day(sunrise, sunset):
    """
    Purpose: This function returns a datetime object of the longest day in the year, as  well as the difference between
    the rising time in minutes.
    Parameters: sunrise - A sunrise data frame.
    sunset - A sunset data frame.
    Returns: A timestamp of the longest day this year and a string containing the sunrise time in minutes.
    """
    s = sunset.astype(dtype=int) # Coverts strings to ints.
    r = sunrise.astype(dtype=int)
    day_lengths = (s - r) # Substracts the sunrise time from the sunset time.
    longest = day_lengths.idxmax() # Gets the datetime object of the longest day.
    mins = str(day_lengths[longest]) # Gets the time in minutes of the longest day and converts it to a string.
    return longest, mins
    # Answer: According to Google, the summer solstice is on Thursday June 21st 2018, from function generated, the value
    # that it returns shows June 18th being the summer solstice. For the most part, both dates are fairly close which proves
    # that the function is somewhat accurate.

def sunrise_dif(sunrise, timestamp):
    """
    Purpose: This function returns the difference of minutes between 90 days before and 90 days after the timestamp
    passed in from the sunrise series.
    Parameters: sunrise - A sunrise data frame.
    Returns: The difference of minutes between 90 days before and 90 days after the timestamp
    passed in
    """
    date = timestamp.date()
    ninety_before = date - timedelta(90) # Gets the date for 90 minutes before date passed in.
    ninety_after = date + timedelta(90) # Gets the date for 90 minutes after date passed in.
    mins_before = int(sunrise[ninety_before]) # Gets the sunrise time of before 90 days.
    mins_before = int(str(mins_before)[0]) * 60 + int(str(mins_before)[-2:])
    mins_after = int(sunrise[ninety_after])
    mins_after = int(str(mins_after)[0]) * 60 + int(str(mins_after)[-2:])
    diff = (mins_before - mins_after) # Finds the difference between minutes.
    return diff