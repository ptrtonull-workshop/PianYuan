from bs4 import BeautifulSoup

import requests
import time
import re
import MySQLdb



test={
    "_default": {
        "1": {
            "id": "3097278"
        },
        "2": {
            "id": "4167113"
        },
        "3": {
            "id": "24751811"
        },
        "4": {
            "id": "6075345"
        },
        "5": {
            "id": "26874505"
        },
        "6": {
            "id": "1840299"
        },
        "7": {
            "id": "26577541"
        },
        "8": {
            "id": "24298647"
        },
        "9": {
            "id": "3425812"
        },
        "10": {
            "id": "1875218"
        },
        "11": {
            "id": "10573342"
        },
        "12": {
            "id": "7052699"
        },
        "13": {
            "id": "1292052"
        },
        "14": {
            "id": "1782004"
        },
        "15": {
            "id": "5159040"
        },
        "16": {
            "id": "33400747"
        },
        "17": {
            "id": "26933690"
        },
        "18": {
            "id": "26236632"
        },
        "19": {
            "id": "25787888"
        },
        "20": {
            "id": "4186795"
        },
        "21": {
            "id": "25754522"
        },
        "22": {
            "id": "24882562"
        },
        "23": {
            "id": "2363526"
        },
        "24": {
            "id": "3761048"
        },
        "25": {
            "id": "1777888"
        },
        "26": {
            "id": "4144377"
        },
        "27": {
            "id": "3156157"
        },
        "28": {
            "id": "1296141"
        },
        "29": {
            "id": "5402497"
        },
        "30": {
            "id": "20413573"
        },
        "31": {
            "id": "1308892"
        },
        "32": {
            "id": "25779043"
        },
        "33": {
            "id": "30253080"
        },
        "34": {
            "id": "30349240"
        },
        "35": {
            "id": "26946426"
        },
        "36": {
            "id": "26354587"
        },
        "37": {
            "id": "5156658"
        },
        "38": {
            "id": "25662329"
        },
        "39": {
            "id": "26265962"
        },
        "40": {
            "id": "24857754"
        },
        "41": {
            "id": "26264388"
        },
        "42": {
            "id": "24333957"
        },
        "43": {
            "id": "1292063"
        },
        "44": {
            "id": "1292720"
        },
        "45": {
            "id": "2264077"
        },
        "46": {
            "id": "1291546"
        },
        "47": {
            "id": "1295124"
        },
        "48": {
            "id": "1295644"
        },
        "49": {
            "id": "26691373"
        },
        "50": {
            "id": "30353874"
        },
        "51": {
            "id": "30402564"
        },
        "52": {
            "id": "30157353"
        },
        "53": {
            "id": "25788649"
        },
        "54": {
            "id": "26291600"
        },
        "55": {
            "id": "26827751"
        },
        "56": {
            "id": "1297777"
        },
        "57": {
            "id": "25920885"
        },
        "58": {
            "id": "26276373"
        },
        "59": {
            "id": "2984627"
        },
        "60": {
            "id": "1419362"
        },
        "61": {
            "id": "3713664"
        },
        "62": {
            "id": "11615927"
        },
        "63": {
            "id": "3694952"
        },
        "64": {
            "id": "1291831"
        },
        "65": {
            "id": "1300285"
        },
        "66": {
            "id": "1293182"
        },
        "67": {
            "id": "2127874"
        },
        "68": {
            "id": "2131459"
        },
        "69": {
            "id": "3442220"
        },
        "70": {
            "id": "1303408"
        },
        "71": {
            "id": "6129689"
        },
        "72": {
            "id": "27010768"
        },
        "73": {
            "id": "1845707"
        },
        "74": {
            "id": "25860925"
        },
        "75": {
            "id": "30167509"
        },
        "76": {
            "id": "1840488"
        },
        "77": {
            "id": "2134469"
        },
        "78": {
            "id": "26276498"
        },
        "79": {
            "id": "26764928"
        },
        "80": {
            "id": "4705150"
        },
        "81": {
            "id": "27101775"
        },
        "82": {
            "id": "26951951"
        },
        "83": {
            "id": "6846495"
        },
        "84": {
            "id": "2352020"
        },
        "85": {
            "id": "2139020"
        },
        "86": {
            "id": "3636923"
        },
        "87": {
            "id": "25702328"
        },
        "88": {
            "id": "25986298"
        },
        "89": {
            "id": "5240678"
        },
        "90": {
            "id": "26766869"
        },
        "91": {
            "id": "26718518"
        },
        "92": {
            "id": "26707074"
        },
        "93": {
            "id": "5327268"
        },
        "94": {
            "id": "1296181"
        },
        "95": {
            "id": "26582012"
        },
        "96": {
            "id": "1473562"
        },
        "97": {
            "id": "2979243"
        },
        "98": {
            "id": "2342568"
        },
        "99": {
            "id": "3095617"
        },
        "100": {
            "id": "3734350"
        },
        "101": {
            "id": "1304920"
        },
        "102": {
            "id": "1291561"
        },
        "103": {
            "id": "1291857"
        },
        "104": {
            "id": "1292571"
        },
        "105": {
            "id": "1419673"
        },
        "106": {
            "id": "2029049"
        },
        "107": {
            "id": "3718778"
        },
        "108": {
            "id": "1291549"
        }
    }
}


class DoubanInfo:
    def get_douban_inf(self,url):

        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}
        req = requests.get(url,headers = headers)
        print(req)
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




class DoubanDatabase:

    def SaveInfo(self,douban_info):
        account = {"host": "localhost", "username": "root", "password": "root"}
        db = MySQLdb.connect(
        account["host"], account["username"], account["password"], "sys", charset="utf8"
        )
        
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS DOUBAN;")
        cursor.execute("USE DOUBAN;")
        cursor.execute("CREATE TABLE IF NOT EXISTS INFORMATION"+
                        "(id varchar(50) primary key not null,"+
                        "actor varchar(200) not null,"+
                        "location varchar(50) not null,"+
                        "language varchar(50) not null,"+
                        "runtime varchar(50) not null,"+
                        "othername varchar(200) not null,"+
                        "type varchar(50) not null,"+
                        "date varchar(50) not null,"+
                        "introduction varchar(1000) not null,"+
                        "comment_name varchar(50) not null,"+
                        "comment varchar(3000) not null)"
                        )
        try:
            Command_insert = "INSERT INTO INFORMATION VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(Command_insert,
                (
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
                    str(douban_info['comment'])
                )
            )
        except KeyError:
            print("this information has some problem ,therefore we just ignore it right now")
        except MySQLdb._exceptions.OperationalError:
            print("fuck that!")

        
        db.commit()
        db.close()

class DoubanSpider:
    def spider(self):

        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}

        for a in range (1,30):
            temp = str(a)
            num = test['_default'][temp]['id']
            url = "https://movie.douban.com/subject/"+num+"/"
            Douban_info = DoubanInfo()
            Douban_database = DoubanDatabase()
            douban_info = Douban_info.get_douban_inf(url)
            Douban_database.SaveInfo(douban_info)
            print(str(a)+" done")
            time.sleep(0.1)
        
        




if __name__ == "__main__":
    spider = DoubanSpider()
    spider.spider()