from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time
import re

def jiandan():
    print("data is from http://jandan.net/ooxx/page")
    list_url = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    img_req = requests.get(url="http://jandan.net/ooxx/page-4484#comments", headers=headers)
    img_req.encoding = 'utf-8'
    img_html = img_req.text
    img_bf = BeautifulSoup(img_html, 'lxml')
    total = img_bf.find_all(class_="title")
    page = img_bf.find_all(class_="title", id="comments")
    page = str(page)
    page = page.split(":")
    page = page[1].split("<")
    max_page = page[0]
    #print(total)
    s = int(input("which page do you want to start and start(1-"+max_page+")(the larger number means newer page):\n"))
    e = int(input("which page do you want to start and end(1-"+max_page+"4186):\n"))
    for num in range(s, e+1):
        if num == 1:
            url = 'http://jandan.net/ooxx'
        else:
            url = 'http://jandan.net/ooxx/page-%d#comments' % num
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        req = requests.get(url=url, headers=headers)
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        targets_url = bf.find_all(class_='view_img_link')

        for each in targets_url:
            list_url.append('http://' + each.get('href').replace('//', ''))
        print(list_url)
        n = 1
    for target_url in list_url:
        if target_url[-3:-1] == "jpg":
            filename = '' + str(time.localtime()) + '.jpg'
        else:
            filename = '' + str(time.localtime()) + '.gif'
        img_req = requests.get(url=target_url, headers=headers)
        img_req.encoding = 'utf-8'
        img_html = img_req.text
        img_bf = BeautifulSoup(img_html, 'lxml')
        # print("download",filename)
        print("download",n,"image")
        n = n + 1
        if 'beauty' not in os.listdir():
            os.makedirs('beauty')
        try:
            urlretrieve(url=target_url, filename='beauty/' + filename)
        except urllib.error.HTTPError as e:
            print("some errir occur.please delete the exised pictures and try again")
        except BaseException as e:
            urlretrieve(url=target_url, filename='beauty/' + filename)
        time.sleep(1)


    print('finish')
