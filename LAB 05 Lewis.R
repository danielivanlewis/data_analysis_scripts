# Name: Daniel Ivan Lewis
# Date: 9/21/18
# ISTA 116 Section C
# Lab Assignment 05
# Collaborator(s): Phong Vo

download.file("http://www.openintro.org/stat/data/kobe.RData", destfile = "kobe.RData")
load("kobe.RData")

# Question 1:
kobe.basket.prob <- prop.table(table(kobe$basket))

# Question 2:
hits <- kobe.basket.prob['H']

# Question 3:
first.13 <- (kobe$basket[1:13])
first.13
calc_streak(first.13)
# Answer: The function calc_streak calculates how many times Kobe makes a shot (Looks for 'H' in data passed through). Once a streak ends, the function prints out the number of the streak and resets the streak to 0, If kobe misses the function prints out a '0'. The process is repeated until all values in the vector are counted.

# Question 4:
barplot(table(calc_streak(kobe$basket)), ylim=c(0,40))

# Question 5:
new.player.sample <- sample(c('H','M'), length(kobe$basket), prob = c(hits, 1-hits),replace=TRUE)

# Question 6:
new.player.prob <- prop.table(table(new.player.sample))
# Answer: According to the new table provided, Kobe's probability distribution does differ from the new player's probability distribution, this is to be expected since the new players data only uses the same probability with each value generated, it does not mean it is exactly the same values. However, it can also be seen that the probability for both Kobe and the new player are fairly close to each other. 

# Question 7:
barplot(table(calc_streak(new.player.sample)), ylim = c(0,40))
# Answer: Both Kobe's and the new players barplot are very similar. However, the new player does have some variation, for example, in the barplot generated, the new player misses more than Kobe, but also has a 9 shot streak, yet, it is somewhat consistent to Kobe's barplot as well. 

# Question 8:
newplayer.streak.prob <- prop.table(table(calc_streak(new.player.sample)))
# Answer: As far as the probability of both players streaks. There are some variations between both, although the new player genreated had higher sized streaks, his percentage of missing a shot was about 10% higher than Kobe's. Yet they do show a similar trend in streaks, the higher the amount of shots in a streak, the lower the probaility is. 

# Question 9:
replicate(100, {
  s = sample(c('H','M'), length(kobe$basket), prob = c(hits, 1-hits),replace=TRUE);
  probs = prop.table(table(calc_streak(s)))['0']
})
# Answer: From the values generated, it seems as though Kobe's probability of missing a shot is, for the most part, on the lower side than most of the generated samples. However, it is within range of all of the values produced from the replicate function. 

# Question 10:
replicate(100, {
  s = sample(c('H','M'), length(kobe$basket), prob = c(hits, 1-hits),replace=TRUE);
  probs = prop.table(table(calc_streak(s)))['3']
})
# Answer: As far as the information gathered through the replicate function. It can be seen that there is a great amount of variation between the shots that are generated. However, for the most part, he is on the higher side of the values that were generated. 


