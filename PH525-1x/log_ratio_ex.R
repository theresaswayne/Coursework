# log_ratio_ex.R
# Symmetry of Log Ratios Exercises

# setup

require(dplyr)
require(UsingR)
data(nym.2002, package = "UsingR")

# Create a vector time of the sorted times:

time = sort(nym.2002$time)

# ex 1 ----------
# What is the fastest time divided [by] the median time?

fastest_time <- time[1] # indices start at 1 in R
# or min(time) if it's not sorted!

median_time <- median(time)

cat("Fastest time divided by median time is", fastest_time/median_time)

# What is the slowest time divided [by] the median time?
cat("Slowest / median is",max(time)/median(time))

# Compare the following two plots.
# 
# 1) A plot of the ratio of times to the median time, with horizontal lines at 
# twice as fast as the median time, and twice as slow as the median time.
# 
plot(time/median(time), ylim=c(1/4,4))
abline(h=c(1/2,1,2))
# 
# 2) A plot of the log2 ratio of times to the median time. The horizontal 
# lines indicate the same as above: twice as fast and twice as slow.
 
plot(log2(time/median(time)),ylim=c(-2,2))
abline(h=-1:1) # -1, 0, 1

# Note that the lines are equally spaced in Figure #2.
