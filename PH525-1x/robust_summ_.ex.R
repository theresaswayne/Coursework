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

# ex 2 ---------

# In exercise 1, we saw how sensitive the mean is to outliers. 
# Now let's see what happens when we use the median instead of the mean. 
# Compute the same ratio, but now using median instead of mean. 
# Specifically, what is the median weight of the day 4 chicks, 
# including the outlier chick, divided by the median of the weight of the 
# day 4 chicks without the outlier.


true_med_day4 <- median(day4_wt)

mod_median_day4 <- median(day4wt_mod)

cat("Addition of an outlier changes median from",
    true_med_day4, "to", mod_median_day4,
    ", a difference of", 100*mod_median_day4/true_med_day4,"%")

# ex 3 ---------------
# Now try the same thing with the sample standard deviation 
# (the sd function in R). Add a chick with weight 3000 grams 
# to the chick weights from day 4. How much does the standard deviation 
# change? What's the standard deviation with the outlier chick divided by 
# the standard deviation without the outlier chick?


true_sd_day4 <- sd(day4_wt)

mod_sd_day4 <- sd(day4wt_mod)

cat("Addition of an outlier changes SD from",
    true_sd_day4, "to", mod_sd_day4,
    ", a difference of", 100*mod_sd_day4/true_sd_day4,"%")

# ex 4 --------
# Compare the result above to the median absolute deviation in R, 
# which is calculated with the mad function. 
# Note that the mad is unaffected by the addition of a single outlier. 
# The mad function in R includes the scaling factor 1.4826, 
# such that mad and sd are very similar for a sample from a normal distribution. 
# What's the MAD with the outlier chick divided by the MAD without the outlier chick?


true_mad_day4 <- mad(day4_wt)

mod_mad_day4 <- mad(day4wt_mod)

cat("Addition of an outlier changes SD from",
    true_mad_day4, "to", mod_mad_day4,
    ", a difference of", 100*mod_mad_day4/true_mad_day4,"%")

# ex 5 -----------

# The Pearson correlation between x and y is given in R by cor(x,y). 
# The Spearman correlation is given by cor(x,y,method="spearman").

# Plot the weights of chicks from day 4 and day 21. 
# We can see that there is some general trend, with the
# lower weight chicks on day 4 having low weight again on day 21, 
# and likewise for the high weight chicks.
require(ggplot2)
qplot(chick$weight.4, chick$weight.21)

# Calculate the Pearson correlation of the weights of 
# chicks from day 4 and day 21. Now calculate how much the Pearson correlation changes 
# if we add a chick that weighs 3000 on day4 and 3000 on day 21. 
# Again, divide the Pearson correlation with the outlier chick 
# over the Pearson correlation computed without the outliers.

pearson_cor_4_21 <- cor(chick$weight.4, chick$weight.21)
day21_wt_mod <- c(chick$weight.21, 3000)
pearson_mod_4_21 <- cor(day4wt_mod, day21_wt_mod)

cat("Addition of an outlier changes Pearson correlation from",
    pearson_cor_4_21, "to", pearson_mod_4_21,
    ", a difference of", pearson_mod_4_21/pearson_cor_4_21,"fold")
