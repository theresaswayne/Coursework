# monte_carlo_ex.R

# Ex 1 --------------------------------------------------------------------

# Set the seed at 1, use rnorm to generate a random sample of size 5,  
# from a standard normal distribution, 
# then compute the t-statistic t = sqrt(5) * mean(x)/s
# with s the sample standard deviation. 
# What value do you observe?

set.seed(1)
N <- 5
samp5 <- rnorm(5)
t <- sqrt(N)*mean(samp5)/sd(samp5)

# Ex 2 --------------------------------------------------------------------

# Set the seed to 1, generate 1000 t-statistics as done in exercise 1. 
# What proportion is larger than 2?

set.seed(1)
tstat <- function(n) { # n = sample size
  samp <- rnorm(n)
  t <- sqrt(n)*mean(samp)/sd(samp)
}

tstats <- replicate(1000, tstat(N))

# returns a boolean

simul_result <- mean(tstats > 2) # proportion > 2 sds from mean

# Ex 3 --------------------------------------------------------------------

set.seed(1)
theor_result <- 1-pt(2,df=4) # this is 0.058, not 0.68, why??

# To obtain quantiles for the t-distribution 
# we can generate percentiles from just above 0 to just below 1

B <- 100
ps <- seq(1/(B+1), 1-1/(B+1),len=B) 

# and compute the quantiles with 
quantiles <- qt(ps,df=4)

# Now we can use qqplot to compare these theoretical quantiles 
# to those obtained in the Monte Carlo simulation. 

qqplot(quantiles, tstats)
qqline(tstats)

# Use Monte Carlo simulation developed for exercise 2 
# to corroborate that the t-statistic t= sqrt(N)*mean(X)/s
# follows a t-distribution for several values of N.

Ns <- c(3, 5, 20, 50)
set.seed(1)

sapply(Ns, function(n) {
  tstats <- replicate(1000, tstat(n))
  label <- c("tstats, N=",n)
  quantiles <- qt(ps,df=n-1) 
  qqplot(quantiles, tstats, ylab = label)
  # abline(tstats) 
  qqline(tstats) # generates 4 plots
})

# official answer
library(rafalib)
mypar(3,2)

Ns<-seq(5,30,5)
B <- 1000
mypar(3,2)
LIM <- c(-4.5,4.5)
for(N in Ns){
  ts <- replicate(B, {
    X <- rnorm(N)
    sqrt(N)*mean(X)/sd(X)
  })
  ps <- seq(1/(B+1),1-1/(B+1),len=B)
  qqplot(qt(ps,df=N-1),ts,main=N,
         xlab="Theoretical",ylab="Observed",
         xlim=LIM, ylim=LIM)
  abline(0,1)
} 


# Ex 4 --------------------------------------------------------------------

# Use Monte Carlo simulation to corroborate that the t-statistic 
# comparing two means and obtained with normally distributed (mean 0 and sd) data 
# follows a t-distribution. In this case we will use 
# the t.test function with var.equal=TRUE. With this argument 
# the degrees of freedom will be df=2*N-2 with N the sample size. 
# For which sample sizes does the approximation best work?

# based on official answer to previous problem

set.seed(1)

mypar(3,2) # graph parameters

Ns<-seq(5,30,5) # 5 to 30 inclusive, in increments of 5
B <- 1000 # sample size
LIM <- c(-4.5,4.5) # x axis range
for(N in Ns){
  ts <- replicate(B, {
    X <- rnorm(N)
    Y <- rnorm(N)
    t.test(X, Y, var.equal = TRUE)$stat # returns the t statistic
  })
  ps <- seq(1/(B+1),1-1/(B+1),len=B)
  qqplot(qt(ps,df=2*N-2),ts,main=N,
         xlab="Theoretical",ylab="Observed",
         xlim=LIM, ylim=LIM)
  abline(0,1)
} 

# Ex 5 --------------------------------------------------------------------

# Is the following statement true or false? 
# If instead of generating the sample with X=rnorm(15) 
# we generate it with binary data (either positive or negative 1 with probability 0.5) 
# X =sample(c(-1,1), 15, replace=TRUE) 
# then the t-statistic
# tstat <- sqrt(15)*mean(X) / sd(X)
# is approximated by a t-distribution with 14 degrees of freedom.

set.seed(1)
N <- 15 # sample size
B <- 10000 # replications
LIM <- c(-4.5,4.5) # x axis range

ts <- replicate(B, {
  X <- sample(c(-1,1), N, replace=TRUE) # binary data with mean 0
  sqrt(N)*mean(X) / sd(X)
})
ps <- seq(1/(B+1),1-1/(B+1),len=B)
qqplot(qt(ps,df=N-1),ts, # change df with N
       xlim=range(tstats))
abline(0,1)

# official answer
set.seed(1)
N <- 15
B <- 10000
tstats <- replicate(B,{
  X <- sample(c(-1,1), N, replace=TRUE)
  sqrt(N)*mean(X)/sd(X)
})
ps=seq(1/(B+1), 1-1/(B+1), len=B) 
qqplot(qt(ps,N-1), tstats, xlim=range(tstats))
abline(0,1)
#The population data is not normal thus the theory does not apply.
#We check with a Monte Carlo simulation. The qqplot shows a large tail. 
#Note that there is a small but positive chance that all the X are the same.
##In this case the denominator is 0 and the t-statistics is not defined
