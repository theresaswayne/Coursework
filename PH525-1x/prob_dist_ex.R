# probability distributions exercises

library(gapminder) # does not check if it's installed...
library(dplyr)

# Create a vector 'x' of the life expectancies of each country for the year 1952. 

x <- filter(gapminder, year == 1952) %>% select(lifeExp) %>% unlist # year is int

# Plot a histogram of these life expectancies to see the spread of the different countries.

hist(x)

# In statistics, the empirical cumulative distribution function (or empirical cdf or empirical distribution function) 
# is the function F(a) for any a, which tells you the proportion of the values which are less than or equal to a.

# We can compute F in two ways: 
# the simplest way is to type mean(x <= a). 


# The second way, which is a bit more complex for beginners, is to use the ecdf() function. 
# This is a bit complicated because this is a function that doesn't return a value, but a function.

# Ex 1
# What is the proportion of countries in 1952 that have a life expectancy less than or equal to 40?

# cat(mean(x <= 40))

# answer from course: (not using dplyr)
# dat1952 = gapminder[ gapminder$year == 1952, ]
# x = dat1952$lifeExp

# Ex 2
# What is the proportion of countries in 1952 that have a life expectancy between 40 and 60 years?

# cat(mean(x <= 60) - mean(x <= 40))

# Ex 3
# Suppose we want to plot the proportions of countries 
# with life expectancy 'q' for a range of different years.

prop = function(q) { # proportion of countries with a mean <= q
  mean(x <= q)
}

# cat(prop(40))

# Now let's build a range of q's that we can apply the function to:

qs = seq(from=min(x), to=max(x), length=20) # equally spaced

# cat(qs)

# Now... use sapply() to apply the 'prop' function to each element of 'qs':

props = sapply(qs, prop)
   
plot(qs, props)

# Let's compare our homemade plot with the pre-built one in R:

plot(ecdf(x))

