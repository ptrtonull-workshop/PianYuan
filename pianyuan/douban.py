from bs4 import BeautifulSoup

# import requests
# import bs4
# import re


def get_douban_inf():
    # direct:导演  starring:演员  genre：
    # inf = {'direct':'null','starring':'null','genre':'null','loca':'null','lang':'null','time':'null'}
    # response = requests.get(url)
    htmlfile = open(
        "C:/Users/97607/Documents/GitHub/Python/PianYuan/html/mainWeb.html",
        "r",
        encoding="utf8",
    )
    htmlpage = htmlfile.read()

    soup = BeautifulSoup(htmlpage, "html.parser")
    # mov_info = soup(id="info")[0]

    # for循环里面的东西不能重复

    # 评论

    comment_info = soup.find_all(class_="comment")
    for child in comment_info:
        com_name_te = child.find_all(name="a", class_="")
        for childc1 in com_name_te:
            if childc1.string == "展开":
                print()
            else:
                print(childc1.string)

        com_say = child.find_all(name="span", class_="short")
        com_say_re = child.find_all(name="span", class_="hide-item full")
        for childc2 in com_say_re:
            if childc2.string == "":
                for childc3 in com_say:
                    print(childc3.string)
            else:
                print(childc2.string)

    # 简介
    """
    comment_info = soup.find_all(class_="comment")
    for child in comment_info:
        com_name_te = child.find_all(name='a',class_="")
        for child1 in com_name_te:
            print(child1.string)

        com = child.find_all(class_="short")
        if(child.find_all(class_="short"))


        for child2 in com:
            print(child2.string)

        print("")

    """


"""

    #获取电影简介（以string形式输出）
    intro_te = soup(name='span',attrs={"property":"v:summary"})
    for child in intro_te:
        print(child.string)

    #获取主演名称
    star_te = soup(rel="v:starring")
    for child in star_te:
        print(child.string)

    #获取类型名称
    cate_te = soup(property="v:genre")
    for child in cate_te:
        print(child.string)

    #获取上映日期
    date_te = soup(property="v:initialReleaseDate")
    for child in date_te:
        print(child.string)



    #获取其他相关信息
    compil_dire = r'导演<.*?><.*>(.+)</a>'
    compil_writ = r'编剧<.*?><.*>(.+)</a>'
    compil_loca = r'制片国家/地区:<.*?> (.+)<.*>'
    compil_lang = r'语言:<.*?> (.+)<.*>'
    compil_runt = r'片长:<.*?>.*<.*?>(.+)</.*>'
    compil_otna = r'又名:<.*?> (.+)<.*>'


    dire = re.findall(compil_dire,str(mov_info))
    writ = re.findall(compil_writ,str(mov_info))
    loca = re.findall(compil_loca,str(mov_info))
    lang = re.findall(compil_lang,str(mov_info))
    runt = re.findall(compil_runt,str(mov_info))
    otna = re.findall(compil_otna,str(mov_info))


    print(dire)
    print(writ)
    print(loca)
    print(lang)
    print(date)
    print(runt)
    print(otna)
"""


# 主程序入口，最后封装请直接删除
if __name__ == "__main__":
    get_douban_inf()
