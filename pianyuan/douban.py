from bs4 import BeautifulSoup

import requests
import time
import re



def get_douban_html(url):

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}
    req = requests.get(url,headers = headers)

    return req.text



def get_douban_inf(html):

    douban_info = {}

    htmlfile = open(
        html,
        "r",
        encoding="utf8",
    )
    htmlpage = htmlfile.read()

    soup = BeautifulSoup(htmlpage, "html.parser")

    soup.find_all

    comment_info = soup.find_all(class_="comment")
    for child in comment_info:
        com_name_te = child.find_all(name="a", class_="")
        for childc1 in com_name_te:
            if childc1.string == "展开":
                time.sleep(0.1)
            else:
                douban_info["comment_name"] = childc1.string

        com_say = child.find_all(name="span", class_="short")
        com_say_re = child.find_all(name="span", class_="hide-item full")
        for childc2 in com_say_re:
            if childc2.string == "":
                for childc3 in com_say:
                    douban_info["comment"] = childc3.string
            else:
                    douban_info["comment"] = childc2.string

    #获取电影简介（以string形式输出）
    #Get the movie introduction
    intro_te = soup(name='span',attrs={"property":"v:summary"})
    for child in intro_te:
        douban_info["introduction"] = child.string

    #获取主演名称
    #Get the actor
    star_te = soup(rel="v:starring")
    for child in star_te:
        douban_info["actor"] = child.string

    #获取类型名称
    #Get the Type
    cate_te = soup(property="v:genre")
    for child in cate_te:
        douban_info["type"] = child.string

    #获取上映日期
    #Get the date
    date_te = soup(property="v:initialReleaseDate")
    for child in date_te:
        douban_info["date"] = child.string



    #获取其他相关信息
    compil_dire = r'导演<.*?><.*>(.+)</a>'
    compil_writ = r'编剧<.*?><.*>(.+)</a>'
    compil_loca = r'制片国家/地区:<.*?> (.+)<.*>'
    compil_lang = r'语言:<.*?> (.+)<.*>'
    compil_runt = r'片长:<.*?>.*<.*?>(.+)</.*>'
    compil_otna = r'又名:<.*?> (.+)<.*>'


    dire = re.findall(compil_dire,str(htmlpage))
    writ = re.findall(compil_writ,str(htmlpage))
    loca = re.findall(compil_loca,str(htmlpage))
    lang = re.findall(compil_lang,str(htmlpage))
    runt = re.findall(compil_runt,str(htmlpage))
    otna = re.findall(compil_otna,str(htmlpage))


    douban_info["director"] = dire
    douban_info["writer"] = writ
    douban_info["location"] = loca
    douban_info["language"] = lang
    douban_info["runtime"] = runt
    douban_info["othername"] =otna


    return douban_info