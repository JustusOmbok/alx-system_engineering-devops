#!/usr/bin/python3
"""Module for subscribers number."""


def number_of_subscribers(subreddit):
    """ Retrieves total suscribers on reddit."""
    import requests

    headers = {'User-Agent': 'Ombok)'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
