# null distributions exercise 1, 2, 3

x <- read_csv("extdata/femaleControlsPopulation.csv")
x <- unlist(x) # dataframe to vector, required for sample function

set.seed(1)
# n <- 1000 # ex 1
n <- 10000 # ex 2
# sampSize <- 5 # ex 1, 2
sampSize <- 50 # ex 3

sampMeans <- c() # empty vector

# get sample means
for (i in 1:n) { 
  samplemean <- mean(sample(x, sampSize))
  sampMeans <- c(sampMeans, samplemean)
}

# get population mean
popMean <- mean(x)

# get absolute differences
sampDiffs <- abs(sampMeans - popMean)

# fraction of differences exceeding a threshold
numExceeding <- length(which(sampDiffs>1))
total <- length(sampDiffs)
ans <- numExceeding/total
cat(ans)

# official answer
#set.seed(1)
#n <- 1000
#averages5 <- vector("numeric",n)
#for(i in 1:n){
#  X <- sample(x,5)
#  averages5[i] <- mean(X)
#}
#hist(averages5) ##take a look
#mean( abs( averages5 - mean(x) ) > 1) # converting vector to boolean and taking the average = percent True


