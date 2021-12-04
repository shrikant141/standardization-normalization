

install.packages("readr")

library(readr)

seed <- read_csv("F:/DataSets/Seeds_data.CSV")

View(seed)

seed <- seed[,]

# use scale function 
seedStand <- as.data.frame(scale(seed))

View(seedStand)


















