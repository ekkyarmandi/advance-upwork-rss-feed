# import the upworkrss object
from UpWorkRSS import UpWorkRSS
import time

# clear the terminal
import os
os.system("cls")

# run feed parser in loop
print("feed parser running..",end="")
while True:
    feed = UpWorkRSS("profile/scraping.json")
    feed.get()
    time.sleep(60)