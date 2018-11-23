# t-test_ex.R

library(dplyr)
library(rafalib)

babies <- read.table("./extdata/babies.txt", header=TRUE)
bwt.nonsmoke <- filter(babies, smoke==0) %>% select(bwt) %>% unlist 
bwt.smoke <- filter(babies, smoke==1) %>% select(bwt) %>% unlist

mean(bwt.nonsmoke)-mean(bwt.smoke) # difference between "population" means
popsd(bwt.nonsmoke) # "population" sds -- calculated directly, not using the unbiased estimation built into R as "sd"
popsd(bwt.smoke)


# Ex 1 --------------------------------------------------------------------

# Set the seed at 1 and obtain a sample from the non-smoking mothers
# of size 25. Then, without resetting the seed, take a sample of the same size 
# from smoking mothers. Compute the t-statistic (call it tval). 
# Please make sure you input the absolute value of the t-statistic.

set.seed(1)
nonsmoke <- sample(bwt.nonsmoke, 25)
smoke <- sample(bwt.smoke, 25)

# difference in sample means
diff <- mean(nonsmoke) - mean(smoke)

# se of difference is the sum of sample se's
se <- sqrt( 
  var(nonsmoke)/25 + 
    var(smoke)/25 
)

# t statistic
tval <- abs(diff/se)
cat("t statistic for a sample of 25 is",tval,"\n")


# Ex 2 --------------------------------------------------------------------
cat(2*pnorm(-abs(tval)), "\n")

# Ex 4 --------------------------------------------------------------------

t.test(smoke,nonsmoke)

diff -  19.3258047
diff + -0.5141953



