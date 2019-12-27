"""
Daniel Ivan Lewis
SL: Jessie Sumerau
9/4/2018
ISTA 131 Hw2
Summary: This file contains a few functions working with NumPy and SQL
"""

import numpy as np
import sqlite3
import csv
    
def is_power_of_2(n):
    """ Purpose: This function checks to see if the number passed in is a power of 2. 
  
    Parameters: n - The integer being checked.
  
    Returns: True - if n is a power of 2.
    False - otherwise
    """
    
    i = 0
    while i < n:
        if 2**i == n: #loops through each iteration to check if 2^i = n.
            return True
        i += 1
    return False

def all_power_of_2(matrix):
    """ Purpose: This function checks to see if each number in the matrix
    passed in is a power of 2. 
  
    Parameters: matrix - A non-empty numpy matrix of integers.
  
    Returns: True - if all the numbers within the matrix are powers of 2.
    False - otherwise
    """
    
    for row in matrix:
        for num in row:
            if is_power_of_2(num) == False: #Uses is_power_of_2 as a helper function.
                return False
    return True

def first_divisible(matrix, n = 2):
    """ Purpose: This function returns the first value within a numpy matrix
    that is divisible by the integer n, which is set to 2 by default. 
  
    Parameters: matrix - a non-empty numpy matrix of integers.
    n - an integer, default value is set to 2.
  
    Returns: The first value that is divisible by n, returns an empty list if
    none of the values are divisible by n.
    """
    
    indices = []
    for i in range (0,len(matrix)):
        for j in range (0,len(matrix[i])):
            if matrix[i,j] % n == 0: # checks each value to see if it is divisible by n. 
                indices.append([i,j])
    return indices[0] # returns first value divisible by n that was found. 

def multiples_of_4(matrix):
    """ Purpose: This function returns the values in a numpy matrix that have
    indices that are miltiples of 4. 
  
    Parameters: matrix - A non-empty numpy matrix of integers.
  
    Returns: multiples - a list of all of the values with indices that are
    multiples of 4.
    """
    
    multiples = []
    for i in range (0,len(matrix)):
        for j in range (0,len(matrix[i])):
            if (i + j) % 4 == 0: # adds up indices to see if they are divisible by 4
                multiples.append(matrix[i,j])
    return multiples

def to_array(d):
    """ Purpose: This function returns a numpy matrix of sorted values gathered
    from a dictionary.
  
    Parameters: d - a dictionary mapping keys to a list of numbers
  
    Returns: a numpy matrix containing the sorted values from the d dictionary.
    """
    
    nums = []
    keys = sorted(d.keys())
    for key in keys:
        nums.append(d[key])
    return np.array(nums) # converts matrix into a numpy matrix

def to_table(csv_fname, sql_fname, tbl_name = 'new1'):
    """ Purpose: This function creates a table using sqlite3 and data from a
    csv file. 
  
    Parameters: csv_fname: a csv file containing the data for the table.
    sql_fname - the name of the sqlite3 database that the function will connect to.
    tbl_name - the name of the table that will be created, has 'new1' set as default name.
  
    Returns: NONE - sqlite3 table is created no return.
    """
    
    f = open(csv_fname, 'r')
    lines = f.readlines()

    tbl_variables = lines[0].split(',') # splits the variables into a list

    qmark = ['?']* len(tbl_variables) # sets question marks depending on length of columns
    qmark = '(' + ', '.join(qmark) + ')' # formats question marks to fit sqlite3 syntax
    columns = '(' + tbl_variables[0] + ' text PRIMARY KEY, ' # <---
    remainder = ' text, '.join(tbl_variables[1:])            # block of code creates variables for table in sqlite format
    columns += remainder + ')'                               # <---
    
    conn = sqlite3.connect(sql_fname)
    c = conn.cursor()

    c.execute('CREATE TABLE {}{}'.format(tbl_name, columns))

    for line in lines[1:]: # skips first line that contains variables
        line = line.strip('\n')
        row = line.split(',')
        c.execute('INSERT INTO ' + tbl_name + ' VALUES ' + qmark + ';', tuple(row)) # inserts data each iteration through csv file
        conn.commit()
    conn.close()
    

def to_csv(sql_fname, tbl_name, csv_fname = 'data.csv'):
    """ Purpose: This function uses a table in an sqlite3 database and exports
    a csv file containing the information from the table. 
  
    Parameters: sql_fname - the name of the sqlite3 database that the function will connect to.
    tbl_name - the name of the table that the information is gathered from.
    csv_fname - a csv file that will contain all the information from the table, set to 'data.csv' as default.
  
    Returns: NONE - csv file containing table data is created, nothing returned.
    """
    
    conn = sqlite3.connect(sql_fname)
    c = conn.cursor()

    c.execute('SELECT * FROM ' + tbl_name) # gets all info from table
    columns = c.description # pulls the table variables
    rows = c.fetchall()

    with open(csv_fname, 'w') as csv_file:
        first_row = ""
        for var in columns[:-1]:            # <---- 
            first_row += var[0] + ','       # Block of code gathers all the table variables
        first_row += columns[-1][0]         # and creates the first row in the csv file    
        csv_file.write(first_row + '\n')    # <----
        for row in rows:
            data = ','.join(row)
            csv_file.write(data + '\n')
    conn.close()

def get_students(conn, tbl_name, grade):
    """ Purpose: This function connects to an Sqlite database and returns
    a list of the sorted names of students that have the matching grade passed in.
  
    Parameters: conn - an sql connection passed in
    tbl_name - the name of the table where the information is fetched from
    grade - the grade used to match the students names. 
  
    Returns: a list of sorted names of all the students who have the matching grade passed in.
    """
    
    c = conn.cursor()
    c.execute("SELECT last, first FROM {} WHERE grade=?".format(tbl_name), grade)
    rows = c.fetchall()
    names = []
    for name in rows:
        names.append(name[0] + ", " + name[1])
    return sorted(names)