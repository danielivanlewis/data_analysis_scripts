# Name: Daniel Ivan Lewis
# Date: 9/07/18
# ISTA 116 Section C
# Lab Assignment 04
# Collaborator(s): Phong Vo

library(openintro)

# Question 1
boxplot(heartTr$survtime)
# Answer: From the boxplot produced with the survtime column within the heartTr data, it appears as though there are approximately 10 outliers within the data. 

# Question 2
surv.time <- (heartTr$survtime)
boxplot(log(surv.time))
# Answer: After creating a new boxplot with the log transformed survtime data, there are no longer any visible outliers within the boxplot produced. 

# Question 3
# Answer: The benefit of using the boxplot produced with the log transformed data is that it gets rid of the outliers and gives a better representation of the distribution of the data. 

# Question 4
table(heartTr$survived, heartTr$transplant)
# Answer: According to the contingency table produced, only 4 people out of the control group survived.

# Question 5
prop.table(table(heartTr$survived, heartTr$transplant), margin = 2)
# Answer: From the proportion table produced, the treatment group is more likely to survive than those in the control group. Approximately 34.9% of the treatment group end up alive and only about 11.8% of the control group end up surviving. 

# Question 6
prop.table(table(heartTr$survived, heartTr$transplant), margin = 1)
# Answer: The row proportions differ from the column proportions in that it shows the proportion of control or treatment subjects out of all of the individuals that survived, or died, as opposed to the column proportions that show proportions of subjects that survived or died based off of the group that each individual pertained to. 

# Question 7
barplot(table(heartTr$survived, heartTr$acceptyear))
# Answer: From the stacked barplot created, it can be seen that as time goes by, the people who survived the heart transplant increased as the years go on, as far as deaths, there seems to be no clear correlation and it is evident that deaths still occur throughout the years, except the final year of 74, where all subjects lived. 

# Question 8
help("barplot")
# Answer: In order to include legends in a barplot, the argument "legend.text =" needs to be passed in to the barplot funciton. 

# Question 9
barplot(prop.table(table(heartTr$transplant, heartTr$acceptyear), margin = 2), legend.text = TRUE)
# Answer: From the barplot created, it looks as though the proportion of the control group genreally decreases throughout each year. While the treatment group tends to increase from year to year until the final year, when it switches back to a majority of control groups patients rather than treatment group patients. 

# Question 10
mosaicplot(table(heartTr$acceptyear, heartTr$transplant))
# Answer: Although the mosaic plot and the barplot created from the porportion tables are very similar, it seems as though the mosaic plot adjusts the size of each 'bin' according to the amount of people who were used to gather data, some years, the bins are smaller than the other bins.