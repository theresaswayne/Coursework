# PH525.1x
# first assesment, ex 3
# Use a for loop to determine the value of (the summation of i^2 over i=1 to 25)

ans <- 0
for(i in (1:25)) {
  ans <- ans + i^2
}
cat(ans)
