# Name: Daniel Ivan Lewis
# Date: 10/26/18
# ISTA 116 Section C
# Lab Assignment 09
# Collaborator(s): None

download.file("http://www.openintro.org/stat/data/ames.RData", destfile = "ames.RData")
load("ames.RData")

# Question 1
Gr.Liv.mean <- mean(ames$Gr.Liv.Area)

# Question 2
Gr.Liv.sample <- sample(ames$Gr.Liv.Area, size=50, replace=FALSE)
Gr.Liv.sample.mean <- mean(Gr.Liv.sample)
# Answer: From the code generated above, it looks as though the mean for the entire data comes out to 1499.69, whereas the mean for the sample of 50 created comes out to 1477.02. There is a bit of a difference between both averages due to the fact that the sample is of a small size compared to the length of the actual data set which has 2930 values. The bigger the sample size, the closer it will be to the actual average of the full data set. 

# Question 3
par(mfrow=c(2,1)) # Sets plotting area to 2 Rows and 1 column, top and bottom plots. 
area.xlim <- range(ames$Gr.Liv.Area)

# Question 4
hist(ames$Gr.Liv.Area, xlim=area.xlim)
abline(v=Gr.Liv.mean, col='red')

# Question 5
hist(Gr.Liv.sample, xlim=area.xlim)
abline(v=Gr.Liv.sample.mean, col='red')
# Answer: Looking at the two graphs created, it looks as though the distribution of both graphs are very similar. However, there are some differences between both. To start off the abline from the top graph (normal data set) is marked at a higher X value, this is due to the fact that the mean from the sample was a bit lower than the actual mean. Most of the data from both of the graphs fall between 1000 - 2000 size range, but the bottom graph(sample) has a break between 2500 - 3000, this is due to the size of the sample, If there were more values added it would be more likely that the graph would resemble a closer view of the actual distribution of the data; nevertheless, they have a fairly close resemblance. 

# Question 6
par(mfrow=c(1,1)) # Reverts the view of the plots back to single plot view. 
area.means.10 <- replicate(5000, {
  s = sample(ames$Gr.Liv.Area, size=10, replace=FALSE);
  mean = mean(s)
})
hist(area.means.10) # Plots a histogram of means from sample of size 10.

# Question 7
area.means.50 <- replicate(5000, { # Gathers 5000 means from samples of size 50.
  s = sample(ames$Gr.Liv.Area, size=50, replace=FALSE);
  mean = mean(s)
})
area.means.100 <- replicate(5000, { # Gathers 5000 means from samples of size 100.
  s = sample(ames$Gr.Liv.Area, size=100, replace=FALSE);
  mean = mean(s)
})

# Question 8
par(mfrow=c(3,1)) # Sets view of plot box to 3 Rows and 1 column.
area.means.10.xlim <- range(area.means.10)

# Question 9
hist(area.means.10, xlim= area.means.10.xlim, breaks= 20)
hist(area.means.50, xlim= area.means.10.xlim, breaks= 20)
hist(area.means.100, xlim= area.means.10.xlim, breaks= 20)
# Answer: If I were to choose between a sample size of 10, 50, or 100, to estimate the mean of a full data set, It would be best to use the 100 sized sample means. This is due to the fact that as the sample size increases, the variation from the actual mean decreases. In other words, the means get closer to the actual mean as the sample size increases. If you look at the graphs generated from the code above, the distribution of the graphs keep contracting and getting closer to the actual mean of the data set as the size of the sample increases.

# Question 10
# Answer: The distributions of means for samples of size 1 would closely resemble the original data set, while the distribution of means for samples of size 2930 would just be one bin at the actual mean of the data set, since the sample is without replacement, It would just gather the same actual mean 5000 times.