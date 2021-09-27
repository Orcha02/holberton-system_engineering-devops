#!/usr/bin/python3
""" Return number of subs """
import requests


def number_of_subscribers(subreddit):
    """ Query Reddit API to return number of subs """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "Python3"}
    response = requests.request("GET", url, headers=headers).json()
    try:
        subscribers = response['data']['subscribers']
        return subscribers
        # OR-> return response.json().get('data').get('subscribers')
    except Exception:
        return 0
