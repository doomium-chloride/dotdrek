import urllib.request, json


def fetch_json(link):
    with urllib.request.urlopen(link) as url:
        return json.load(url)
