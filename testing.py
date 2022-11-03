import requests
import random


def get_free_proxies():
    proxies = open('proxy.txt', 'r').read().splitlines()
    return proxies


def get_session(proxies):
    session = requests.Session()
    proxy = random.choice(proxies)
    session.proxies = {'http': proxy, 'https': proxy}
    return session


for i in range(25):
    s = get_session(get_free_proxies())
    try:
        print("Request page with IP:", s.get(
            "http://icanhazip.com", timeout=1.5).text.strip()
        )
    except Exception as e:
        continue
