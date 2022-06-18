from UpWorkRSS import UpWorkRSS
import time

while True:
    feed = UpWorkRSS("profile/scraping.json")
    feed.get()
    time.sleep(3)