
# random variables exercises

library(readr)

# get data
fcp <- read_csv("extdata/femaleControlsPopulation.csv")
unl_fcp <- unlist(fcp)

# exercise 2
# After setting the seed at 1, take a random sample of size 5.
# What is the absolute value (use abs) of the difference between
# the average of the sample and the average of all the values?

set.seed(1)
print("Seed 1 ")
pop_mean <- mean(unl_fcp)
samp_mean <- mean(sample(unl_fcp, 5))
samp_delta <- abs(pop_mean - samp_mean)
cat(samp_delta, "\n")

# exercise 3 
# same but set seed at 5

set.seed(5)
print("Seed 5 ")
pop_mean2 <- mean(unl_fcp)
samp_mean2 <- mean(sample(unl_fcp, 5))
samp_delta2 <- abs(pop_mean2 - samp_mean2)
cat(samp_delta2, "\n")


