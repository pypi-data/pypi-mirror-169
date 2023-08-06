import urllib3
import random
import json

try:
    with open("./emojis.json", "r") as file:
        data = list(json.load(file).values())

except:
    http = urllib3.PoolManager()
    r = http.request(
        "GET",
        "https://gist.githubusercontent.com/cobanov/fbae0c689aba5fab6075ca3155fb8759/raw/a6bdbad133486f631f1696e7d694dc0c9b4641f4/emojis.json",
    )
    data = list(json.loads(r.data.decode("utf-8")).values())


def get():
    return random.choice(data)
