library(nycflights13)
library(dplyr)

flights %>%
    select(origin, dest, carrier, flight) %>%
    filter(grepl("^J", origin))

