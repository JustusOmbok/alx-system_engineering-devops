#!/usr/bin/python3
"""Module that prints occurrence of topics."""


def count_words(subreddit, word_list=[], after=None, counts={}):
    """ Retrieves hot topics occurrencesby on reddit."""
    import requests
    if counts is None:
        counts = {}

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
        title = child["data"]["title"].lower()
        for word in word_list:
            counts[word] = counts.get(word, 0) + title.count(word.lower())

    after = data.get("after")

    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = (
            sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        )
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")
