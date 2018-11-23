# conf_int_ex.R

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
# from smoking mothers. 

set.seed(1)
N <- 25
nonsmoke <- sample(bwt.nonsmoke, N)
smoke <- sample(bwt.smoke, N)

# difference in sample means
diff <- mean(nonsmoke) - mean(smoke)

# se of difference is the sum of sample se's
se <- sqrt( 
  var(nonsmoke)/N + 
    var(smoke)/N 
)

# t statistic
tval <- abs(diff/se)
cat("t statistic for a sample of 25 is",tval,"\n")


cat(2*pnorm(-abs(tval)), "\n")

# Ex 2 --------------------------------------------------------------------

t.test(smoke,nonsmoke)

clt_ci <- qnorm(0.995)*sqrt(sd(bwt.nonsmoke)^2/N + sd(bwt.smoke)^2/N)
cat("With CLT", clt_ci, "\n")
# supposed to be 12.0478

t_ci <- qt(0.995,48)*sqrt(sd(bwt.nonsmoke)^2/N + sd(bwt.smoke)^2/N ) #df = 2*N-2
cat("With t",t_ci,"\n")
# supposed to be 13.46762 

# Ex 4 --------------------------------------------------------------------

# Set the seed at 1 and take a random sample of N=5 measurements from 
# each of the smoking and nonsmoking datasets. 
# What is the p-value (use the t-test function)?

set.seed(1)
N <- 5
small_s <- sample(bwt.smoke, N)
small_ns <- sample(bwt.nonsmoke, N)
t.test(small_s, small_ns)$p.value

