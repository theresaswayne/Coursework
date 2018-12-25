# assoc_tests_ex.R

# setup
require(here)
require(rafalib)
require(dplyr)

# load data
d = read.csv(here("extdata","assoctest.csv"))

# Ex 1 ------------
# Compute the Chi-square test for the association of genotype with case/control status 
# (using the table() function and the chisq.test() function). 
# Examine the table to see if it looks enriched for association by eye. 
# What is the X-squared statistic?

assoc_test_tab <- table(d) 
cat(assoc_test_tab) # looks like more cases in the allele = 1 category

assoctest_chi <- chisq.test(assoc_test_tab) # X2 is done on the table, not the raw data
cat(assoctest_chi$statistic)

# Ex 2 ------------
# Compute the Fisher's exact test ( fisher.test() ) 
# for the same table. What is the p-value?

assoc_test_fish <- fisher.test(assoc_test_tab)
cat(assoc_test_fish$p.value)