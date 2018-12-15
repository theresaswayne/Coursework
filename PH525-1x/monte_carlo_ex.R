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

simul_result <- mean(tstats > 2) # proportion > 2 sds from mean (in one direction)

# Ex 3 --------------------------------------------------------------------

set.seed(1)
theor_result <- 1 - pt(2,df=4) # this is within the range of the simulation result
# (can see by repeating simulation without resetting seed)

# To obtain quantiles for the t-distribution 
# we can generate percentiles from just above 0 to just below 1

B <- 100
ps <- seq(1/(B+1), 1-1/(B+1),len=B) 

# and compute the quantiles with 
quantiles <- qt(ps,df=4)

# Now we can use qqplot to compare these theoretical quantiles 
# to those obtained in the Monte Carlo simulation. 

qqplot(quantiles, tstats)
qqline(tstats) # note that this is a line through the stats, not a theoretical one


# Use Monte Carlo simulation developed for exercise 2 
# to corroborate that the t-statistic t= sqrt(N)*mean(X)/s
# follows a t-distribution for several values of N.

Ns <- c(3, 5, 20, 50)
set.seed(1)

sapply(Ns, function(n) { # generates 4 plots
  tstats <- replicate(1000, tstat(n))
  label <- c("tstats, N=",n)
  quantiles <- qt(ps,df=n-1) 
  qqplot(quantiles, tstats, ylab = label)

  # abline(tstats) # regression line through data
  
  # qqline(tstats) # line through 1st & 3rd quartiles of data
  
  # "qqline adds a line to a “theoretical”, by default normal, 
  # quantile-quantile plot which passes through the probs quantiles, 
  # by default the first and third quartiles.

  abline(0,1)
  })

# playing with lines -------------------
set.seed(1)
y <- rt(300, df = 5) # t distrib
qqnorm(y) # generates the plot
qqline(y, col = 2) # orange line ***based on data***
abline(0,1) # line with slope 1 and intercept 0


# official answer
library(rafalib)
mypar(3,2) # sets up panel graph

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
mypar(1,1) # reset graph size
N <- 15 # sample size
B <- 10000 # replications
LIM <- c(-4.5,4.5) # x axis range

ts <- replicate(B, {
  X <- sample(c(-1,1), N, replace=TRUE) # binary data with mean 0
  sqrt(N)*mean(X) / sd(X)
})
ps <- seq(1/(B+1),1-1/(B+1),len=B)
# qqplot(qt(ps,df=N-1),ts, # change df with N
#       xlim=range(tstats)) # this gives a broad range > 5 sds
qqplot(qt(ps,df=N-1),ts, # change df with N
       xlim=LIM) # set a narrower x range for plot
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

# Ex 6 ---------------------
# Is the following statement true or false ? 
# If instead of generating the sample with 
# X=rnorm(N) with N=1000, we generate the data with 
# binary data X= sample(c(-1,1), N, replace=TRUE), then 
# the t-statistic sqrt(N)*mean(X)/sd(X) is approximated 
# by a t-distribution with 999 degrees of freedom.

# based on official answer to previous
set.seed(1)
N <- 1000
B <- 10000
tstats <- replicate(B,{
  X <- sample(c(-1,1), N, replace=TRUE)
  sqrt(N)*mean(X)/sd(X)
})
ps=seq(1/(B+1), 1-1/(B+1), len=B) 
qqplot(qt(ps,N-1), tstats, xlim=range(tstats))
abline(0,1)

# lesson -- large sample size makes the binary data t's fit the t distrib
# because of CLT

# Ex 7-----------------

# ...suppose we are interested in the distribution of a statistic 
# for which a theoretical approximation is not immediately obvious.
# 
# Consider the sample median as an example. 
# Use a Monte Carlo to determine which of the following best 
# approximates the median of a sample taken from normally 
# distributed population with mean 0 and standard deviation 1.

set.seed(1)
N <- 1000 # sample size
B <- 10000 # Monte Carlo reps
medians <- replicate(B,{
  X <- rnorm(N) # take the sample
  median(X) # calculate the median, which will be returned
})
ps=seq(1/(B+1), 1-1/(B+1), len=B) 

# generate the comparative qq plots

# Normal dist with mean 0 and sd 1/sqrt(N)
qqplot(qnorm(p = ps,mean = 0,sd = 1/sqrt(N)), 
      medians, 
      xlim=range(medians)) 
abline(coef = c(0,1), col = 1) # color 1 is green
# it's not very close to this line! slope is different but it does pass through 0

# Normal dist with mean 0 and SD "larger than 1/sqrt(N)"

# Normal dist with mean 0 and sd randomly picked as double the previous
qqplot(qnorm(p = ps,mean = 0,sd = 2/sqrt(N)), 
       medians, 
       xlim=range(medians)) 
abline(coef = c(0,1), col = 1)
# changing SD changed the slope of the qq plot. 
# this time it is on the other side of the identity line.

# Normal dist with mean 0 and sd a bit over 1/sqrt(N)
qqplot(qnorm(p = ps,mean = 0,sd = 1.3/sqrt(N)), 
       medians, 
       xlim=range(medians)) 
abline(coef = c(0,1), col = 1)
# this is very close!!!
# official answer -- ##there is an asymptotic result 
# that says SD is sqrt(N*4*dnorm(0)^2) (dnorm is density distrib fn)

# t distrib for small and normal for large?

set.seed(1)
M <- 10 # small sample size
B <- 10000 # Monte Carlo reps
medians_small_n <- replicate(B,{
  Y <- rnorm(M) # take the sample
  median(Y) # calculate the median, which will be returned
})
ps=seq(1/(B+1), 1-1/(B+1), len=B) 

# t dist with 9 df
qqplot(qt(p = ps,df = M-1), 
       medians_small_n, 
       xlim=range(medians_small_n)) 
abline(coef = c(0,1), col = 1)
# this does not match well.

# Normal dist with mean 0 and sd 1/sqrt(N)
qqplot(qnorm(p = ps,mean = 0,sd = 1/sqrt(M)), 
       medians_small_n, 
       xlim=range(medians_small_n)) 
abline(coef = c(0,1), col = 1)
# this is not a particularly good match either 

