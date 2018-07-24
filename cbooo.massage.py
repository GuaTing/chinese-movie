# -*- coding: utf-8 -*-
"""
created on 2018/7/20
author:Guo
target:获得中國票房網中电影的基本信息
finished on:2018
"""

import requests
from lxml import etree
from selenium import webdriver
import time
driver = webdriver.PhantomJS(executable_path='../phantomjs')
# #中文轉url編碼
# # print(url)
# r= requests.get(url)
# print(r.content.decode("utf-8"))

def get_name(url):
    """
    获取電影名字
    :param url: 电影所在頁面地址
    :return:
    """
    name = ''
    time.sleep(2)
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


def get_film(url):
    """
    获取類型
    :param url:电影所在頁面地址
    :return:
    """
    film=''
    time.sleep(2)
    for x in range(1,10):
        try:
            r = requests.get(url)
            page_source = r.content.decode("utf-8")
            html = etree.HTML(page_source)

            for i in html.xpath("//div[@class='ziliaoku']/div[@class='ziliaofr']/div[@class='cont']/p[3]"):
                movie_film = i.xpath("text()")
                for p_film in movie_film:
                    film=p_film
            print(film.replace('类型：',''))
            return film.replace('类型：','')
        except:
            return 'NULL'
def get_length(url):
    """
    获取片長
    :param url:电影所在頁面地址
    :return:
    """
    length=''
    time.sleep(2)
    for x in range(1,10):
        try:
            r = requests.get(url)
            page_source = r.content.decode("utf-8")
            html = etree.HTML(page_source)

            for i in html.xpath("//div[@class='ziliaoku']/div[@class='ziliaofr']/div[@class='cont']/p[4]"):
                movie_time = i.xpath("text()")
                for p_time in movie_time:
                    length = p_time
            print(length.replace('\r\n                    ','').replace('片长：','').strip())
            return length.replace('\r\n                    ','').replace('片长：','').strip()
        except:
            return 'NULL'
def get_data(url):
    """
    获取上映時間
    :param url:电影所在頁面地址
    :return:
    """
    data=''
    time.sleep(2)
    for x in range(1,10):
        try:
            r = requests.get(url)
            page_source = r.content.decode("utf-8")
            html = etree.HTML(page_source)

            for i in html.xpath("//div[@class='ziliaoku']/div[@class='ziliaofr']/div[@class='cont']/p[5]"):
                movie_data = i.xpath("text()")
                for p_data in movie_data:
                    data=p_data
            print(data.replace('\r\n                    ','').replace('上映时间：','').strip())
            return data.replace('\r\n                    ','').replace('上映时间：','').strip()
        except:
            return 'NULL'
def get_country(url):
    """
    获取國家及地區
    :param url:电影所在頁面地址
    :return:
    """
    country=''
    time.sleep(2)
    for x in range(1,10):
        try:
            r = requests.get(url)
            page_source = r.content.decode("utf-8")
            html = etree.HTML(page_source)

            for i in html.xpath("//div[@class='ziliaoku']/div[@class='ziliaofr']/div[@class='cont']/p[7]"):
                movie_country = i.xpath("text()")
                for p_country in movie_country:
                    country=p_country
            print(country.replace('\r\n                    ','').replace('国家及地区：','').strip())
            return country.replace('\r\n                    ','').replace('国家及地区：','').strip()
        except:
            return 'NULL'
def get_director(url):
    """
    获取導演
    :param url:电影所在頁面地址
    :return:
    """
    director=[]
    time.sleep(2)
    for x in range(1,10):
        try:
            r = requests.get(url)
            page_source = r.content.decode("utf-8")
            html = etree.HTML(page_source)

            for i in html.xpath("//div[@id='tabcont1']/dl[@class='dltext']/dd[1]/p/a"):
                movie_directors = i.xpath("text()")
                for p_director in movie_directors:
                    director.append(p_director.replace('\r\n                    ','').strip())
            print(director)
            return director
        except:
            return 'NULL'
def get_actor(url):
    """
    获取演員
    :param url:电影所在頁面地址
    :return:
    """
    actor=[]
    time.sleep(2)
    for x in range(1,10):
        try:
            r = requests.get(url)
            page_source = r.content.decode("utf-8")
            html = etree.HTML(page_source)

            for i in html.xpath("//div[@id='tabcont1']/dl[@class='dltext']/dd[2]/p/a"):
                movie_actor = i.xpath("text()")
                for p_actor in movie_actor:
                    actor.append(p_actor.replace('\r\n                    ','').strip())
            print(actor)
            return actor
        except:
            return 'NULL'
def get_company(url):
    """
    获取制作公司
    :param url:电影所在頁面地址
    :return:
    """
    company=[]
    time.sleep(2)
    for x in range(1,10):
        try:
            r = requests.get(url)
            page_source = r.content.decode("utf-8")
            html = etree.HTML(page_source)

            for i in html.xpath("//div[@id='tabcont1']/dl[@class='dltext']/dd[3]/p/a"):
                movie_company = i.xpath("text()")
                for p_company in movie_company:
                    company.append(p_company.replace('\r\n                    ','').strip())
            print(company)
            return company
        except:
            return 'NULL'
def get_distributor(url):
    """
    获取發行公司
    :param url:电影所在頁面地址
    :return:
    """
    distributor=[]
    time.sleep(2)
    for x in range(1,10):
        try:
            r = requests.get(url)
            page_source = r.content.decode("utf-8")
            html = etree.HTML(page_source)

            for i in html.xpath("//div[@id='tabcont1']/dl[@class='dltext']/dd[4]/p/a"):
                movie_distributor = i.xpath("text()")
                for p_distributor in movie_distributor:
                    distributor.append(p_distributor.replace('\r\n                    ','').strip())
            print(distributor)
            return distributor
        except:
            return 'NULL'

def get_total(url):
    """
    获取累計票房
    :param url:电影所在頁面地址
    :return:
    """
    total=''
    time.sleep(2)
    for x in range(1,10):
        try:
            r = requests.get(url)
            page_source = r.content.decode("utf-8")
            html = etree.HTML(page_source)

            for i in html.xpath("//div[@class='ziliaoku']/div[@class='ziliaofr']/div[@class='cont']/p/span[@class='m-span']"):
                movie_total = i.xpath("text()")[1]
                total = movie_total
            print(total)
            return total
        except:
            return 'NULL'

r = open("../Movies")
line = r.readlines()
a = 0
names_list = []
movie_names = []
movie_ids = []
for names_line in line:
    names_line = names_line.replace('\n','')
    movie_ids.append(names_line.split(':')[2])
for movie_id in movie_ids:
    # print(movie_id.replace('\tReleaseYear','').strip())
    url0 = 'http://www.cbooo.cn/m/'+movie_id.replace('\tReleaseYear','').strip()
    with open('../中國票房網/'+str(get_name(url0))+'.txt',"a+") as f:
        f.write('id:'+movie_id.replace('\tReleaseYear','').strip()+'\n'
            +'name:'+str(get_name(url0))+'\n'
            +'film:'+str(get_film(url0))+'\n'
            +'data:'+str(get_data(url0))+'\n'
            +'country'+str(get_country(url0))+'\n'
            +'total:'+str(get_total(url0))+'\n'
            +'length:'+str(get_length(url0))+'\n'
            +'distributor:'+str(get_distributor(url0))+'\n'
            +'company:'+str(get_company(url0))+'\n'
            +'director:'+str(get_director(url0))+'\n'
            +'actor:'+str(get_actor(url0))+'\n'
        )