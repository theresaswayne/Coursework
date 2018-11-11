# populations, samples, estimates exercises

library(dplyr)
library(readr)

dat <- read_csv("extdata/mice_pheno.csv")

# remove lines that contain missing values
dat <- na.omit(dat)

# Exercise 1
# Use dplyr to create a vector x 
# with the body weight of all males on the control (chow) diet. 
# What is this population's average?

x <- filter(dat, Diet == "chow" & Sex == "M") %>% 
  select(Bodyweight) %>%
  unlist

print("Exercise 1")
print(mean(x))

# Exercise 2
# Now use the rafalib package and use the popsd function 
# to compute the population standard deviation.

library(rafalib)

print("Exercise 2")
print(popsd(x))

# Exercise 3
# Set the seed at 1. 
# Take a random sample  of size 25 from x. 
# What is the sample average?

set.seed(1)
samp25x <- sample(x, 25)
print("Exercise 3")
print(mean(samp25x))

# Exercise 4
# Use dplyr to create a vector y with the body weight 
# of all males on the high fat hf) diet. 
# What is this population's average?

y <- filter(dat, Diet == "hf" & Sex == "M") %>% 
  select(Bodyweight) %>%
  unlist

print("Exercise 4")
print(mean(y))

# Exercise 5
# Now use the rafalib package and use the popsd function 
# to compute the population standard deviation.

print("Exercise 5")
print(popsd(y))

# Exercise 6
# Set the seed at 1. 
# Take a random sample  of size 25 from y. 
# What is the sample average?

set.seed(1)
samp25y <- sample(y, 25)
print("Exercise 6")
print(mean(samp25y))

# Exercise 7
# What is the difference in absolute value between 
# (ybar - xbar) and (Ybar- Xbar)?
# [i.e. the diffs based on population means and those based on sample means?]

diffPopMeans <- abs(mean(y)-mean(x))
diffSampMeans <- abs(mean(samp25y) - mean(samp25x))
ans <- diffPopMeans - diffSampMeans
print("Exercise 7")
print(ans)

# Exercise 8
# Repeat the above for females. 
xF <- filter(dat, Diet == "chow" & Sex == "F") %>% 
  select(Bodyweight) %>%
  unlist

set.seed(1)
samp25xF <- sample(xF, 25)

yF <- filter(dat, Diet == "hf" & Sex == "F") %>% 
  select(Bodyweight) %>%
  unlist

set.seed(1)
samp25yF <- sample(yF, 25)

diffPopMeansF <- abs(mean(yF)-mean(xF))
diffSampMeansF <- abs(mean(samp25yF) - mean(samp25xF))
ansF <- abs(diffPopMeansF - diffSampMeansF)

print("Exercise 8")
print(ansF)