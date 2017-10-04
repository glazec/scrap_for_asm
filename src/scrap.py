# -*- coding:UTF-8 -*-
import re
import requests
from sys import exit
from urllib.request import urlretrieve
import urllib.error
import os
import time
from shuaia import shuaia
from jiandan import jiandan
# from download import download
# from number_to_pre_url import number_to_pre_url
# from url_to_pre_url import url_to_pre_url
# from category import category
import sys
from bs4 import BeautifulSoup
# list_name = []
# list_href = []
# filename = ""
# pre_img_url = ""
#if __name__ == "__main__":

def category(page="1"):
    global list_name
    global list_href
    page = input("which page you want to get(default is 1):\n")
    url = "https://asmhentai.com/" + "pag" + "/" + page + "/"
    headers = {
        "User-Agent": "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"
    }
    req = requests.get(url=url, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    gf = BeautifulSoup(html, "lxml")
    names_url = gf.find_all(class_="lazy no_image")  # the url contain name
    src_url = gf.find_all(href=re.compile("/g/"))  # the url contain the picture url
    list_name = []
    list_href = []
    n = 1
    for i in names_url:
        name = i.get("alt")
        i = i.get("src")
        a = i.split("/")
        a.insert(3, "g")
        a.insert(2, "asmhentai.com")
        a.insert(1, "https:/")
        a.pop(8)
        a.pop(6)
        a.pop(4)
        a.pop(2)
        a.pop(0)
        b = "/".join(a)
        print(n, name)
        print(b + "/", "\n")
        list_name.append(name)
        list_href.append(b)
        n = n + 1

def number_to_pre_url():
    global filename
    global pre_img_url
    global list_name
    global list_href
    global pre_img_url
    filename = ""
    filename = list_name[int(torrent) - 1]
    for i in list_href:
        i = int(torrent) - 1
        pre_img_url = list_href[i]
        break

def url_to_pre_url():
    global filename
    global list_name
    global list_href
    global pre_img_url
    filename = ""
    pre_img_url = torrent
    print(list_href)
    print(torrent)
    t = torrent.split("/")
    t.pop[-1]
    t = "/".join(t)
    print(t)
    n = list_href.index(t)
    filename = list_name[i]


def download():
    global filename
    global pre_img_url
    print("downdload " + filename)
    while 'benzi' not in os.listdir():
        os.mkdir("benzi/")
    os.chdir('benzi/')
    os.makedirs(filename)
    os.chdir("..")
    img_url = ""
    for i in range(1, 100):
        pre_img_url = pre_img_url.split("/")
        # print(url_op)
        pre_img_url[2] = "images.asmhentai.com"
        pre_img_url[3] = "007"
        pre_img_url = "/".join(pre_img_url)
        img_url = str(pre_img_url) + "/" + str(i) + ".jpg"
        # print(img_url)
        print("downloding the " + str(i) + " picture")
        try:
            urlretrieve(url=img_url, filename="benzi/" + filename + "/" + str(i) + ".jpg")
        except urllib.error.HTTPError as e:
            print("finish download")
            break
        finally:
            time.sleep(1)

j = input("18x or 10x(18/10):\n")
if j == "10":
    k = input("shuai'ge or beauty?(s or b):\n")
    if k == "s":
        shuaia()
    else:
        jiandan()
else:
    while True:
        print("data is from www.asmhentai.com(recommended by michale)")
        decision = input("download or go to the category or any key to quit(d/c):\n")
        if decision == "d":
            torrent = input("please enter the number or the url(etc.https://asmhentai.com/g/197279/) to begin download:\n")
            if torrent.isnumeric():
                number_to_pre_url()
            else:
                url_to_pre_url()
            download()
        elif decision == "c":
            category()
        else:
            sys.exit(0)