def parse_comics(comic_number):
    import requests

    url = f"http://xkcd.com/{comic_number}/info.0.json"

    resp = requests.get(url)
    return resp.json()
