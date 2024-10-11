import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from textblob import TextBlob
from fetch_posts import fetch_latest_posts  # Import your fetch_latest_posts function
from matplotlib.dates import DateFormatter

# Fetch latest Reddit posts
posts = fetch_latest_posts(subreddit_name="wallstreetbets", limit=100)  # Adjust parameters as needed

# Convert posts into a DataFrame
df = pd.DataFrame(posts)

# Convert timestamp to datetime
df['created_datetime'] = pd.to_datetime(df['created'], unit='s')

# Sentiment analysis using TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns a value between -1 (negative) to 1 (positive)

# Apply sentiment analysis
df['sentiment'] = df['selftext'].apply(get_sentiment)

# Plotting sentiment over time
plt.figure(figsize=(10, 6))
plt.plot(df['created_datetime'], df['sentiment'], marker='o')

# Date formatting
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M'))

plt.title('Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Sentiment Polarity')
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.show()