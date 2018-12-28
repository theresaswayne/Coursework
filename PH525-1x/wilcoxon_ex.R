# wilcoxon_ex.R

# setup ----------

require(dplyr)
require(ggplot2)

data(ChickWeight)
head(ChickWeight)
overview <- qplot(x=ChickWeight$Time, y=ChickWeight$weight, colour=ChickWeight$Diet)
print(overview)

# get one animal per row

chick <- reshape(ChickWeight, idvar=c("Chick","Diet"), timevar="Time",
                   direction="wide")

# get rid of rows with any missing data

chick = na.omit(chick)

head(chick)

# ex 1-2 --------

# Save the weights of the chicks on day 4 from diet 1 as a vector x. 
# Save the weights of the chicks on day 4 from diet 4 as a vector y. 
# Perform a t-test comparing x and y (t.test(x,y))
# Then perform a Wilcoxon test of x and y (wilcox.test(x,y)). 
# A warning will appear that an exact p-value cannot be calculated with ties, so an approximation is used, which is fine for our purposes.

# Perform a t-test of x and y, after adding a single chick of weight 
# 200 grams to x (the diet 1 chicks). What is the p-value from this test?
# (t.test(x,y)$p.value)

# vectors for the different diets
x <- chick %>% filter(Diet == 1) %>% select(weight.4) %>% unlist
y <- chick %>% filter(Diet == 4) %>% select(weight.4) %>% unlist

orig_t <- t.test(x,y)$p.value
orig_w <- wilcox.test(x,y)$p.value

x_mod <- c(x,200)

mod_t <- t.test(x_mod,y)$p.value
mod_w <- wilcox.test(x_mod,y)$p.value

Test <- c("Original", "With Outlier")
t_test <- c(orig_t, mod_t) %>% signif(digits = 4)
wilcoxon <- c(orig_w, mod_w) %>% signif(digits = 4)

results <- rbind(Test, t_test, wilcoxon) 
print(results)

# ex 3 ----------
# We will now investigate a possible downside to the Wilcoxon-Mann-Whitney test # statistic. Using the following code to make three boxplots, showing the true # Diet 1 vs 4 weights, and then two altered versions: one with an additional 
# difference of 10 grams and one with an additional difference of 100 grams. 
# Use the x and y as defined above, NOT the ones with the added outlier.
 
require(rafalib)
mypar(1,3)
boxplot(x,y)
boxplot(x,y+10)
boxplot(x,y+100)

mypar() # reset

# What is the difference in t-test statistic (t.test(x,y)$statistic) 
# between adding 10 and adding 100 to all the values in the group 'y'? 
# Take the the t-test statistic with x and y+10 and subtract the t-test
# statistic with x and y+100. The value should be positive.

t0 <- t.test(x,y)

t10 <- t.test(x,y+10)

t100 <- t.test(x,y+100)

t_diff <- t.test(x,y+10)$statistic - t.test(x,y+100)$statistic

cat(t_diff)

# ex 4 ----------
# Examine the Wilcoxon test statistic for x and y+10 and for x and y+100. Because the Wilcoxon works on ranks, once the two groups show complete separation, that is all points from group 'y' are above all points from group 'x', the statistic will not change, regardless of how large the difference grows. Likewise, the p-value has a minimum value, regardless of how far apart the groups are. This means that the Wilcoxon test can be considered less powerful than the t-test in certain contexts. In fact, for small sample sizes, the p-value can't be very small, even when the difference is very large. What is the p-value if we compare c(1,2,3) to c(4,5,6) using a Wilcoxon test?

w0 <- wilcox.test(x,y)
w10 <- wilcox.test(x,y+10) # statistic goes to 0
w100 <- wilcox.test(x,y+100) # statistic still 0

cat(wilcox.test(c(1,2,3),c(4,5,6))$p.value) # p = 0.1

# ex 5 --------
# What is the p-value if we compare c(1,2,3) to c(400,500,600) using a Wilcoxon test?

cat(wilcox.test(c(1,2,3),c(400,500,600))$p.value) # p = 0.1
