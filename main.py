from fetch_posts import fetch_latest_posts
from preprocessing import preprocess_text

def main():
    # Fetch latest posts from WallStreetBets
    posts = fetch_latest_posts('wallstreetbets', limit=10)

    # Preprocess the text of each post
    for post in posts:
        cleaned_text = preprocess_text(post['text'])
        print(f"Original: {post['text']}\nProcessed: {cleaned_text}\n")

if __name__ == '__main__':
    main()