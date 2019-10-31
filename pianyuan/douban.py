# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import re
import MySQLdb
import json


def open_data(num):
    f = open("../pianyuan/data/" + str(num) + ".json")
    data = json.load(f)
    return data


class DoubanInfo:
    def get_douban_inf(self, url):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
        }
        req = requests.get(url, headers=headers)

        htmlpage = req.text

        douban_info = {}

        soup = BeautifulSoup(htmlpage, "html.parser")

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
            for childc2 in com_say:
                if childc2.string == "":
                    for childc3 in com_say_re:
                        douban_info["comment"] = childc3.string
                else:
                    douban_info["comment"] = childc2.string

        # 获取电影简介（以string形式输出）
        # Get the movie introduction
        intro_te = soup(name="span", attrs={"property": "v:summary"})
        for child in intro_te:
            douban_info["introduction"] = child.string

        # 获取主演名称
        # Get the actor
        star_te = soup(rel="v:starring")
        for child in star_te:
            douban_info["actor"] = child.string

        # 获取类型名称
        # Get the Type
        cate_te = soup(property="v:genre")
        for child in cate_te:
            douban_info["type"] = child.string

        # 获取上映日期
        # Get the date
        date_te = soup(property="v:initialReleaseDate")
        for child in date_te:
            douban_info["date"] = child.string

        # 获取其他相关信息
        compil_dire = r"导演<.*?><.*>(.+)</a>"
        compil_writ = r"编剧<.*?><.*>(.+)</a>"
        compil_loca = r"制片国家/地区:<.*?> (.+)<.*>"
        compil_lang = r"语言:<.*?> (.+)<.*>"
        compil_runt = r"片长:<.*?>.*<.*?>(.+)</.*>"
        compil_otna = r"又名:<.*?> (.+)<.*>"

        dire = re.findall(compil_dire, str(htmlpage))
        writ = re.findall(compil_writ, str(htmlpage))
        loca = re.findall(compil_loca, str(htmlpage))
        lang = re.findall(compil_lang, str(htmlpage))
        runt = re.findall(compil_runt, str(htmlpage))
        otna = re.findall(compil_otna, str(htmlpage))

        douban_info["director"] = dire
        douban_info["writer"] = writ
        douban_info["location"] = loca
        douban_info["language"] = lang
        douban_info["runtime"] = runt
        douban_info["othername"] = otna

        return douban_info


class DoubanDatabase:
    def SaveInfo(self, douban_info, num):
        account = {"host": "localhost", "username": "root", "password": "root"}
        db = MySQLdb.connect(
            account["host"],
            account["username"],
            account["password"],
            "sys",
            charset="utf8",
        )

        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS DOUBAN;")
        cursor.execute("USE DOUBAN;")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS INFORMATION"
            + "(id varchar(100) primary key not null,"
            + "actor varchar(200) not null,"
            + "writer varchar(100) not null,"
            + "location varchar(100) not null,"
            + "language varchar(100) not null,"
            + "runtime varchar(100) not null,"
            + "othername varchar(200) not null,"
            + "type varchar(100) not null,"
            + "date varchar(100) not null,"
            + "introduction varchar(1000) not null,"
            + "comment_name varchar(100) not null,"
            + "comment varchar(3000) not null)"
        )
        try:
            Command_insert = (
                "INSERT INTO INFORMATION VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            )
            cursor.execute(
                Command_insert,
                (
                    str(num),
                    str(douban_info["actor"]),
                    str(douban_info["writer"]),
                    str(douban_info["location"]),
                    str(douban_info["language"]),
                    str(douban_info["runtime"]),
                    str(douban_info["othername"]),
                    str(douban_info["type"]),
                    str(douban_info["date"]),
                    str(douban_info["introduction"]),
                    str(douban_info["comment_name"]),
                    str(douban_info["comment"]),
                ),
            )
        except KeyError:
            print(
                "this information has some problem ,therefore we just ignore it right now"
            )
        except MySQLdb._exceptions.OperationalError:
            print("fuck that!")

        db.commit()
        db.close()


class DoubanSpider:
    def spider(self, num_in):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
        }

        for temp in range(1, 684):
            temp_num = str(temp)
            num = num_in["_default"][temp_num]["id"]
            url = "https://movie.douban.com/subject/" + num + "/"

            Douban_info = DoubanInfo()
            Douban_database = DoubanDatabase()
            douban_info = Douban_info.get_douban_inf(url)
            Douban_database.SaveInfo(douban_info, num)
            print(str(temp) + " done")
            time.sleep(0.3)


if __name__ == "__main__":

    for i in range(5):
        dir_in = open_data(i + 1)
        spider = DoubanSpider()
        spider.spider(dir_in)
