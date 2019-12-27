# Name: Daniel Ivan Lewis
# Date: 11/2/18
# ISTA 116 Section C
# Lab Assignment 10
# Collaborator(s): None

download.file("http://www.openintro.org/stat/data/ames.RData", destfile = "ames.RData")
load("ames.RData")

# Question 1:
gr.liv.sample <- sample(ames$Gr.Liv.Area, size=60, replace=FALSE)
gr.liv.sample.mean <- mean(gr.liv.sample)
# Answer: From the sample of 60 created, the sample mean came out to 1399.25.

# Question 2:
gr.liv.sample.sdev <- sd(gr.liv.sample)
gr.liv.sample.serr <- gr.liv.sample.sdev / sqrt(length(gr.liv.sample))
# Answer: The sample standard deviation from the sample came out to 475.3894, which was then used to calculate the standard error for the sample, which is calculated using the following formula: sample sd / sqaure root(sample size). As a result, we get a value of approx 61.4 for the standard error of the sample.

# Question 3:
sample.95conf.intreval <- c(gr.liv.sample.mean - (gr.liv.sample.serr * 1.96), gr.liv.sample.mean + (gr.liv.sample.serr * 1.96))
# Answer: To calculate the 95% confidence intreval for the sample, the following equation was used: sample mean - (sample standard error * 1.96) for the lower boundary, and sample mean + (sample standard error * 1.96), which results in the following values (lower boundary = 1278.96, upper boundary = 1519.54) according to our sample.

# Question 4:
pop.mean <- mean(ames$Gr.Liv.Area)
# The true population mean is 1499.69.

# Question 5:
sample.intrevals <- replicate(50, {s = sample(ames$Gr.Liv.Area, size=60); intreval = c(mean(s) - (sd(s)/sqrt(60))*1.96, mean(s) + (sd(s)/sqrt(60))*1.96)})
dim(sample.intrevals)
# Answer: According to the dim() function, the return value given for the sample.intrevals function is (2,50), which is as expected since we want a matrix of two rows with 50 columns (dim() function returns 'num of rows, num  of columns'). 

# Question 6:
lower.bounds <- sample.intrevals[1,]
upper.bounds <- sample.intrevals[2,]
length(lower.bounds)
length(upper.bounds)
# Answer: Both of the lower.bounds and upper.bounds variable contain 50 values each, which is what we are expecting. 

# Question 7:
plot_ci(lower.bounds, upper.bounds, pop.mean)
# Answer: From the plot_ci function, we are given a clear representation that the sample intrevals created do fall in within 95% confidence level. This is due to the fact that from the sample values generated, only 3 of the samples do not contain the true mean of the population. 50 - 3 or (number of intrevals generated - intrevals that do not contain true population mean) = 47. Which means 47 of the values do contain the poulation mean. Therefore, 47/50 = .94 which is close to .95, this means that out of the samples generated, we can expect that 94 percent of our sample intrevals generated will contain the true population mean. In other words, the samples generated are very close but not exact, which is expected since there is some level of randomness.

# Question 8:
crit.val.90 <- qnorm(1 -(1-.90)/2)
# Answer: From the equation given in the slides above, a critical value for a confidence level of 90% results in 1.644854.

# Question 9:
sample.intrevals.90 <- replicate(50, {s = sample(ames$Gr.Liv.Area, size=60); intreval = c(mean(s) - (sd(s)/sqrt(60))*crit.val.90, mean(s) + (sd(s)/sqrt(60))*crit.val.90)})
lower.bounds.90 <- sample.intrevals.90[1,]
upper.bounds.90 <- sample.intrevals.90[2,]

# Question 10:
plot_ci(lower.bounds.90, upper.bounds.90, pop.mean)
# Answer: From the plot generated with the plot_ci function. It is seen that 6 out of the 50 confidence intrevals do not contain the true population mean. This means that 88% of the confidence intrevals contain the true mean population, which is expected since it is close to 90%. This is to be expected since the confidence intreval was lowered to 90% there will be more confidence intrevals that will not contain the population mean, thus resulting in a lower value than the value given in question #7. 
