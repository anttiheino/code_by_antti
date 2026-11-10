library(dplyr)

# Read the input table from SAS Data and AI Studio
df <- sd2df(R_input1)

# Process the data in R
result <- df %>%
  filter(Make == "Honda")

# Write to the connected output table
df2sd(result, R_output1)