install.packages("tidyverse")  # includes ggplot2, dplyr, readr, etc.

# Load necessary libraries
library(ggplot2)
library(dplyr)
library(readr)
library(lubridate)

# Read the dataset
df <- read_csv("social_media_visualization.csv")

# Convert date column to Date format
df$Date_Posted <- as.Date(df$Date_Posted)

# 1️⃣ Chart 1: Average Engagement Rate by Post Type
ggplot(df, aes(x = Post_Type, y = Engagement_Rate, fill = Post_Type)) +
  geom_boxplot() +
  labs(title = "Engagement Rate by Post Type",
       x = "Post Type",
       y = "Engagement Rate") +
  theme_minimal()

# 2️⃣ Chart 2: Total Likes per Hashtag (Top 10)
top_hashtags <- df %>%
  group_by(Hashtags) %>%
  summarise(Total_Likes = sum(Likes)) %>%
  arrange(desc(Total_Likes)) %>%
  slice_head(n = 10)

ggplot(top_hashtags, aes(x = reorder(Hashtags, Total_Likes), y = Total_Likes, fill = Hashtags)) +
  geom_col() +
  coord_flip() +
  labs(title = "Top 10 Hashtags by Total Likes",
       x = "Hashtag",
       y = "Total Likes") +
  theme_minimal()

# 3️⃣ Chart 3: Engagement Rate Trend Over Time
df_daily <- df %>%
  group_by(Date_Posted) %>%
  summarise(Avg_Engagement = mean(Engagement_Rate))

ggplot(df_daily, aes(x = Date_Posted, y = Avg_Engagement)) +
  geom_line(color = "steelblue") +
  geom_point() +
  labs(title = "Daily Average Engagement Rate Over Time",
       x = "Date Posted",
       y = "Average Engagement Rate") +
  theme_minimal()

# 4️⃣ Chart 4: Most Active Users (by number of posts)
top_users <- df %>%
  count(Username, sort = TRUE) %>%
  slice_head(n = 10)

ggplot(top_users, aes(x = reorder(Username, n), y = n, fill = Username)) +
  geom_col() +
  coord_flip() +
  labs(title = "Top 10 Most Active Users",
       x = "Username",
       y = "Number of Posts") +
  theme_minimal()
