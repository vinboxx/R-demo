load("src/data/flights.rda")
library(dplyr)

flights %>%
    select(year, month, day, dep_time, origin, dest, carrier, air_time, distance) %>%
    head(10)
