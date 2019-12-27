# Name: Daniel Ivan Lewis
# Date: 9/07/18
# ISTA 116 Section C
# Lab Assignment 03
# Collaborator(s): Andrew Rickus

source("http://www.openintro.org/stat/data/cdc.R")

# Question 1
plot(cdc$weight ~ cdc$wtdesire)
# ANS: For the most part, from the scatterplot it can be inferred that people who weight more have a lower weight desire than people who weight less, where people are more satisfied with their weight and the difference between weight and desired weight are less. 
# Question 2
wdiff <- (cdc$weight - cdc$wtdesire)
View (wdiff)
# ANS: wdiff represents the amount of weight that each individual wishes to lose/gain. If a person wdiff variable is equal to 0, that means that they are satisfied with their current weight, if wdiff is positive, that is the amount that an individual wishes to lose to achieve their desired weight, and if wdiff is negative, it represents the amount of weight that an individual wants to put on/gain.

# Question 3
median(wdiff)
# ANS: The center of the wdiff distribution is 10. That means that when the data is sorted from least to greatest, the center point of all of the data has an individual who wishes to lose 10 pounds. Median is used to determine the center point of the data since it shows the exact middle point of all the data values collected.

# Question 4
hist(wdiff,100)
# ANS: From the histogram created, it can be inferred that the wdiff data has a skew to the right, this means that some people want to lose greater amounts of weight that creates the skew. In order to get a clearer visual the amount of buckets in the histogram was set to 100.

# Question 5
# ANS: The shape and spread of the histogram show that there are many people who are either satisfied with their weight or wish to lose a bit more weight as opposed to the people who wish to gain a bit of weight or want to lose greater amounts of weight. Since there are people who wish to lose significantly more, it creates a skew in the data to the right.
# Question 6
boxplot(wdiff ~ cdc$gender)
# ANS: According to the boxplots, the way in which men and women view their weight slightly differs. For the most part women have a slight increase in the amount of weight they wish to lose than men. However, the men boxplot does have a significantly higher amount of individuals that wish to gain weight as opposed to women. 

# Question 7
# ANS: When manually inspecting the boxplots, the only two outliers that seem like they might be a data error are within the mens boxplot, the two further outliers would represent that one individual wishes to gain about 500 lbs while another individual wishes to gain 300 pounds.

# Question 8
wt.mean <- mean(cdc$weight)
wt.sdev <- sd(cdc$weight)
one.sdev.abv <- (wt.mean + wt.sdev)
two.sdev.abv <- (one.sdev.abv + wt.sdev)
one.sdev.blw <- (wt.mean - wt.sdev)
two.sdev.blw <- (one.sdev.blw - wt.sdev)
within.one.dev <- cdc$weight[(cdc$weight <= one.sdev.abv)&(cdc$weight >= one.sdev.blw)]
within.two.dev <- cdc$weight[(cdc$weight <= two.sdev.abv)&(cdc$weight >= two.sdev.blw)]
perc.one.dev <- (length(within.one.dev)/length(cdc$weight)) * 100
perc.two.dev <- (length(within.two.dev)/length(cdc$weight)) * 100
# ANSWERS 
# one standard deviation below = 129.602
# two standard deviations below = 89.52101
# one standard deviation above = 209.7639
# two standard deviations above = 249.8449
# Percent of data within one standard dev of mean = 70.76%
# Percent of data within two standard dev of mean = 95.63%

# Question 9
ht.mean <- mean(cdc$height)
ht.sdev <- sd(cdc$height)
one.sdev.abv.ht <- (ht.mean + ht.sdev)
two.sdev.abv.ht <- (one.sdev.abv.ht + ht.sdev)
one.sdev.blw.ht <- (ht.mean - ht.sdev)
two.sdev.blw.ht <- (one.sdev.blw.ht - ht.sdev)
within.one.dev.ht <- cdc$height[(cdc$height <= one.sdev.abv.ht)&(cdc$height >= one.sdev.blw.ht)]
within.two.dev.ht <- cdc$height[(cdc$height <= two.sdev.abv.ht)&(cdc$height >= two.sdev.blw.ht)]
perc.one.dev.ht <- (length(within.one.dev.ht)/length(cdc$height)) * 100
perc.two.dev.ht <- (length(within.two.dev.ht)/length(cdc$height)) * 100
# ANSWERS 
# ----- For Height ------
# one standard deviation below = 63.05695
# two standard deviations below = 58.93099
# one standard deviation above = 71.30885
# two standard deviations above = 75.43481
# Percent of data within one standard dev of mean = 62.125%
# Percent of data within two standard dev of mean = 97.725%

ag.mean <- mean(cdc$age)
ag.sdev <- sd(cdc$age)
one.sdev.abv.ag <- (ag.mean + ag.sdev)
two.sdev.abv.ag <- (one.sdev.abv.ag + ag.sdev)
one.sdev.blw.ag <- (ag.mean - ag.sdev)
two.sdev.blw.ag <- (one.sdev.blw.ag - ag.sdev)
within.one.dev.ag <- cdc$age[(cdc$age <= one.sdev.abv.ag)&(cdc$age >= one.sdev.blw.ag)]
within.two.dev.ag <- cdc$age[(cdc$age <= two.sdev.abv.ag)&(cdc$age >= two.sdev.blw.ag)]
perc.one.dev.ag <- (length(within.one.dev.ag)/length(cdc$age)) * 100
perc.two.dev.ag <- (length(within.two.dev.ag)/length(cdc$age)) * 100
# ANSWERS 
# ----- For Age ------
# one standard deviation below = 27.87556
# two standard deviations below = 10.68287
# one standard deviation above = 62.26094
# two standard deviations above = 79.45363
# Percent of data within one standard dev of mean = 64.03%
# Percent of data within two standard dev of mean = 96.93%