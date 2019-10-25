import requests
import time

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}

url1 = "https://movie.douban.com/subject/30226522/"
url2  = "https://movie.douban.com/subject/26331839/"
url3 = "https://movie.douban.com/subject/34788059/"
url4 = "https://movie.douban.com/subject/34841044/"
req1 = requests.get(url1,headers = headers)
time.sleep(2)
req2 = requests.get(url1,headers = headers)
time.sleep(2)
req3 = requests.get(url1,headers = headers)
time.sleep(2)
req4 = requests.get(url1,headers = headers)
time.sleep(2)

print(req1)
print(req2)
print(req3)
print(req4)