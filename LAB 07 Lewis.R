# Name: Daniel Ivan Lewis
# Date: 10/12/18
# ISTA 116 Section C
# Lab Assignment 06
# Collaborator(s): None

# Question 1:
game <- data.frame(prob = c(1/6, 1/6, 1/6, 1/6, 1/6, 1/6), score = c(100, 0, 0, 0, 50, 0))

# Question 2:
scores <- sample(game$score, size = 10000, prob = game$prob, replace = TRUE)
score.hist <- hist(scores, ylim = c(0, 7000))
# Answer: From the histogram created with the sample above, it can be seen that there are only three available outcomes for the game, either scoring 0, 50, or 100 points. As expected, the histogram shows 0 occuring the most at around 6,500 times, and scoring 50 or 100 at around 2000 occurences each. This is expected becuase the probability of scoring 0 in the game is 4/6, while the probability of scoring 50 or 100 are both 1/6. 

# Question 3:
theoretical.mean <- mean(scores)
actual.expected.value <- weighted.mean(game$score, game$prob)
# Answer: The sample mean does differ slightly from the expected value. This is to be expected since the sample created was has some randomness to it. However, the both the mean from the sample created and the expected value are very close. The expected value generated was 25, while the actual mean of the samples generated turned out to be 24.715 after running the code above. Although they are not exact, they are very close to being so. 

# Question 4:
theoretical.sd <- sd(scores) # Standard deviation of sample created
actual.sd <- sd(game$score) # Actual standard deviation
#Answer: The theoretical standard deviation generated from the code above also shows some deviation than the actual standard deviation. The theoretical standard deviation from the sample created came out to 38.11908 after running the code above, while the actual standard deviation of the game would be 41.833. Therefore, as expected, both values are close, but not the same. Once again this is due to the fact that the sample created has some randomness applied to it. 

# Question 5:
loaded.game <- data.frame(prob = c(0.1, 0.1, 0.1, 0.1, 0.5, 0.1), score = c(100, 0, 0, 0, 50, 0))

# Question 6:
loaded.game.scores <- sample(loaded.game$score, size = 10000, prob = loaded.game$prob, replace = TRUE)
loaded.game.scores.hist <- hist(loaded.game.scores, ylim = c(0, 6000))
# Answer: The possible outcomes/score of the loaded game remain the same as the possible outcomes of the regular die game, however, if the die is loaded, the probabilities will differ. For the loaded die game, the probabilities of scoring 0 points would sum to 0.4, the probability of scoring 50 points would be 0.5, and the probability of scoring 100 points would be 0.1. Therefore, it makes sense that out of the 10,000 rolls created with the sample function, the result for scoring 0 points is 3,947/10,000, the result for scoring 50 points is 4,978/10,000, and scoring 100 points is 1,075/10,000. All the actual values are close to the probabilities of each outcome. 

# Question 7:
loaded.theoretical.mean <- mean(loaded.game.scores)
loaded.actual.expected.value <- weighted.mean(loaded.game$score, loaded.game$prob)
# Answer: After running the code above, it can be inferred that on average a player would score 10 points more by using the loaded dice rather than the regular dice. This can be caulcuated by getting the expected value of the loaded die game, which would be 35, and substracting the expected value of the regular die game, which is 25. This can be confirmed by gathering the theoretical values of both the loaded die game and the regular die game. Which in this case came out to 35.64 - 24.715, which means the player scored 10.925 points more by using the loaded die. 

# Question 8:
two.dice.game <- replicate(10000, sample(game$score, size = 1, prob = game$prob, replace = TRUE) + sample(loaded.game$score, size = 1, prob = loaded.game$prob, replace = TRUE))
two.dice.hist <- hist(two.dice.game)
# Answer: As far as the modes in the histogram created with the two dice game there are more bins than the previous histograms from questions 3 and 6. This is due to the fact that there are more possible outcomes. The sum of the two scores can either be 0, 50, 100, 150, or 200. 

# Question 9:
two.dice.game.mean <- mean(two.dice.game)
theoretical.two.dice <- theoretical.mean + loaded.theoretical.mean
# Answer: The values for the expected value and sample mean of the two dice game are much higher than the original game due to the fact that there are two dice being rolled. Not only that, but the value also increases due to the fact that the probability of scoring 50 is 50% with a loaded die, which increase the overall score for the two dice game. 

# Question 10:
five.dice.game <- replicate(10000, sum(replicate(2,sample(game$score, size = 1, prob = game$prob, replace = TRUE))) + sum(replicate(3,sample(loaded.game$score, size = 1, prob = loaded.game$prob, replace = TRUE)))/5)
five.dice.game.mean <- mean(five.dice.game)
theoretical.five.dice <- ((theoretical.mean*2) + (loaded.theoretical.mean*3))/5
# Answer: According to the code above, the five dice game has an average of 71.74, while the expected value of the five dice game is 45.88. The reason why the expected value is lower is due to the variation in randomness that is added by the samples used. 

# Question 11:
# Answer: If playing with one regular die would cost 5 points, playing with a loaded die would cost 15 points, and playing with 5 dice costs 10 points, it would be best to play the 5 dice game. This is due to the fact that the theoretical avereges for these games are represented as the following. 1 normal die = 25.245 - 5 = 20.245, 1 loaded die = 34.77 - 15 = 19.77, and the five dice game = 30.96 - 10 = 20.96. Therfore, playing the 5 dice game would theoretically end up with a larger amount of net points over the course of the game. 