# Name: Daniel Ivan Lewis
# Date: 8/31/18
# ISTA 116 Section C
# Lab Assignment 01
# Collaborator(s): Andrew Rickus

source("http://www.openintro.org/stat/data/arbuthnot.R")
source("http://www.openintro.org/stat/data/present.R")

# Question 1
dim(present)
# Ans: The dimensions are 63 rows 3 columns

# Question 2
names(present)
# Ans:  The variables are 'year' 'boys' 'girls'

# Question 3
present$year
# Ans: Years 1940 - 2002

# Question 4
View(arbuthnot)
# Ans: The counts from arbuthnot are far smaller than the counts from the present data set. The scales differ since the present data set has a borader pool of data and arbuthnot focuses on the counts of children that were baptised in a certain church. 

# Question 5
boy_girl_ratio_arb <- (arbuthnot$boys / arbuthnot$girls)
plot(x=arbuthnot$year, y=boy_girl_ratio_arb)
# Ans: According to the data boys are generally born more than girls. 

# Question 6
boy_girl_ratio_pres <- (present$boys / present$girls)
plot(x=present$year, y=boy_girl_ratio_pres)
# Ans: The present day data is much closer together than the arbuthnot data set. 

# Question 7
present[1, "year"]
present[1, "boys"]
# Ans: It gives the value of the variable '2nd index' of the row '1st index' specified. 

# Question 8 
# Ans: The brackets ask R to search for the values within the certain indices provided. The left indices checks for the row, while the right index asks for the variable/column. 

# Question 9
?which.max
# Ans: The function determines the location (index) of the first maxium of a numeric vector. 

# Question 10
present[which.max(present$boys + present$girls) ,"year"]
# Ans: In the year 1961 the sum of boy and girl births were the max from the data set present.
