from bs4 import BeautifulSoup

import requests
import time
import re
import MySQLdb


url = "https://movie.douban.com/subject/3097278/"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
}
req = requests.get(url, headers=headers)
htmlpage = req.text
print("request Ok,and the req has back")
douban_info = {}

soup = BeautifulSoup(htmlpage, "html.parser")

comment_info = soup.find_all(class_="comment")
for child in comment_info:
    com_name_te = child.find_all(name="a", class_="")
    for childc1 in com_name_te:
        if childc1.string == "展开":
            time.sleep(0.1)
        else:
            print(childc1.string)

    com_say = child.find_all(name="span", class_="short")
    com_say_re = child.find_all(name="span", class_="hide-item full")
    for childc2 in com_say:
        if childc2.string == "":
            for childc3 in com_say_re:
                print(childc3.string)
                print("done")
        else:
            print(childc2.string)
            print("done")
