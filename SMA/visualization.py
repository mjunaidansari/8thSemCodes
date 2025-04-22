import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter

# Load the dataset
df = pd.read_csv("social_media_visualization.csv")

# Convert 'Date_Posted' to datetime format
df['Date_Posted'] = pd.to_datetime(df['Date_Posted'])

# Set the style of the plots
sns.set(style="whitegrid")

# 1️⃣ Chart 1: Average Engagement Rate by Post Type
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="Post_Type", y="Engagement_Rate", palette="Set2")
plt.title("Engagement Rate by Post Type")
plt.xlabel("Post Type")
plt.ylabel("Engagement Rate")
plt.show()

# 2️⃣ Chart 2: Total Likes per Hashtag (Top 10)
top_hashtags = df.groupby("Hashtags")["Likes"].sum().reset_index()
top_hashtags = top_hashtags.sort_values(by="Likes", ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_hashtags, x="Likes", y="Hashtags", palette="Blues_d")
plt.title("Top 10 Hashtags by Total Likes")
plt.xlabel("Total Likes")
plt.ylabel("Hashtags")
plt.show()

# 3️⃣ Chart 3: Engagement Rate Trend Over Time
df_daily = df.groupby("Date_Posted")["Engagement_Rate"].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_daily, x="Date_Posted", y="Engagement_Rate", marker="o", color="steelblue")
plt.title("Daily Average Engagement Rate Over Time")
plt.xlabel("Date Posted")
plt.ylabel("Average Engagement Rate")
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
plt.show()

# 4️⃣ Chart 4: Most Active Users (by number of posts)
top_users = df['Username'].value_counts().reset_index()
top_users.columns = ['Username', 'Number_of_Posts']
top_users = top_users.head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_users, x="Number_of_Posts", y="Username", palette="Set2")
plt.title("Top 10 Most Active Users")
plt.xlabel("Number of Posts")
plt.ylabel("Username")
plt.show()
