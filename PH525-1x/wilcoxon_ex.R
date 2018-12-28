# wilcoxon_ex.R

# setup ----------

require(dplyr)
require(ggplot2)

data(ChickWeight)
head(ChickWeight)
qplot(x=ChickWeight$Time, y=ChickWeight$weight, colour=ChickWeight$Diet)

# get one animal per row

chick <- reshape(ChickWeight, idvar=c("Chick","Diet"), timevar="Time",
                   direction="wide")

# get rid of rows with any missing data

chick = na.omit(chick)

head(chick)

# ex 1 --------

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
