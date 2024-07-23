load("src/data/flights.rda")
library(dplyr)

flights %>%
    select(origin, dest, carrier, flight) %>%
    filter(grepl("^J", origin))

