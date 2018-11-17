# CLT and t-distribution exercises

library(dplyr)
library(rafalib)


dat <- read.csv("femaleMiceWeights.csv")

#Ex 1

# Suppose we are interested in the proportion of times we see a 6 when rolling n=100 die. 
# This is a random variable which we can simulate with x=sample(1:6, n, replace=TRUE) 
# and the proportion we are interested in can be expressed as an average: mean(x==6). 
# Because the die rolls are independent, the CLT applies.

n <- 100
set.seed(1)
x <- sample(1:6, n, replace=TRUE)
sixes_singlerep <- mean(x==6)
cat("With", n, "rolls the fraction of 6s is",sixes_singlerep)

# We want to roll n dice 10,000 times and keep these proportions. 
# This random variable (proportion of 6s) has mean p=1/6 and variance p*(1-p)/n. 
# So according to CLT z = (mean(x==6) - p) / sqrt(p*(1-p)/n) should be normal with mean 0 and SD 1. 
# Set the seed to 1, then use replicate to perform the simulation, 
# and report what proportion of times z was larger than 2 in absolute value 
# (CLT says it should be about 0.05).

set.seed(1)
reps <- 10000
x_replic <- replicate(reps, sample(1:6, n, replace=TRUE))
sixes_replic <- mean(x_replic==6)
cat("With",reps, "replicates of",n,"rolls the fraction of 6s is",sixes_replic, "\n")
# calculate z by scaling
p <- 1/6 # we know this mean independently
z <- (mean(x_replic==6) - p) / sqrt(p*(1-p)/n)
ans <- (mean(abs(z) > 2))
print(ans)
