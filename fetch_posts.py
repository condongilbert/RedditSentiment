import praw

# Configure your Reddit API client
reddit = praw.Reddit(
    client_id='JwBBjyCT4vfSbyBDgcW6VQ',
    client_secret='kMoJdCbBK7spWd58JHGYGyfNbZcsfA',
    user_agent='SentApp/0.1 by /u/NoBookkeeper3492'
)

# Function to fetch latest posts
def fetch_latest_posts(subreddit_name, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    # Fetch the latest posts
    for submission in subreddit.new(limit=limit):  # Change the limit as needed
        post_data = {
            "title": submission.title,
            "score": submission.score,
            "url": submission.url,
            "comments": submission.num_comments,
            "created": submission.created_utc,
            "selftext": submission.selftext
        }
        posts.append(post_data)
    
    return posts

# Example usage:
if __name__ == '__main__':
    latest_posts = fetch_latest_posts('wallstreetbets', limit=10)
    for post in latest_posts:
        print(f"Title: {post['title']}")
        print(f"Score: {post['score']}")
        print(f"URL: {post['url']}")
        print(f"Comments: {post['comments']}")
        print(f"Created: {post['created']}")
        print(f"Selftext: {post['selftext']}\n")