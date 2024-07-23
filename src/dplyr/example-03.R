library(nycflights13)
library(dplyr)

flights %>%
    filter(month == 1, day == 1) %>%
    mutate(date = paste(year, sprintf("%02d", month), sprintf("%02d", day), sep = "-")) %>%
    select(date, origin, dest, carrier, flight, tailnum) %>%
    head(10)
