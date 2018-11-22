# CLT and t-distribution exercises

library(dplyr)
library(rafalib)


dat <- read.csv("femaleMiceWeights.csv")

# Ex 1 --------------------------------------------------------------------

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
cat("|z| > 2 about",ans*100,"% of the time", "\n")

# official answer to ex 1 puts the z calculation inside the replication
# and avoids the megamatrix
#zs <- replicate(10000,{
#  x <- sample(1:sides,n,replace=TRUE)
#  (mean(x==6) - p) / sqrt(p*(1-p)/n)
#})

qqnorm(z)
abline(0,1)#confirm it's well approximated with normal distribution

# Ex 2 --------------------------------------------------------------------

# Now, the CLT is an asympototic result, meaning it is closer and closer to being a perfect 
# approximation as the sample size increases. In practice ...we need to decide if it is appropriate 
# for actual sample sizes. Is 10 enough? 15? 30?

# In the example used in exercise 1, the original data is binary (either 6 or not). 
# In this case, the success probability also affects the appropriateness of the CLT. 
# With very low probabilities, we need larger sample sizes for the CLT to "kick in".

# Run the simulation from exercise 1, but for different values of p and n. 
# For which of the following is the normal approximation best?


# 2a ----------------------------------------------------------------------
n <- 5
set.seed(1)
p <- 0.5
possib <- 1/p
x <- sample(1:possib, n, replace=TRUE)
success_singlerep <- mean(x==possib) # probability that x is one partic number
cat("With", n, "rolls the fraction of success is",success_singlerep, "\n")
reps <- 10000
set.seed(1)
x_replic <- replicate(reps, sample(1:possib, n, replace=TRUE)) # a VERY large array
success_replic <- mean(x_replic==possib)
cat("With",reps, "replicates of",n,"rolls and a p of",p,"the fraction of successs is",success_replic, "\n")
success_per_rep <- colSums(x_replic == possib)/n 
z <- (success_per_rep - p) / sqrt(p*(1-p)/n)
ans <- (mean(abs(z) > 2))
cat("|z| > 2 about",ans*100,"% of the time")
qqnorm(z, main = "(a) p=0.5, n=5")
abline(0,1)#confirm it's well approximated with normal distribution

# 2b ----------------------------------------------------------------------
n <- 30
set.seed(1)
p <- 0.5 
possib <- 1/p
x <- sample(1:possib, n, replace=TRUE)
success_singlerep <- mean(x==possib) # probability that x is one partic number
cat("With", n, "rolls the fraction of success is",success_singlerep, "\n")
reps <- 10000
set.seed(1)
x_replic <- replicate(reps, sample(1:possib, n, replace=TRUE)) # a VERY large array
success_replic <- mean(x_replic==possib)
cat("With",reps, "replicates of",n,"rolls and a p of",p,"the fraction of successs is",success_replic, "\n")
success_per_rep <- colSums(x_replic == possib)/n 
z <- (success_per_rep - p) / sqrt(p*(1-p)/n)
ans <- (mean(abs(z) > 2))
cat("|z| > 2 about",ans*100,"% of the time","\n")
qqnorm(z, main = "(b) p=0.5, n=30")
abline(0,1)#confirm it's well approximated with normal distribution

# 2c ----------------------------------------------------------------------
n <- 30
set.seed(1)
p <- 0.01 
possib <- 1/p
x <- sample(1:possib, n, replace=TRUE)
success_singlerep <- mean(x==possib) # probability that x is one partic number
cat("With", n, "rolls the fraction of success is",success_singlerep, "\n")
reps <- 10000
set.seed(1)
x_replic <- replicate(reps, sample(1:possib, n, replace=TRUE)) # a VERY large array
success_replic <- mean(x_replic==possib)
cat("With",reps, "replicates of",n,"rolls and a p of",p,"the fraction of successs is",success_replic, "\n")
success_per_rep <- colSums(x_replic == possib)/n 
z <- (success_per_rep - p) / sqrt(p*(1-p)/n)
ans <- (mean(abs(z) > 2))
cat("|z| > 2 about",ans*100,"% of the time","\n")
qqnorm(z, main = "(c) p=0.01, n=30")
abline(0,1)#confirm it's well approximated with normal distribution

# 2d ----------------------------------------------------------------------
n <- 100
set.seed(1)
p <- 0.01 # for dice
possib <- 1/p
x <- sample(1:possib, n, replace=TRUE)
success_singlerep <- mean(x==possib) # probability that x is one partic number
cat("With", n, "rolls the fraction of success is",success_singlerep, "\n")
reps <- 10000
set.seed(1)
x_replic <- replicate(reps, sample(1:possib, n, replace=TRUE)) # a VERY large array
success_replic <- mean(x_replic==possib)
cat("With",reps, "replicates of",n,"rolls and a p of",p,"the fraction of successs is",success_replic, "\n")
success_per_rep <- colSums(x_replic == possib)/n 
z <- (success_per_rep - p) / sqrt(p*(1-p)/n)
ans <- (mean(abs(z) > 2))
cat("|z| > 2 about",ans*100,"% of the time", "\n")
qqnorm(z, main = "(d) p=0.01, n=100")
abline(0,1)#confirm it's well approximated with normal distribution


# Ex 3 --------------------------------------------------------------------

X <- filter(dat, Diet=="chow") %>% select(Bodyweight) %>% unlist
Y <- filter(dat, Diet=="hf") %>% select(Bodyweight) %>% unlist
cat(mean(X), "\n")

# Ex 8 --------------------------------------------------------------------

# What is the estimate of SE (Xbar-Ybar)
# = sqrt((sigma^2x)/12 + (sigma^2y/12))

se <- sqrt( sd(X)^2/12 + sd(Y)^2/12 )
cat("SE:", se,"\n") # null hypoth using both actual samples

#sqrt( sd(X)^2/12 + sd(Y)^2/12 )
# 1.469867

# Ex 9  --------------------------------------------------------------------
# tstat = diff/(se of diff)

se_diff <- sqrt( 
  var(Y)/length(Y) + 
    var(X)/length(X) 
)
tstat <- (mean(Y)-mean(X))/se_diff
cat("The t statistic:",tstat, "\n")

cat(t.test(X, Y)$p.value, "\n")

Z <- ( mean(Y) - mean(X) ) / sqrt( var(X)/12 + var(Y)/12)
2*( 1-pnorm(Z)) 
