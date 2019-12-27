# Name: Daniel Ivan Lewis
# Date: 9/28/18
# ISTA 116 Section C
# Lab Assignment 06
# Collaborator(s): Kevin Velasquez

# Question 1:
ranks <- c('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
suits <- c ('Spade', 'Heart', 'Diamond', 'Club')

# Question 2:
cards <- expand.grid(ranks=ranks, suits=suits)

# Question 3:
card.prob <- prop.table(table(cards))
suit.prob <- colSums(card.prob)
rank.prob <- rowSums(card.prob)
prob.of.spade <- suit.prob['Spade']
prob.of.ace <- rank.prob['Ace']
prob.of.aceofspades <- card.prob['Ace','Spade']
# Answers: Probability of Spade: 0.25; Probability of Ace: 0.07692308; Probability of Ace of Spades: 0.01923077.

# Question 4:
sample.indices <- sample(1:nrow(cards), 10)
sample.cards = cards[sample.indices,]

# Question 5:
cards.without.sample <- cards[-(sample.indices),]
card.prob.wo.sample <- prop.table(table(cards.without.sample))
suit.prob.wo.sample <- colSums(card.prob.wo.sample)
rank.prob.wo.sample <- rowSums(card.prob.wo.sample)
prob.of.spade.wo.sample <- suit.prob.wo.sample['Spade']
prob.of.ace.wo.sample <- rank.prob.wo.sample['Ace']
prob.of.aceofspades.wo.sample <- card.prob.wo.sample['Ace','Spade']
# Answer: Probability of Spade w/o sample: 0.2619048; Probability of Ace w/o sample: 0.07142857; Probability of Ace of Spades w/o sample: 0.02380952. After removing the sample from the deck of cards, the probabilites change. This is due to removing the cards without replacement. In this situation, the Ace of Spades probability and the Spade probability went up, this is due to none of those cards being selected in the random sample, therefore those cards remain but there is now a lesser amount in the deck as a whole, which leads to a higher probability. However, some probabilities, such as the probability of the selecting an Ace decreased, since one of the cards in the sample was an Ace card.

# Question 6:
sidesofDice <- c(1,2,3,4,5,6)
diceCombinations <- expand.grid(dice1=sidesofDice, dice2=sidesofDice, dice3=sidesofDice)

# Question 7:
sumofComb <- rowSums(diceCombinations)
diceCombinations$sumOfCombinations = sumofComb

# Question 8:
sum.of.dice.props <- barplot(table(diceCombinations$sumOfCombinations))
# Answer: The two most likely outcomes that occur throughout would be a sum of 11, or a sum of 10.

# Question 9:
sums <- replicate(1000, {
  s = sum(sample(sidesofDice, 3, replace = TRUE));
})
barplot(prop.table(table(sums)))
# Answer: According to the barplot generated with the code above, it seems as though the information gatherd with the replicate function is close to the findings from question 8. However, ther is some variation. For instance, the barplot from the replicate values have the outcomes 9 and 13 as the most probable to occur. Therefore, although the distribution of the values are close, there are still some differences. 

# Question 10:
sums.5.dice <- replicate(1000, {
  s = sum((sort(sample(sidesofDice, 5, replace = TRUE)))[c(3,4,5)]);
})
barplot(prop.table(table(sums.5.dice)))
# Answer: From the barplot generated with the code above, there is now a noticeable left skew in the distribution. This is due to the fact that the sum of the highest three numbers are being collected from the outcomes of 5 dice, where as the distribution from questions 8 and 9 were more symmetrical. 