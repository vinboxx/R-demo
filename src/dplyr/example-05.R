library(nycflights13)
library(dplyr)

flights %>% select(carrier, dep_delay) %>%
  filter(!is.na(dep_delay)) %>%
  group_by(carrier) %>%
  summarise(avg_dep_delay = mean(dep_delay, na.rm = TRUE)) %>%
  arrange(avg_dep_delay) %>%
  head(10) %>%
  inner_join(airlines, by = c("carrier" = "carrier")) %>%
  select(carrier, name, avg_dep_delay)
