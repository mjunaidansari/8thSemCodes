import pandas as pd
import random

# Function to generate random dates
def random_date():
    return pd.to_datetime(f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}")

# Creating a dataset with clean values
data = []
usernames = [f"user{i}" for i in range(1, 31)]  # 30 unique users for variation
post_types = ["Image", "Video", "Reel", "Story"]
hashtags = ["#fun", "#travel", "#music", "#fitness", "#food", "#gaming", "#fashion",
            "#sports", "#nature", "#art", "#tech", "#books", "#education", "#movies",
            "#health", "#pets", "#DIY", "#quotes", "#history"]

for i in range(1, 101):  # Generating 100 rows
    user = random.choice(usernames)
    data.append([
        100 + i,  # Post_ID
        user,  # Username
        random.randint(1000, 10000),  # Followers
        random.choice(post_types),  # Post_Type
        random.randint(100, 1000),  # Likes
        random.randint(5, 50),  # Comments
        random.randint(1, 20),  # Shares
        random.choice(hashtags),  # Hashtags
        random_date(),  # Date_Posted
        round(random.uniform(1.0, 5.0), 2)  # Engagement_Rate
    ])

# Creating DataFrame
df = pd.DataFrame(data, columns=["Post_ID", "Username", "Followers", "Post_Type", "Likes", 
                                 "Comments", "Shares", "Hashtags", "Date_Posted", "Engagement_Rate"])

# Save dataset as CSV for visualization
df.to_csv("social_media_visualization.csv", index=False)

# Display first 10 rows
print(df.head(10))
