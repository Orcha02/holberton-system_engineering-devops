#!/usr/bin/python3
""" Return list containing the titles of all hot articles """
from requests import request


def recurse(subreddit, hot_list=[], after=""):
    """ Query Reddit API to return all got articles """
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        top = response['data']['children']
        _after = response['data']['after']
        for item in top:
            hot_list.append(item['data']['title'])
        if _after is not None:
            recurse(subreddit, hot_list, _after)
        return hot_list
    except Exception:
        return None
