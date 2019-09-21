from bs4 import BeautifulSoup
import requests
mainWeb = 'http://www.pianyuan.la'


# get film page from main page's recommend
# page : page number of main recommend list
# number : the film position in page
def get_recommend(page, number):
    if page == 1:
        web = mainWeb
    else:
        web = mainWeb + '/' + '?p=' + str(page)
    response = requests.get(web)
    soup = BeautifulSoup(response.text, 'html.parser')
    film = soup.find_all(name='a', attrs={'class': 'ico ico_bt'})
    for i in film:
        i['href'] = mainWeb + i['href']
    return film[number]['href']


def get_film_download(url, form):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if form == 'url':
        film = soup.find_all(name='a', attrs={'class': 'btn btn-danger btn-sm'})
        return mainWeb + film[0]['href']
    elif form == 'bt':
        film = soup.find_all(name='a', attrs={'class': 'btn btn-primary btn-sm'})
        return film[0]['href']
    elif form == 'subtitle':
        film = soup.find_all(name='a', attrs={'class': 'btn btn-success btn-sm'})
        return film[0]['href']
    else:
        return ''


print(get_film_download(get_recommend(1, 1), 'bt'))
