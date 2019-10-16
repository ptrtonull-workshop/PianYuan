import requests, os
from pianyuan import spider

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
        film_name = film_name.replace("/", " and ").replace(":", " ")
        paths = path
        paths += "/" + film_name
        mkdir(paths)
        film_res_all = spider.get_more_film(i["url"])
        for j in film_res_all:
            download(j["url"], paths, j["movie_name"])


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


def get_all_film_bt(path):
    for i in range(int(spider.get_page_num())):
        download_all_in_page(i + 1, path)
    print("all bt save in" + path)
