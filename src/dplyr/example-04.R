load("src/data/flights.rda")
load("src/data/airlines.rda")
library(dplyr)

flights %>%
    select(carrier) %>%
    inner_join(airlines, by = c("carrier" = "carrier")) %>%
    distinct(name) %>%
    arrange(name)
