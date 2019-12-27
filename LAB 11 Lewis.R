# Name: Daniel Ivan Lewis
# Date: 11/9/18
# ISTA 116 Section C
# Lab Assignment 11
# Collaborator(s): None

download.file("http://www.openintro.org/stat/data/nc.RData", destfile = "nc.RData")
load("nc.RData")
nc <- na.omit(nc)

# Question 1:
# Null Hypothesis: Pregnancy lasts 40 weeks. Pregnancy time = 40 weeks. 
# Alternate Hypothesis: Pregnancy does not last 40 weeks. Pregnancy time != 40 weeks.

# Question 2: 
hist(nc$weeks)
# From the histogram created with the code above, we can see that he distribution does seem to be somewhat normal. Hypothesis testing does assume that data is normally distributed, yet, according to the central limit theorem, if the data set contains many values and is of larger scale, a normally distributed data set is not required.

# Question 3:
week.mean <- mean(nc$weeks)
week.SD <- sd(nc$weeks)
week.SE <- (week.SD/sqrt(length(nc$weeks)))
# Answer: Average # of weeks until birth = 38.4675, Standard Deviation = 2.753802, Standard Error = 0.09736159

# Question 4: 
crit.val.99 <- qnorm(1 - (1 - .99) / 2)
# Answer: Crit val = 2.575829

# Question 5:
conf.int99 <- c(week.mean - (crit.val.99*week.SE), week.mean + (crit.val.99*week.SE))
# Answer: Confidence intreval = (38.21671, 38.71829)
# From the answer genreated above, we can see that the null hypothesis, which states that the average weeks it takes for a child to be born is 40, does not fall within our 99% confidence intreval. 

# Question 6:
t.stat <- ((week.mean - 40) / week.SE)
# Answer: T-statistic = -15.74029

# Question 7:
pnorm(t.stat)*2
# Answer: We can see that by using pnorm with the given t.stat, we get a very small number. We also multiply the t test value by 2 since the test is a 2 sided test. The test is two sided since we are not checking to see if the average number of weeks it takes during birth is smaller or larger than the actual mean, instead, we are just looking to see that the average number of weeks it takes for birth is not equal to 40, thus we check both greater than and less than 40. Since the value is less than .05, we reject the null hypothesis. 

# Question 8:
rejection.val <- qnorm(.05, 40, week.SE)

# Question 9:
power.39.and.6.days <- pnorm(rejection.val,39 + 6/7, week.SE)
# Answer: From the value generated above, we get a value of approx. 0.43. This is to be expected since the null hypothesis states that the average weeks during birth are 40, since the values are only off by a week, there is a 43% chance of correctly rejecting the null hypothesis, meaning it is close to the null hypothesis estimation. 

# Question 10:
power.39 <- pnorm(rejection.val,39, week.SE)
# Answer: From the value given by the power of 39 weeks, we can see that the power is much higher at 1, which means that we are correctly rejcting the null hypothesis. 
