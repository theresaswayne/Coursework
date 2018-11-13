# central limit theorem exercises

library(dplyr)
library(rafalib)

filename <- "extdata/mice_pheno.csv"
dat <- na.omit( read.csv(filename) )

# ex 4
# Define y to be the weights of males on the control diet. 
# What proportion of the mice are within one standard deviation 
# away from the average weight 
# (remember to use popsd for the population sd)?

y <- filter(dat, Diet == "chow" & Sex == "M") %>%
  select(Bodyweight) %>%
  unlist

pop_mean <- mean(y) 
pop_sd <- popsd(y)
ans4 <- (mean(y < pop_mean + pop_sd & y > pop_mean - pop_sd))

# official answer with comments
# z <- ( y - mean(y) ) / popsd(y) # z score is the deviation from mean div by the sd
# mean( abs(z) <=1 ) # z score of 1 means it is 1 sd from the mean

# ex 5
# What proportion of these numbers are within two 
# standard deviations away from the list's average?
z <- (y-pop_mean)/pop_sd
ans5 <- mean (abs(z < 2)) # note the <= answer is not accepted but this one is
print(ans5)
ans5b <- (mean(y < (pop_mean + (2*pop_sd)) & y > pop_mean - (2*pop_sd)))
print(ans5b)
 
 # ex 6
 # What proportion of these numbers are within two 
 # standard deviations away from the list's average?
 
ans6 <- mean(abs(z <3 ))
print("Exercise 6")
print(ans6)

# ex 9
# We will now take a sample of size 25 from the population of males on the chow diet. 
# The average of this sample is our random variable. 
# We will use the replicate function to observe 10,000 realizations of this random variable. 
# Set the seed at 1, generate these 10,000 averages. 
# Make a histogram and qq-plot of these 10,000 numbers 
# against the normal distribution.

avgs <- replicate(10000, mean( sample(y, 25)))
mypar(1,2)
hist(avgs)
qqnorm(avgs)
qqline(avgs)

samp_avg <- mean(avgs)
print("Ex9")
print(samp_avg)
samp_sd <- popsd(avgs)
r_sd <- sd(avgs)
print("Ex 10")
print(samp_sd)
print(r_sd)
