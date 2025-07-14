# reddit_scraper.py

import praw
import os
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def extract_username_from_url(url):
    """
    Extracts the Reddit username from a profile URL.
    Example: https://www.reddit.com/user/kojied/ -> kojied
    """
    return url.strip('/').split('/')[-1]

def fetch_user_activity(username, post_limit=50, comment_limit=50):
    """
    Fetches recent posts and comments from a Reddit user.
    Returns two lists: posts, comments
    """
    try:
        redditor = reddit.redditor(username)

        posts = []
        for submission in redditor.submissions.new(limit=post_limit):
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext,
                "subreddit": str(submission.subreddit),
                "url": submission.url,
                "permalink": "https://www.reddit.com" + submission.permalink
            })

        comments = []
        for comment in redditor.comments.new(limit=comment_limit):
            comments.append({
                "body": comment.body,
                "subreddit": str(comment.subreddit),
                "permalink": "https://www.reddit.com" + comment.permalink
            })

        return posts, comments

    except Exception as e:
        print(f"Error fetching data for user {username}: {e}")
        return [], []
