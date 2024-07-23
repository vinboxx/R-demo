library(nycflights13)
library(dplyr)

flights %>%
    select(year, month, day, dep_time, origin, dest, carrier, air_time, distance) %>%
    sample_n(10)
