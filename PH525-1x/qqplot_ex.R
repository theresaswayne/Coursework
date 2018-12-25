# qqplot_ex.R

# setup
require(here)
require(rafalib)
require(dplyr)

# load data

load(here("extdata","skew.RData")) # no name -- automatically becomes "dat"
dim(dat) # You should have a 1000 x 9 dimensional matrix

# Using QQ-plots, compare the distribution of 
# each column of the matrix to a normal. 
# That is, use qqnorm() on each column. 
# To accomplish this quickly... set up a grid for 3x3=9 plots. 
# ("mfrow" means we want a multifigure grid filled in row-by-row. 
# Another choice is mfcol.)

par(mfrow = c(3,3))

# ... loop through the columns, and display one qqnorm() plot at a time.

for (i in 1:9) {
  qqnorm(dat[,i], main = paste0("Column ", i)) # insert variable in title
  }

# Identify the two columns which are skewed. 

# Examine each of these two columns using a histogram. 
# Note which column has "positive skew", in other words the histogram 
# shows a long tail to the right (toward larger values). 
# Note which column has "negative skew", that is, a long tail to the left 
# (toward smaller values). 

# Note that positive skew looks like an up-shaping curve 
# in a qqnorm() plot, while negative skew looks like a down-shaping curve.

# use the following line to reset your graph to just show one at a time:
par(mfrow=c(1,1))

hist(dat[,4], main = "Column 4") # positive

hist(dat[,9], main = "Column 9") 
