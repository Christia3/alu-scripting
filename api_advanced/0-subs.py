#!/usr/bin/python3
"""Queries the Reddit API to get the number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-script/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    return 0

