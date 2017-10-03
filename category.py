import re
import requests
from sys import exit
from urllib.request import urlretrieve
import urllib.error
import os
import time
import sys
from bs4 import BeautifulSoup


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
    print(list_name)