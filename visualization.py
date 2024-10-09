import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from textblob import TextBlob
import praw

# Fetch Reddit posts (assuming you have already fetched them)
# This is just a rough outline. Make sure to adapt it to your project.

posts = [
    {"title": "Post 1", "selftext": "I love stocks", "created_utc": 1630000000},
    {"title": "Post 2", "selftext": "This stock sucks", "created_utc": 1630100000},
    # More posts...
]

# Convert posts into a DataFrame
df = pd.DataFrame(posts)

# Convert timestamp to datetime
df['created_datetime'] = df['created_utc'].apply(lambda x: datetime.utcfromtimestamp(x))

# Sentiment analysis using TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns a value between -1 (negative) to 1 (positive)

# Apply sentiment analysis
df['sentiment'] = df['selftext'].apply(get_sentiment)

# Plotting sentiment over time
plt.figure(figsize=(10, 6))
plt.plot(df['created_datetime'], df['sentiment'], marker='o')
plt.title('Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Sentiment Polarity')
plt.grid(True)
plt.show()