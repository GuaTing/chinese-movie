import urllib
import  urllib.request
import re
import requests
from lxml import etree
from selenium import webdriver
import time
driver = webdriver.PhantomJS(executable_path='../phantomjs')
def get_name(url):
    """
    获取電影名字
    :param url: 电影所在頁面地址
    :return:
    """
    name = ''
    time.sleep(1)
    for x in range(1,10):
        try:
            r = requests.get(url)
            page_source = r.content.decode("utf-8")
            html = etree.HTML(page_source)
            for i in html.xpath("//div[@class='ziliaoku']/div[@class='ziliaofr']/div[@class='cont']/h2"):
                movie_names = i.xpath("text()")
                for p_name in movie_names:
                    name = p_name
            print(p_name)
            return p_name
        except:
            return 'NULL'
def get_cover(url):
    """
    获取電影海報
    :param url: 电影所在頁面地址
    :return:
    """
    cover = ''
    time.sleep(1)
    r = requests.get(url)
    page_source = r.content.decode("utf-8")
    html = etree.HTML(page_source)
    for x in range(1,10):
        try:
            for i in html.xpath("//div[@class='ziliaoku']/div[@class='imgfl']/img"):
                pics = i.xpath("@src")
                print(pics)
                for imgPath in pics:
                    cover=imgPath
        except:
            return cover
    f = open(str(get_name(url0))+".jpg", 'wb')
    f.write((urllib.request.urlopen(cover)).read())
    print(cover)
    f.close()

r = open("../Movies")
line = r.readlines()
a = 0
names_list = []
movie_names = []
movie_ids = []
message_dict={}
for names_line in line:
    names_line = names_line.replace('\n','')
    movie_ids.append(names_line.split(':')[2])
for movie_id in movie_ids:
    # print(movie_id.replace('\tReleaseYear','').strip())
    url0 = 'http://www.cbooo.cn/m/'+movie_id.replace('\tReleaseYear','').strip()
    print(url0)
    get_cover(url0)