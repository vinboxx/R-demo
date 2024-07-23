library(nycflights13)
library(dplyr)

flights %>%
    select(carrier) %>%
    inner_join(airlines, by = c("carrier" = "carrier")) %>%
    distinct(name) %>%
    arrange(name)
