# Name: Daniel Ivan Lewis
# Date: 11/30/18
# ISTA 116 Section C
# Lab Assignment 13
# Collaborator(s): None

download.file("http://www.openintro.org/stat/data/atheism.RData", destfile = "atheism.RData")
load("atheism.RData")

# Question 1:
# Answer: From the summary given by the report. It can be seen that the information gathered is from the sample gathered from WIN-Gallups global poll about religion standings. Therfore, all of the information gathered is not population based as it would be impossible to get the full worldwide population to participate in the poll, rather, it is a summary of the findings from the sample representing the global population. 

# Question 2:
us <- subset(atheism, nationality == 'United States')
atheism.us <- table(us$year, us$response)

# Question 3:
prop.table(atheism.us,1)
# Answer: From the information gathered above. We can see that in 2012 the percentage of people who classified themselves as an athiest is approximately 5%, which leaves approx. 95% as non-atheiests. From the table on pages 15 & 16 from the study report, we also see the same information. Only 5% classified themselves as true atheists while the rest of the classifications add up to 95%. This confirms that the summary given at the beginning of the report is based off of the sample information gathered from the study. 

# Question 4:
response.pooled.p<-prop.table(colSums(atheism.us))
row.count<-rowSums(atheism.us)
outer(row.count,response.pooled.p)
# Since we can see that there are at least 10 observed successes and failures
prop.test(as.table(atheism.us["2012",]), alternative = "greater")
# Answer: 95% Confidence intreval: 0.03930392 1.00000000

# Question 5:
prop.test(as.table(atheism.us["2012",]),p=.13)
# Answer: From the information given above. We can see that we fail to reject the null hypothesis, thus concluding that the global percentage of 13% is simlar to the U.S. percentage of atheist in 2012.

# Question 6:
response.pooled.p<-prop.table(colSums(atheism.us))
row.count<-rowSums(atheism.us)
outer(row.count,response.pooled.p)
prop.test(as.table(atheism.us))
# Answer: From the information given above, we see that both 2012 and 2005 include 10 observed successes and failures which reach conditions. 2005 has a proportion of 0.00998004 which is lower than 2014. 

# Question 7:
n <- 1000
p <- seq(0,1,0.01)
SE <- sqrt((p*(1-p))/n)

# Question 8:
plot(SE~p)
# Answer: From the graph generated above, we can see that we would have the largest confidence intreval with a p value of .5

# Question 9: 
# a)
spain <- subset(atheism, nationality == "Spain")
atheism.spain <- table(spain$year, spain$response)
# b)
response.pooled.p <- prop.table(colSums((atheism.spain)))
row.count <- rowSums(atheism.spain)
outer(row.count, response.pooled.p)
# There are at least 10 observations for each, conditions are met.
#c)
prop.test(as.table(atheism.spain))
# Answer: With a p value of 0.4375, we conclude that there is not enough evidence to conclude that spain has changed in its atheism index between 2005 and 2014. 

# Question 10:
brazil <- subset(atheism, nationality == "Brazil")
atheism.brazil <- table(brazil$year, brazil$response)
colombia <- subset(atheism, nationality == "Colombia")
atheism.colombia <- table(colombia$year, colombia$response)

bra.col <- rbind(atheism.brazil, atheism.colombia["2012",])
prop.test(as.table(bra.col))
# Answer: With a low p value of 0.0007942 we can not conclude that ther is enough evidence to conclude that the proportion of atheists in Colombia was higher than the proportion of atheists in Brazil. 