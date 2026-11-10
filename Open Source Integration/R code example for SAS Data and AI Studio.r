# Load tidyverse for data manipulation and visualization
library(tidyverse)

# Select the vehicle manufacturer
VMake <- "Honda"

# Convert the SAS table into an R data frame
carsdf <- sd2df("sashelp.cars")

# Filter the data to Honda vehicles
mycars <- carsdf %>%
  filter(Make == VMake)

# Calculate the average MSRP, ignoring missing values
avg_msrp <- round(mean(mycars$MSRP, na.rm = TRUE))

# Write the filtered R data frame back to SAS
df2sd(mycars, "work.filtered_cars")

# Create a histogram with color representing highway MPG
p <- ggplot(mycars, aes(x = MPG_Highway, fill = after_stat(x))) +
  geom_histogram(
    binwidth = 5,
    color = "white",
    linewidth = 0.7
  ) +
  scale_fill_gradient(
    low = "#FFB703",
    high = "#0072B2"
  ) +
  labs(
    title = "Distribution of Highway MPG for Honda Cars",
    subtitle = "Higher fuel economy shown in blue",
    x = "Highway MPG",
    y = "Number of Cars",
    fill = "MPG"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    plot.subtitle = element_text(size = 11),
    legend.position = "right"
  )

# Display the R visualization in SAS results
rplot(p)
# Display the first rows of the filtered data
show(head(mycars))