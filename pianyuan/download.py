import requests
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
