import praw

# Configure your Reddit API client
reddit = praw.Reddit(
    client_id='abcd1234',
    client_secret='efgh5678ijkl',
    user_agent='my_test_app/0.1 by /u/YOUR_USERNAME'
)

# Specify the subreddit
subreddit = reddit.subreddit('wallstreetbets')

# Fetch the latest posts
for submission in subreddit.new(limit=10):  # Change the limit as needed
    print(f"Title: {submission.title}")
    print(f"Score: {submission.score}")
    print(f"URL: {submission.url}")
    print(f"Comments: {submission.num_comments}")
    print(f"Created: {submission.created_utc}")
    print(f"Selftext: {submission.selftext}\n")