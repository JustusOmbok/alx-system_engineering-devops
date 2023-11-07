#!/usr/bin/python3
"""Module to retrieve hot topics by page."""


def recurse(subreddit, hot_list=[], after=None):
    """ Retrieves hot topics by page on reddit."""
    import requests

    headers = {'User-Agent': 'Ombok)'}
    url = (
        f"https://www.reddit.com/r/{subreddit}/hot.json"
        f"?limit=100&after={after}"
    )

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        return None

    data = response.json().get("data")
    children = data.get("children")

    for child in children:
        hot_list.append(child["data"]["title"])

    after = data.get("after")

    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
