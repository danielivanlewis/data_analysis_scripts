# Name: Daniel Ivan Lewis
# Date: 8/24/18
# ISTA 116 Section C
# Lab Assignment 01
# Collaborator(s): Andrew Rickus

# 1
2+3
# ANSWER: 5

# 2
2 + 3 * 6 - 4
# ANSWER: 16
2+3 * (6-4)
# ANSWER: 8
4/2 * 8
# ANSWER: 16

# 3
# 2 + 3
# ANSWER: No output from the console.

# 4 
2 + 3#
# ANSWER = 5, the console still outputs the answer to the equation. 

# 5
# 5 + 3
# Answer No output
5 + 3 #
# Answer = 8
# Overall Findings: Any input before a '#' will be computed by the console, anything after a '#' will not give any output.

# 6
textbooks
# Answer: Recieved an error message "ERROR: Object 'textbooks' not found"

# 7
library()
# Answer: Opens a script with all the available R packages.

# 8
library(openintro)
# Answer: Attaches the openintro package. 

# 9
TExtBooks
# Answer: "Error: object 'TExtBooks' not found". Case sensitivity has an effect on the input in console. However, Rstudio will attempt to fix case sensitivity by recommending a corrected input. 

#10
plot(x=textbooks$uclaNew, y=textbooks$amazNew)
# Answer: Brings up a scatterplot in the Plot Window showing a comparison of new textbooks purchased from Amazon V.S. UCLA