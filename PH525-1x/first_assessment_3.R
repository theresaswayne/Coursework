# uses a for loop to find the sum of squared integers from 1-25

total <- 0
print(paste("total is",total))

for (i in 1:25){
  total <- total + i^2
  print(i)
  }
print(total)

