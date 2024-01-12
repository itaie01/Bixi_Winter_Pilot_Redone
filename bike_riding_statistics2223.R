# Read in the 2022 ridership data
ridership_data_2022 <- read.csv("./Data/DonneesOuvertes2022.csv", header = TRUE, sep = ",")

# Display dataframe information
# summary(ridership_data_2022)
# head(ridership_data_2022)

# Get the most popular start stations
start_station_counts_22 <- table(ridership_data_2022$STARTSTATIONNAME)
start_station_counts_22 <- sort(start_station_counts_22, decreasing = TRUE)
# print(start_station_counts_22[1:10])

# Get the most popular end stations
end_station_counts_22 <- table(ridership_data_2022$ENDSTATIONNAME)
end_station_counts_22 <- sort(end_station_counts_22, decreasing = TRUE)
# print(end_station_counts_22[1:10])

# Read in the 2022 ridership data
ridership_data_2023 <- read.csv("./Data/DonneesOuvertes2023.csv", header = TRUE, sep = ",")

# Display dataframe information
# summary(ridership_data_2023)
# head(ridership_data_2023)

# Get the most popular start stations
start_station_counts_23 <- table(ridership_data_2023$STARTSTATIONNAME)
start_station_counts_23 <- sort(start_station_counts_23, decreasing = TRUE)
# print(start_station_counts_23[1:10])

# Get the most popular end stations
end_station_counts_23 <- table(ridership_data_2023$ENDSTATIONNAME)
end_station_counts_23 <- sort(end_station_counts_23, decreasing = TRUE)
# print(end_station_counts_23[1:10])

combined_data <- rbind(start_station_counts_22[1:150], start_station_counts_23[1:150], end_station_counts_22[1:150], end_station_counts_23[1:150])
