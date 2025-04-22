import pandas as pd

df = pd.read_csv("social_media_data.csv")

print("Before Cleaning:\n", df.head(20))

df["Followers"].fillna(df["Followers"].median(), inplace=True)
df["Likes"].fillna(df["Likes"].mean(), inplace=True)
df["Engagement_Rate"].fillna(df["Engagement_Rate"].mean(), inplace=True)
df.drop_duplicates(inplace=True)

df["Date_Posted"] = pd.to_datetime(df["Date_Posted"], errors="coerce", dayfirst=True)
print("\nAfter Cleaning:\n", df.head(20))
