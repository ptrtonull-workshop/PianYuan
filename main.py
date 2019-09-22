from bs4 import BeautifulSoup
import requests
mainWeb = 'http://www.pianyuan.la'


# get film page from main page's recommend
# page : page number of main recommend list
# number : the film position in page


#Question A: how can we get the recommend movies' name and match with its href?
def get_recommend(page, number):
    if page == 1:
        web = mainWeb
    else:
        web = mainWeb + '/' + '?p=' + str(page)
    response = requests.get(web)
    #else: page >100
        #相应的保护措施（或者前端做限制）
    
    soup = BeautifulSoup(response.text, 'html.parser')
    film = soup.find_all(name='a', attrs={'class': 'ico ico_bt'})   #class located to find the target
    for i in film:
        i['href'] = mainWeb + i['href']
    return film[number]['href']

#SUGGESTION:
#This is a film_download_link, not the download function.
#Can we change this function's name?    
def get_film_download(url):
    res = {'url': 'null', 'bt': 'null', 'subtitle': 'null'}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    film = soup.find_all(name='a', attrs={'class': 'btn btn-danger btn-sm'})
    res['url'] = mainWeb + film[0]['href']
    film = soup.find_all(name='a', attrs={'class': 'btn btn-primary btn-sm'})
    res['bt'] = film[0]['href']
    film = soup.find_all(name='a', attrs={'class': 'btn btn-success btn-sm'})
    res['subtitle'] = film[0]['href']
    return res


def get_link(url):
    res = {'douban': 'null', 'more': 'null'}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    douban = soup.find_all(name='a', attrs={'title': '豆瓣链接'})
    more = soup.find_all(name='a', attrs={'class': 'text-danger'})
    res['douban'] = 'https:' + douban[0]['href']
    res['more'] = 'http://pianyuan.la' + more[0]['href']
    return res


def get_res_type(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    douban = soup.find_all(name='span', attrs={'class': 'label label-warning'})
    print(douban[0].string)


def get_inf(url):
    inf = {'name': 'null', 'number': 'null', 'douban': 'null'}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    douban = soup.find_all(name='a', attrs={'title': '豆瓣链接', 'target': '_blank'})
    douban = 'https:' + douban[0]['href']
    inf['douban'] = douban
    print(soup.html.body.h1.string)


def get_more_film(url):
    info = {"quality": "null", "name": "null", "url": "null", "size": "null", "time": "null"}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all(name='table', attrs={'class': 'data'})   # 所有的资源列表，每一个代表一个清晰度
    for i in items:                                                # 取其中一个清晰度
        quatify = i.find(name='span', attrs={'class': 'label label-warning'}).text  # 取得清晰度的值
        films = i.find_all(name='tr', attrs={'class': 'odd'})
        films += i.find_all(name='tr', attrs={'class': 'even'})   # 取得所有子资源
        for j in films:                                           # 抽取其中一个子资源
            htxt = j.find(name='td', attrs={'class': 'nobr'})  # 找到它带名字的超文本
            url = htxt.find(name='a', attrs={'class': 'ico ico_bt'})   # 取得更细节的超文本信息
            name = url.string  # 取得名字
            url = 'http://pianyuan.la' + url['href']   # 取得链接
            size = j.find(name='td', attrs={'class': 'nobr center'}).string   # 取得大小信息
            time = j.find(name='td', attrs={'class': 'nobr lasttd center'}).string   # 取得更新时间信息
            info["quality"] = quatify    # 收录此子资信息到字典
            info["name"] = name
            info["url"] = url
            info["size"] = size
            info["time"] = time
    return info


get_more_film('http://pianyuan.la/m_S8oNccec0.html')
