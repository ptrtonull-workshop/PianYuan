from bs4 import BeautifulSoup
import requests
from tinydb import TinyDB, Query
from pianyuan import spider
import threading


def get_comment(url):
    res = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    comment_inf = soup.find_all(name="span", attrs={"class": "comment-info"})
    # for i in item:
    # comment={"userId":"null","isWatched":"null","rating":"null","voted":"null",time":"null","comment":"null"}
    # id = i.find(name="a",attr={"class":""})['href']
    ex = comment_inf[0]
    comment_user = {"userId": "null", "isWatched": "null", "rating": "null"}
    user_url = ex.find(name="a")["href"]
    user_url = str(user_url)
    id = user_url.replace("https://www.douban.com/people/", "").replace("/", "")
    comment_user["userId"] = id
    print(id)



# download douban id from page
# start : start page number
# end   : end page number
# name  : file name
def get_douban_link(start, end, name):
    db = TinyDB("./data/" + name)
    for i in range(start, end):
        i = i + 1
        page = spider.get_film_name_in_page(i)
        for j in page:
            j = j["url"]
            douban = spider.get_douban_from_film(j)
            mo = {"id": "null"}
            mo["id"] = douban
            db.insert(mo)


for i in range(6):
    get_douban_link(i * 20 + 1, (i + 1) * 20, str(i + 1) + ".json")
