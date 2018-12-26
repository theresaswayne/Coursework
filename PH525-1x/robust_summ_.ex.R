# robust_summ_ex.R

# setup ----------
# The MAD (median absolute deviation) is 
# a robust estimate of the standard deviation.

# 1.4826 * median(abs(Xi - median(X)))
# 
# We are going to explore the properties of robust statistics. 
# We will use one of the datasets included in R, which contains 
# weight of chicks in grams as they grow from day 0 to day 21. 
# This dataset also splits up the chicks by different protein diets, 
# which are coded from 1 to 4. 

# We use this dataset to also show an important operation in R 
# (not related to robust summaries): reshape.
# 

data(ChickWeight)

# To begin, take a look at the weights of all observations over time 
# and color the points to represent the Diet:

head(ChickWeight)
plot(ChickWeight$Time, ChickWeight$weight, col=ChickWeight$Diet)

# First, notice that the rows here represent time points rather than individuals. To facilitate the comparison of weights at different time points and across the different chicks, we will reshape the data so that each row is a chick. In R we can do this with the reshape function:

chick = reshape(ChickWeight, idvar=c("Chick","Diet"), timevar="Time",
                   direction="wide")

# The meaning of this line is: reshape the data from _long_ to _wide_, 
# where the columns Chick and Diet are the ID's 
# and the column Time indicates different observations for each ID. 
# Now examine the head of this dataset:
# 
head(chick)

# We also want to remove any chicks that have missing observations 
# at any time points (NA for "not available"). 
# The following line of code identifies these rows and then removes them:
chick = na.omit(chick)

# ex 1 --------
# Focus on the chick weights on day 4 
# (check the column names of 'chick' and note the numbers). 
# How much does the average of chick weights at day 4 increase 
# if we add an outlier measurement of 3000 grams? 
#   Specifically, what is the average weight of the day 4 chicks, 
# including the outlier chick, divided by the average of the weight 
# of the day 4 chicks without the outlier. 
# Hint: use c to add a number to a vector.

day4_wt <- chick$weight.4

true_mean_day4 <- mean(day4_wt)

day4wt_mod <- c(day4_wt, 3000)

mod_mean_day4 <- mean(day4wt_mod)

cat("Addition of an outlier changes mean from",
    true_mean_day4, "to", mod_mean_day4,
    ", a difference of", 100*mod_mean_day4/true_mean_day4,"%")
