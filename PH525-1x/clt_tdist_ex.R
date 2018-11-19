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
cat("With", n, "rolls the fraction of 6s is",sixes_singlerep, "\n")

# We want to roll n dice 10,000 times and keep these proportions. 
# This random variable (proportion of 6s) has mean p=1/6 and variance p*(1-p)/n. 
# So according to CLT z = (mean(x==6) - p) / sqrt(p*(1-p)/n) should be normal with mean 0 and SD 1. 
# Set the seed to 1, then use replicate to perform the simulation, 
# and report what proportion of times z was larger than 2 in absolute value 
# (CLT says it should be about 0.05).


reps <- 10000
set.seed(1)
x_replic <- replicate(reps, sample(1:6, n, replace=TRUE)) # a VERY large array
sixes_replic <- mean(x_replic==6)
cat("With",reps, "replicates of",n,"rolls the fraction of 6s is",sixes_replic, "\n")

# calculate z by scaling
p <- 1/6 # in this case, we know the real population mean 

# now calculate the mean for *each* replicate
# should end up with 10000 elements
sixes_per_rep <- colSums(x_replic == 6)/n 

z <- (sixes_per_rep - p) / sqrt(p*(1-p)/n)
ans <- (mean(abs(z) > 2))
cat("|z| > 2 about",ans*100,"% of the time")

# official answer to ex 1 puts the z calculation inside the replication
# and avoids the megamatrix
#zs <- replicate(10000,{
#  x <- sample(1:sides,n,replace=TRUE)
#  (mean(x==6) - p) / sqrt(p*(1-p)/n)
#})

qqnorm(z)
abline(0,1)#confirm it's well approximated with normal distribution

# ex 2
# Now, the CLT is an asympototic result, meaning it is closer and closer to being a perfect 
# approximation as the sample size increases. In practice ...we need to decide if it is appropriate 
# for actual sample sizes. Is 10 enough? 15? 30?

# In the example used in exercise 1, the original data is binary (either 6 or not). 
# In this case, the success probability also affects the appropriateness of the CLT. 
# With very low probabilities, we need larger sample sizes for the CLT to "kick in".

# Run the simulation from exercise 1, but for different values of p and n. 
# For which of the following is the normal approximation best?
