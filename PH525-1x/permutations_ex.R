# permutations_ex.R

# setup
require(here)
require(rafalib)
require(dplyr)

# load data
babies <- read.table(here("extdata", "babies.txt"), header=TRUE)
bwt.nonsmoke <- filter(babies, smoke==0) %>% select(bwt) %>% unlist 
bwt.smoke <- filter(babies, smoke==1) %>% select(bwt) %>% unlist

# take sample and measure observed difference
N <- 10
set.seed(1)
nonsmokers <- sample(bwt.nonsmoke , N)
smokers <- sample(bwt.smoke , N)
obs <- mean(smokers) - mean(nonsmokers)

# function to permute the datasets
nulldiff <- function(n) { # n = sample size
  dat <- c(smokers,nonsmokers) # smokers are first in the list
  shuffle <- sample(dat) # no argument means that n = length of sample
  smokersstar <- shuffle[1:N] # the simulated smokers under the null
  nonsmokersstar <- shuffle[(N+1):(2*N)] 
  mean(smokersstar)-mean(nonsmokersstar) # diff under the null
}
# Q1 ------------
# Repeat the permutation 1,000 times to create a null distribution. 
# What is the permutation derived p-value for our observation?

n <- 1000
nulldiffs <- replicate(n, nulldiff(n))

hist(nulldiffs)

# for fun, test whether it's normal
qqnorm(nulldiffs)
qqline(nulldiffs)

# just for comparison here's a non-normal distrib
stupiddist <- -100:100
hist(stupiddist)
qqnorm(stupiddist, main="definitely not normal")
qqline(stupiddist)

# t-test calculation (2-sided)
# We add a 1 to the numerator and denominator to account 
# for misestimation of the p-value (for more details see 
# Phipson and Smyth, Permutation P-values should never be zero).
# the proportion of permutations with larger difference

p <- (sum(abs(nulldiffs) > abs(obs)) + 1) / (length(nulldiffs) + 1)
cat(p)

# Q2 --------------
# Repeat the above exercise, but instead of the differences in mean, 
# consider the differences in median obs <- median(smokers) - median(nonsmokers). 
# What is the permutation based p-value?

# nonsmokers <- sample(bwt.nonsmoke , N)
# smokers <- sample(bwt.smoke , N)
obsmed <- median(smokers) - median(nonsmokers)

# function to permute the datasets and take the diff in medians
set.seed(1)
nulldiffmed <- function(n) { # n = sample size
  dat <- c(smokers,nonsmokers) # smokers are first in the list
  shuffle <- sample(dat) # no argument means that n = length of sample
  smokersstar <- shuffle[1:N] # the simulated smokers under the null
  nonsmokersstar <- shuffle[(N+1):(2*N)] 
  median(smokersstar)-median(nonsmokersstar) # diff under the null
}

n <- 1000
nulldiffmeds <- replicate(n, nulldiffmed(n))

hist(nulldiffmeds) # are the diffs in medians normally distrib?
qqnorm(nulldiffmeds, main = "Difference in medians under the null")

# but it doesn't matter if it's normal because we can use monte carlo to 
# determine the proportion of diffs exceeding the observed

pmed <- (sum(abs(nulldiffmeds) > abs(obsmed)) + 1) / (length(nulldiffmeds) + 1)
cat(pmed)
