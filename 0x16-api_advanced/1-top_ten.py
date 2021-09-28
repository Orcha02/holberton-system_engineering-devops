#!/usr/bin/python3
""" Return top ten titles """
import requests


def top_ten(subreddit):
    """ Query Reddit API to return first 10 hot posts """
    url = "https://api.reddit.com/r/{}/hot/".format(subreddit)
    headers = {"User-Agent": "Python3"}
    response = requests.request("GET", url, headers=headers,
                                params={'limit': 10}).json()
    try:
        for i in range(10):
            print(response['data']['children'][i]['data']['title'])
    except Exception:
        print(None)
