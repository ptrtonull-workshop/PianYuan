import requests, os
from pianyuan import spider
import time

# download torrent from direct download url, save as name.torrent
# url: download link likes https://pianyuan.la/dlbt/WlpXbDcxdWcwfDg5M2U3ZjJhODVhMDE1ZTVhZDY2YmJmMXwxNTcxMTUwNzQ3fDMwMGFjOTU0
# path: save path likes ./
# name: filename likes yourname
def download_from_url(url, path, name):
    f = requests.get(url)
    with open(path + "/" + name + ".torrent", "wb") as code:
        code.write(f.content)


# download torrent from film resurces url
# url : film res link likes:http://pianyuan.la/r_ZZWl71ug0.html
# path: loacl save path likes: ./
# name : filename likes yourname
def download(url, path, name):
    if spider.get_film_download(url) != False:
        down = spider.get_film_download(url)
        down = down["url"]
        download_from_url(down, path, name)


# download all bt in different folders in one page
# page: page number : likes 1, stands for http://pianyuan.la/mv?order=score&p=2
# path : save path : likes "./bt"
# action: save all res in page page to their folder in "./bt"
def download_all_in_page(page, path):
    film_name = ""
    film_res_all = []
    film_all = spider.get_film_name_in_page(page)
    for i in film_all:
        film_name = i["name"]
        film_name = film_name.replace("/", " ").replace(":", " ")
        paths = path
        paths += "/" + film_name
        mkdir(paths)
        film_res_all = spider.get_more_film(i["url"])
        for j in film_res_all:
            if spider.get_res_num(
                spider.get_film_url_from_res(j["url"])
            ) != get_file_num(
                paths
            ):  # if the film not download compeletly
                download(j["url"], paths, j["movie_name"])  # download bt
            # print(film_name+spider.get_film_url_from_res(j['url']))
            else:
                print("already done!")
                break
        print("The film:" + film_name + " done!")


# create a folder
# path: the folder you want to create, likes "./bt" or "c:/bt"
# return: if successfully created, true
#         if not successfully created , false
def mkdir(path):
    path = path.strip()  # 去除首位空格
    path = path.rstrip("\\")  # 去除尾部 \ 符号
    isExists = os.path.exists(path)  # 判断路径是否存在
    if not isExists:  # 判断结果
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        # print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + ' 目录已存在')
        return False


def get_all_film_bt(start, path):
    s1 = time.time()
    i = start - 1
    while i < int(spider.get_page_num()):
        s = time.time()
        download_all_in_page(i + 1, path)
        e = time.time()
        print("++++++++page " + str(i + 1) + " done!" + str(e - s) + "s has passed!")
        i += 1
    e1 = time.time()
    print("all bt save in" + path + " time is " + str(e1 - s1) + "s")


# get loacl bt film num
# pathname: the folder's path, likes D:\File\vscode\pianyuan\bt\今日比赛 (1964)
# return the bt num of this page, likes 1
def get_file_num(pathname):
    import os

    path = pathname
    count = 0
    for file in os.listdir(path):  # file 表示的是文件名
        count = count + 1
    return count
