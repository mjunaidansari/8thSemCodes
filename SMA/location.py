import pandas as pd
import random
import faker
from datetime import datetime, timedelta

# Initialize Faker for realistic names and locations
fake = faker.Faker()

# Define social media platforms
platforms = ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'TikTok', 'YouTube']

# Define post types
post_types = ['Image', 'Video', 'Text', 'Link', 'Story', 'Reel', 'Live']

# Define countries and some major cities
locations = [
    {'country': 'USA', 'city': 'New York'},
    {'country': 'USA', 'city': 'Los Angeles'},
    {'country': 'UK', 'city': 'London'},
    {'country': 'India', 'city': 'Mumbai'},
    {'country': 'India', 'city': 'Delhi'},
    {'country': 'Germany', 'city': 'Berlin'},
    {'country': 'France', 'city': 'Paris'},
    {'country': 'Japan', 'city': 'Tokyo'},
    {'country': 'Canada', 'city': 'Toronto'},
    {'country': 'Australia', 'city': 'Sydney'}
]

# Generate 1000 rows of social media analytics data
data = []
for _ in range(1000):
    location = random.choice(locations)
    data.append({
        'Post_ID': fake.uuid4(),
        'Platform': random.choice(platforms),
        'Post_Type': random.choice(post_types),
        'User': fake.user_name(),
        'Followers': random.randint(100, 1000000),
        'Likes': random.randint(0, 50000),
        'Shares': random.randint(0, 10000),
        'Comments': random.randint(0, 20000),
        'Impressions': random.randint(1000, 1000000),
        'Engagement_Rate': round(random.uniform(0.1, 10.0), 2),
        'Post_Date': (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d %H:%M:%S'),
        'Country': location['country'],
        'City': location['city'],
        'Latitude': round(random.uniform(-90, 90), 6),
        'Longitude': round(random.uniform(-180, 180), 6)
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('social_media_analytics.csv', index=False)

print("Social media analytics data generated and saved to 'social_media_analytics.csv'")
