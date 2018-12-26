# boxplot_scatterplot_ex.R

# boxplot exercises ---------

# The InsectSprays data set measures the counts of insects 
# in agricultural experimental units treated with different insecticides. 
# This dataset is included in R, and you can examine it by typing:
  
head(InsectSprays)

# Try out two equivalent ways of drawing boxplots in R, 
# using the InsectSprays dataset. Below is pseudocode, 
# which you should modify to work with the InsectSprays dataset.

# 1) using split:
#   
# split divides the data in the vector x into the groups defined by f. 
# The replacement forms replace values corresponding to such a division. 
# unsplit reverses the effect of split.
#   boxplot(split(values, factor))

# boxes extend from 1st to 3rd quartiles
# whiskers default to 1.5 * the interquartile range
boxplot(split(InsectSprays$count, InsectSprays$spray), main = "standard form")

# 2) using a formula:
#   
#   boxplot(values ~ factor)

boxplot(InsectSprays$count ~ InsectSprays$spray, main = "formula")

require(dplyr)
require(UsingR)
data(nym.2002, package = "UsingR")
head(nym.2002)

# Use boxplots and histograms to compare 
# the finishing times of males and females.
boxplot(split(nym.2002$time, nym.2002$gender), main="Finish Time By Gender")

men <- filter(nym.2002, gender == "Male")
women <- filter(nym.2002, gender == "Female")

hist(men$time, breaks = 100)
hist(women$time, breaks = 100)

# scatterplot exercises --------

# For males, what is the Pearson correlation between age and time to finish?
require(ggplot2)
qplot(men$age, men$time)
qplot(women$age, women$time)

cor(men$age, men$time, method = "pearson")

# For females, what is the Pearson correlation between age and time to finish?
cor(women$age, women$time, method = "pearson")

#  Look at scatterplots and boxplots of times stratified by age groups 
# (20-25, 25-30, etc..).

# stratify
men_ages <- split(men$time,round(men$age/5)*5)  # split in 5-year increments
boxplot(men_ages, main = "Men's finishing time by age")

women_ages <- split(women$time,round(women$age/5)*5)  # split in 5-year increments
boxplot(women_ages, main = "Women's finishing time by age")

