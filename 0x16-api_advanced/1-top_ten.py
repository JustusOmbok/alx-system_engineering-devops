#!/usr/bin/python3
"""Module for top ten hot topics."""


def top_ten(subreddit):
    """ Retrieves total suscribers on reddit."""
    import requests

    headers = {'User-Agent': 'Ombok)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        print('None')
    else:
        [print(child["data"]["title"])
         for child in response.json()["data"]["children"]]
