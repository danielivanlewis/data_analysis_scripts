"""
Daniel Ivan Lewis
SL: Jessie Sumerau
08/30/2018
ISTA 131 Hw1
Summary: This module includes various functions working with pythons
built in data structures. 
"""

def is_diagonal(matrix):
    """ Purpose: Checks the matrix passed in to make sure that the matrix is a diagonal matrix.
    A matrix that has only zeroes in any position other than its diagonal line. 
  
    Parameters: matrix - A non-empty 2d list structure.
  
    Returns: True - if matrix is a diagonal matrix
    False - otherwise
    """
    i = 0
    for row in matrix:
        if i == 0:
            remainder = row[i+1:] # Only if checking first row of matrix
        else:
            remainder = row[:i] + row[i+1:]
        for elem in remainder:
            if elem != 0: # if any element in remainder matrix is not diagonal. 
                return False
        i += 1
    return True

def is_upper_triangular(matrix):
    """ Purpose: Checks the matrix passed in to make sure that the matrix is an upper triangular matrix.
    A matrix that has only zeroes below its diagonal line. 
  
    Parameters: matrix - A non-empty 2d list structure.
  
    Returns: True - if matrix is a triangular matrix
    False - otherwise
    """
    i = 0
    for row in matrix:
        if i == 0: # disreguards first row in matrix
            remainder = [0]
        else:
            remainder = row[:i]
        for elem in remainder: # only checks values below diagonal line
            if elem != 0: 
                return False
        i += 1
    return True

def contains(matrix, val):
    """ Purpose: Checks the matrix passed in to see if the value passed in can be
    found anywhere throughout the matrix. 
  
    Parameters: matrix - A non-empty 2d list structure.
    val - the value being checked for within the matrix.
  
    Returns: True - if val is found in matrix
    False - otherwise
    """
    for row in matrix:
        if val in row:
            return True
    return False

def biggest(matrix):
    """ Purpose: Checks the matrix passed in and returns the biggest value. 
  
    Parameters: matrix - A non-empty 2d list structure.
  
    Returns: maximum - the biggest value found in the matrix.
    """
    maximum = (max(matrix[0]))
    for i in range (1,len(matrix)):
        row = matrix[i]
        if maximum < max(row):
            maximum = max(row)
    return maximum
        
def indices_biggest(matrix):
    """ Purpose: Returns the indices of the biggest value found in a matrix. 
  
    Parameters: matrix - A non-empty 2d list structure.
  
    Returns: indices - the indices of the biggest value from within the matrix.
    """
    for i in range (0,len(matrix)):
        if i == 0:
            maximum = matrix[i][0] # initializes the maximum and indices values.
            indices = [0,0]
        for j in range (0,len(matrix[i])):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
                indices = [i,j]
    return indices

def second_biggest(matrix):
    """ Purpose: Returns the second biggest value from within a matrix. 
  
    Parameters: matrix - A non-empty 2d list structure.
  
    Returns: The second biggest value from within the matrix.
    """
    nums = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            nums.append(matrix[i][j])
    nums = sorted(nums)
    return nums[-2] # nums ordered least to greatest, pulls second biggest.
            
def indices_second_biggest(matrix):
    """ Purpose: Returns the indices of the second biggest value from within a matrix. 
  
    Parameters: matrix - A non-empty 2d list structure.
  
    Returns: The indices of the second biggest value from within the matrix.
    """
    nums = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            nums.append(matrix[i][j])
    nums = sorted(nums)
    if len(nums) > 1: # cheks to make sure the list is greater than one. 
        second_biggest = nums[-2]
    else:
        return [0,0] # matrix passed in only has one value returns [0,0]
    for i in range(len(matrix)): # loops through matrix to find first instance of second biggest.
        for j in range(len(matrix[i])):
            if matrix[i][j] == second_biggest:
                return [i,j]

def substr_in_values(d, substr):
    """ Purpose: Returns a sorted list containing all the keys in the d dictionary that
    have values that contain the substr string within those values. 
  
    Parameters: d - a dictionary of keys set to lists of values
    substr - the string being used to find the keys in dict d
  
    Returns: A sorted list of all the keys that have values that contain the
    substr string.
    """
    keys = []
    for key, val in d.items():
        for string in val:
            if substr.lower() in string.lower(): # avoids case sensitivity
                keys.append(key)
    return sorted(list(set(keys)))

def indices_divisible_by_3(matrix):
    """ Purpose: Returns a list of all the values within the indices that are
    divisible by 3 within a matrix. 
  
    Parameters: matrix - A non-empty 2d list structure.
  
    Returns: A list of all the values within a matrix in an indicies that is
    divisible by 3.
    """
    divby3 = []
    for i in range (0,len(matrix)):
        for j in range (0,len(matrix[i])):
            if (i + j) % 3 == 0:
                divby3.append(matrix[i][j])
    return divby3

def sort_int_string(string):
    """ Purpose: Returns a sorted string of numbers seperated by spaces by passing in a string of
    numbers seperated by whitespace. 
  
    Parameters: string - a string of numbers seperated by whitespace.
  
    Returns: A sorted string of numbers seperated by spaces.
    """
    nums = (string.split())
    sortlist = [] # sorted list containing ints
    f_list = [] # final list that converts nums back to strings
    for num in nums:
        sortlist.append(int(num))
    sortlist = sorted(sortlist)
    for num in sortlist:
        f_list.append(str(num)) # converts sorted ints back to strings
    return " ".join(f_list)
                
def dups_lol(lol):
    """ Purpose: Checks to see if a list of list contains any values that are duplicates. 
  
    Parameters: lol -  a list of list containing any values.
  
    Returns: True - if any value repeats itself within the list of lists passed in.
    False - otherwise. 
    """
    dups = []
    for row in lol:
        for char in row:
            if char not in dups:
                dups.append(char)
            else:
                return True
    return False
            
def dups_dict(d):
    """ Purpose: Checks to see if a dictionary contains any values that are duplicates. 
  
    Parameters: d -  a dictionary mapping keys to lists of values.
  
    Returns: True - if any value repeats itself within anywhere in the dictionary.
    False - otherwise. 
    """
    dups = []
    for key, val in d.items():
        for char in val:
            if char not in dups:
                dups.append(char)
            else:
                return True
    return False
