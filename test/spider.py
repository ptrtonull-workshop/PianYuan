from bs4 import BeautifulSoup
import requests
import bs4
from pianyuan import mysql
import time

mainWeb = "http://www.pianyuan.la"
mv_web = "http://pianyuan.la/mv?order=score"

acc = mysql.account

# get film page from main page's recommend
# page : page number of main recommend list
# number : the film position in page


# Question A: how can we get the recommend movies' name and match with its href?
def get_recommend(page, number):
    if page == 1:
        web = mainWeb
    else:
        web = mainWeb + "/" + "?p=" + str(page)
    response = requests.get(web)
    # else: page >100
    # 相应的保护措施（或者前端做限制）
    soup = BeautifulSoup(response.text, "html.parser")
    film = soup.find_all(
        name="a", attrs={"class": "ico ico_bt"}
    )  # lass located to find the target
    for i in film:
        i["href"] = mainWeb + i["href"]
    return film[number]["href"]


# get film resurces download inf
# url: res path, like http://pianyuan.la/r_ZZlK71840.html
# return :{'url':the download link from pianyuan.la,'bt':magnet,'subtitle':subtitle download link(not direct link)}
def get_film_download(url):
    res = {"url": "null", "bt": "null", "subtitle": "null"}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    film = soup.find_all(name="a", attrs={"class": "btn btn-danger btn-sm"})
    res["url"] = mainWeb + film[0]["href"]
    film = soup.find_all(name="a", attrs={"class": "btn btn-primary btn-sm"})
    res["bt"] = film[0]["href"]
    film = soup.find_all(name="a", attrs={"class": "btn btn-success btn-sm"})
    res["subtitle"] = film[0]["href"]
    return res


# get link inf from film page, such as douban link and more resurces
# url film link likes http://pianyuan.la/r_ZZWl71ug0.html
# return {'douban': 'https://movie.douban.com/subject/26683290/', 'more': 'http://pianyuan.la/m_DtmvWHuc0.html'}
def get_link(url):
    res = {"douban": "null", "more": "null"}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    douban = soup.find_all(name="a", attrs={"title": "豆瓣链接"})
    more = soup.find_all(name="a", attrs={"class": "text-danger"})
    res["douban"] = "https:" + douban[0]["href"]
    res["more"] = "http://pianyuan.la" + more[0]["href"]
    return res


# get all  screen type of a film
# url: film  link likes http://pianyuan.la/m_S8wXEc3c0.html
# return: ['4K', 'BluRay-1080P', 'BluRay-720P', 'Remux', 'TS/CAM/HC/DVDScr', 'BluRay-3D', '蓝光原盘', 'HDTV/HDRip/DVDRip']
def get_res_type(url):
    film_type = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    douban = soup.find_all(name="span", attrs={"class": "label label-warning"})
    for i in douban:
        film_type.append(i.string)
    return film_type


#  get a file name of a resurce
# url: a resurce likes : http://pianyuan.la/r_ZZlKD99b0.html
# return : The.Lion.King.2019.1080p.BluRay.x264-SPARKS
def get_inf(url):
    inf = {"name": "null", "number": "null", "douban": "null"}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    douban = soup.find_all(name="a", attrs={"title": "豆瓣链接", "target": "_blank"})
    douban = "https:" + douban[0]["href"]
    inf["douban"] = douban
    return soup.html.body.h1.string


# return  all resurces inf from a film link
# url : a film link likes http://pianyuan.la/m_DwozWH2c0.html
# return :
# [
#   {
#       'quality': 'BluRay-720P',
#       'movie_name': 'Zootopia.2016.720p.BluRay.AC3.x264.Greek-ETRG',
#       'url': 'http://pianyuan.la/r_ZZzxDe3g0.html',
#       'size': '1.21GB', 'flash_time': '07-15'
#   },
#   and so on
# ]
def get_more_film(url):
    page = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all(name="table", attrs={"class": "data"})  # 所有的资源列表，每一个代表一个清晰度
    for i in items:  # 取其中一个清晰度
        quatify = i.find(name="span", attrs={"class": "label label-warning"}).text
        films = i.find_all(name="tr", attrs={"class": "odd"})
        films += i.find_all(name="tr", attrs={"class": "even"})  # 取得所有子资源
        for j in films:  # 抽取其中一个子资源
            info = {}
            htxt = j.find(name="td", attrs={"class": "nobr"})  # 找到它带名字的超文本
            url = htxt.find(name="a", attrs={"class": "ico ico_bt"})  # 取得更细节的超文本信息
            if isinstance(url, bs4.element.Tag) is False:
                url = htxt.find(name="a", attrs={"class": "ico ico_ed2k"})
                if isinstance(url, bs4.element.Tag) is False:
                    url = htxt.find(name="a", attrs={"class": "ico"})  # 取得更细节的超文本信息
            name = url.string  # 取得名字
            url = "http://pianyuan.la" + url["href"]  # 取得链接 btn  btn-primary btn-sm
            size = j.find(name="td", attrs={"class": "nobr center"}).string  # 取得大小信息
            time = j.find(
                name="td", attrs={"class": "nobr lasttd center"}
            ).string  # 取得更新时间信息
            info["quality"] = quatify  # 收录此子资信息到字典
            info["movie_name"] = name
            info["url"] = url
            info["size"] = size
            info["flash_time"] = time
            page.append(info)
    return page  # 取得一个页面，也就是一部电影的所有资源


# get page link
# url : a film list page number likes  2
# return : next page link http://pianyuan.la/mv?order=score&p=2
def page_link(page):
    return "http://pianyuan.la/mv?order=score&p=" + str(page)


# get all resurces in one page
# page: page number, likes 1, it means http://pianyuan.la/mv?order=score&p=1
# return: [
#   [
#       {
#           'quality': 'BluRay-720P',
#           'movie_name': 'Zootopia.2016.720p.BluRay.AC3.x264.Greek-ETRG',
#           'url': 'http://pianyuan.la/r_ZZzxDe3g0.html',
#           'size': '1.21GB', 'flash_time': '07-15'
#       },
#       {
#
#       }
#   ],
#   [
#
#   ]
# ]
def get_list(page):
    url = page_link(page)  # 取得这一页的地址
    all_res_in_film = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all(
        name="div", attrs={"class": "col-sm-3 col-md-3 col-xs-4 col-lg-2 nopl"}
    )  # 取得一个页面的所有电影
    for item in items:
        film = item.find(name="a")
        film["href"] = "http://pianyuan.la" + film["href"]  # 取得一部电影的链接
        all_res_ = get_more_film(film["href"])  # 取得一部电影的所有资源到all_res里
        all_res_in_film.append(all_res_)
    return all_res_in_film


# get all res in a page and save to database
# page: the page number you want to get, likes 1, it means http://pianyuan.la/mv?order=score&p=1
# db: the database you create
def spider_ui(page, db):
    all_res_in_film = get_list(page)
    film_list_number = 0
    start = time.time()
    for x in range(0, 118, 3):  # 存一部电影的所有资源信息到数据库
        all_res = all_res_in_film[film_list_number]
        for r in all_res:  # 取得某一个资源
            mysql.add(r, db)
        num = x // 2
        if x == 107:
            process = "\r[%3d#NO.%3d]: |%-51s|本次运行时间:%3ds\n" % (
                page,
                x / 3 + 1,
                "|" * (num - 1),
                (time.time() - start),
            )
        else:
            process = "\r[%3d#NO.%3d]: |%-51s|本次运行时间:%3ds" % (
                page,
                x / 3 + 1,
                "|" * (num - 1),
                (time.time() - start),
            )
        print(process, end="", flush=True)
        if film_list_number == 35:
            return 0
        else:
            film_list_number = film_list_number + 1


# get the inf of page s to f to database db
# s: start page, likes 1
# f: final page , likes 2
# db: the database you created used mysql.create
def run(s, f, db):
    page = int(s)
    while page <= int(f):
        spider_ui(page, db)
        page = page + 1
