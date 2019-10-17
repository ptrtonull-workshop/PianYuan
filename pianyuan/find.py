from pianyuan.spider import *
import emoji


# find film as key value
# key: keyword likes 你
# action: print all film name and url which appeared in page one
def show_search(key):
    re = get_search(key)
    for i in re:
        name = get_film_name_from_film_page(i)
        print(name + i)
