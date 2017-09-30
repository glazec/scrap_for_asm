# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import re
import requests
from urllib.request import urlretrieve
import os
import time


if __name__ == "__main__":
    url = "https://asmhentai.com/"
    headers = {
        "User-Agent":"User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"
    }

    req = requests.get(url = url, headers = headers)
    req.encoding = 'utf-8'
    html = req.text
    gf = BeautifulSoup(html,"lxml")
    names_url=gf.find_all(class_="lazy no_image")
    src_url = gf.find_all(href=re.compile("/g/"))
    list_name = []
    list_href = []
    n = 1
    for i in names_url:
        name = i.get("alt")
        i = i.get("src")
        a = i.split("/")
        a.insert(3,"gallery")
        a.insert(2, "asmhentai.com")
        a.insert(1, "https:/")
        a.pop(8)
        a.pop(6)
        a.pop(4)
        a.pop(2)
        a.pop(0)
        b = "/".join(a)
        print(n,name)
        print(b,"\n")
        list_name.append(name)
        list_href.append(b)
        n += 1

    def download():
        dec = input("enter d to download;enter any key to quit:\n")
        if dec == "d":
            url_op = input("please enter the number:\n")
            filename = ""
            if url_op.isnumeric():
                filename = list_name[int(url_op)-1]

                for i,value in enumerate(list_href):
                    i = int(url_op)-1
                    url_op = value
                    break
            # else:
            #      filename = gf.find_all(url_op.split("/")[-1]).get('alt')
            print("downdload " + filename)
            # img_req = requests.get(url=url_op,headers = headers)
            # img_req.encoding = "utf-8"
            # img_html = img_req.text
            # img_bf1_ = BeautifulSoup(img_html,"lxml")
            # img
            while 'benzi' not in os.listdir():
                os.mkdir("benzi/")
            os.chdir('benzi/')
            os.makedirs(filename)
            os.chdir("..")
            img_url = ""
            for i in range(1,100):
                url_op = url_op.split("/")
                #print(url_op)
                url_op[2] = "images.asmhentai.com"
                url_op[3] = "007"
                url_op = "/".join(url_op)
                img_url = str(url_op) + "/"+str(i)+".jpg"
                #print(img_url)
                print("downloding the "+str(i)+" picture")
                urlretrieve(url=img_url, filename="benzi/"+filename+"/" +str(i)+".jpg")
            time.sleep(1)

        else:
            exit()
    while True:
        download()
        # https://images.asmhentai.com/007/197127/3.jpg
        # https://asmhentai.com/gallery/197128

 #     <a href="/g/197014/">
 # <img class="lazy no_image" alt="[Tottoko Mtarou (Mda Starou)] Strength and II (BLACK★ROCK SHOOTER)(English)" src="//images.asmhentai.com/007/197014/thumb.jpg">
 # </a>
