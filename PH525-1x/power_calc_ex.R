# wk 3 power calculations exercises

# load packages
require(here) # allows you to specify paths relative to the current wd
require(dplyr)
require(rafalib)

# load data  
babies <- read.table(here("extdata", "babies.txt"), header = TRUE)

# generate smoking and non-smoking vectors
bwt.nonsmoke <- filter(babies, smoke==0) %>% select(bwt) %>% unlist 
bwt.smoke <- filter(babies, smoke==1) %>% select(bwt) %>% unlist

# pretending this is the whole population
# find the "ground truth" difference in means
diff_means <- mean(bwt.nonsmoke)-mean(bwt.smoke)
popsd_ns <- popsd(bwt.nonsmoke)
popsd_s <- popsd(bwt.smoke)

cat("The difference in means is ",diff_means,"\n")
cat("Nonsmoking SD ",popsd_ns,"\n")
cat("Smoking SD ",popsd_s,"\n")

# ex 1
# Set the seed at 1 and take a random sample of N=5 measurements 
# from each of the smoking and nonsmoking datasets. 
# [Use] the t-test function to find the p-value.

N <- 5
set.seed(1)
samp_ns <- sample(bwt.nonsmoke, N)
samp_s <- sample(bwt.smoke, N)
ex1t <- t.test(samp_ns, samp_s)$p.value

# ex 2
# Set the seed at 1, then use the replicate function 
# to repeat the code used in the exercise above 10,000 times. 
# What proportion of the time do we reject at the 0.05 level?

reject <- function(N, alpha=0.05){
  samp_ns <- sample(bwt.nonsmoke, N)
  samp_s <- sample(bwt.smoke, N)
  ex2t <- t.test(samp_ns, samp_s)$p.value
  ex2t < alpha # last expression, therefore the value that is returned
}
reps <- 10000
set.seed(1)
rejections_of_null <- replicate(reps, reject(N))
reject_rate <- mean(rejections_of_null)

# ex 3
# Repeat the exercise above for sample sizes of 30, 60, 90 and 120. 
# Which of those four gives you power of about 80%?
set.seed(1)
Ns <- c(30,60,90,120)
powers_05 <- sapply(Ns, function(n) { 
  rejections_of_null <- replicate(reps, reject(n))
  mean(rejections_of_null) # store the power for each N 
  }) 

# ex 4
# Now require an alpha level of 0.01. 
set.seed(1)
powers_01 <- sapply(Ns, function(n) { 
  rejections_of_null <- replicate(reps, reject(n, alpha=0.01))
  mean(rejections_of_null) # store the power for each N 
}) 

