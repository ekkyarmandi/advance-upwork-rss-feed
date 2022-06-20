# import the upworkrss object
from UpWorkRSS import UpWorkRSS
import time

# clear the terminal
import os

def clear():
    os.system("cls")

# run feed parser in loop
clear()
while True:
    print("feed parser running")
    parser = UpWorkRSS("profile/scraping.json")
    parser.get()
    print("feed parser on pause")
    time.sleep(60)
    clear()