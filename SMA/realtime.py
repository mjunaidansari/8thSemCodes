import csv
import time
import random
from datetime import datetime, timedelta

usernames = ['@nikefan', '@adidaslover', '@pumalife', '@sneakerhead', '@sporty123']
platforms = ['Twitter', 'Instagram']
hashtags = ['#Nike', '#Adidas', '#Puma']
devices = ['iPhone', 'Android', 'Web']
locations = [
    'New York, USA', 'Los Angeles, USA', 'London, UK',
    'Berlin, Germany', 'Mumbai, India', 'Sydney, Australia'
]
texts = [
    'Love the new drop from Nike!',
    'Adidas collab is 🔥🔥🔥',
    'Puma running shoes are awesome.',
    'Waiting for Nike Air Max restock!',
    'Just copped the latest Yeezys!',
    'Performance and style: Puma delivers!',
    'Adidas is losing its edge!',
    'Nike always wins in comfort.'
]

def generate_sentiment(text):
    if 'love' in text.lower() or '🔥' in text or 'awesome' in text or 'wins' in text:
        return 'Positive'
    elif 'losing' in text.lower():
        return 'Negative'
    else:
        return 'Neutral'

# CSV file path
file_path = 'social_media_stream.csv'

# Create header (keep data if already there)
with open(file_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([
        'Timestamp', 'Username', 'Platform', 'Tweet Text',
        'Hashtag', 'Likes', 'Retweets', 'Device Used',
        'Location', 'Sentiment'
    ])

# Function to get a random timestamp in the last 30 days
def get_random_past_timestamp():
    days_ago = random.randint(0, 29)
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    random_time = datetime.now() - timedelta(days=days_ago, hours=hours, minutes=minutes, seconds=seconds)
    return random_time.strftime('%Y-%m-%d %H:%M:%S')

# Keep appending new data
while True:
    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        timestamp = get_random_past_timestamp()
        user = random.choice(usernames)
        platform = random.choice(platforms)
        hashtag = random.choice(hashtags)
        text = random.choice(texts)
        device = random.choice(devices)
        location = random.choice(locations)
        sentiment = generate_sentiment(text)
        likes = random.randint(5, 200)
        retweets = random.randint(0, 50)

        writer.writerow([timestamp, user, platform, text, hashtag, likes, retweets, device, location, sentiment])
    
    print(f"[{timestamp}] Added simulated tweet")
    time.sleep(5)
