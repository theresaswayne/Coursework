# normal distribution exercises

library(dplyr)

x <- read_csv("extdata/femaleControlsPopulation.csv")
x <- unlist(x) # dataframe to vector, required for sample function
# Here x represents the weights for the entire population.

# Using the same process as before (in Null Distribution Exercises), set the seed at 1, then using a for-loop take a random sample of 5 mice 1,000 times. Save these averages. After that, set the seed at 1, then using a for-loop take a random sample of 50 mice 1,000 times. Save these averages.

set.seed(1)

# samples of 5
sampSize <- 5
n <- 1000
mean5 <- vector("numeric",n)

for(i in 1:n) {
  samp <- sample(x,5)
  mean5[i] <- mean(samp)
}

#hist(mean5, main = "Samples of 5", xlim = c(20,30))

# samples of 50
sampSize <- 50
n <- 1000
mean50 <- vector("numeric",n)

for(i in 1:n) {
  samp <- sample(x,55)
  mean50[i] <- mean(samp)
}

#hist(mean50, main = "Samples of 50", xlim = c(20,30))

# For the last set of averages, the ones obtained from a sample size of 50, 
# what proportion are between 23 and 25?

ans2 <- mean((mean50 > 23) & (mean50 < 25))

print("Answer 2")
print(ans2)

# Now ask the same question of a normal distribution 
# with average 23.9 and standard deviation 0.43.

# from text:
# We can compute the proportion of values below a value x 
# with pnorm(x,mu,sigma) without knowing all the values. 


ans3 <- pnorm(25, 23.9, 0.43) - pnorm(23, 23.9, 0.43)
print("Answer 3")
print(ans3)



