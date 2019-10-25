from bs4 import BeautifulSoup
import requests
from tinydb import TinyDB,Query
from pianyuan import spider

def get_comment(url):
    res=[]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    comment_inf= soup.find_all(name="span",attrs={"class":"comment-info"})
    #for i in item:
       # comment={"userId":"null","isWatched":"null","rating":"null","voted":"null",time":"null","comment":"null"}
       # id = i.find(name="a",attr={"class":""})['href']
    ex = comment_inf[0]
    comment_user={"userId":"null","isWatched":"null","rating":"null"}
    user_url=ex.find(name="a")['href']
    user_url=str(user_url)
    id= user_url.replace("https://www.douban.com/people/","").replace("/","")
    comment_user['userId']=id
    print(id)


db =TinyDB("url.json")
def get_douban_link(end):
    for i in range(end):
        i = i+1
        page = spider.get_film_name_in_page(i)
        for j in page:
            j=j['url']
            douban= spider.get_douban_from_film(j)
            mo = {'id':"null"}
            mo['id']=douban
            db.insert(mo)


#page = spider.get_film_name_from_film_page(1)

get_douban_link(3)
