# coding=utf-8
import os
import sys

import requests
from bs4 import BeautifulSoup
import xlwt
import io


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def result2file(parent_dic, article_date, article_title):
    try:
        root_dic = '/Users/Tuoxian/PycharmProjects/demo/test'
        target_dic = root_dic + parent_dic + article_date
        is_exists = os.path.exists(target_dic)
        filename = target_dic + article_title
        if not is_exists:
            os.makedirs(target_dic)
        f = open(filename, 'w')
        return f
    except Exception:
        print 'cnm'
        return 'false'



def request_douban(url):
    try:
        response = requests.get(url)
        result = response.content.decode('gb2312', 'ignore')
        if response.status_code == 200:
            return result

    except requests.RequestException:
        return None


def exchange_url(url):
    http_target_str = 'http://world.people.com.cn'
    if (http_target_str in url):
        # print (title_list[i].get("href"))
        return url
    else:
        # test = http_target_str + title_list[i].get("href")
        _url = http_target_str + url
        return _url


def cjdt():
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    url = 'http://www.ce.cn/xwzx/gnsz/gdxw/'
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    title_list = soup.select("ul.con > li > span >a")
    article_date = soup.select("ul.con > li > span.f2")

    for i in range(len(title_list)):
        article_url = url + title_list[i].get("href")
        try:
            html1 = request_douban(article_url)
            result_soup = BeautifulSoup(html1, 'lxml')
            result_title = result_soup.select("h1")
            artcle_content = result_soup.select("div.TRS_Editor > p")
            article_date_str = article_date[i].get_text()[:6]
            _article_date_str = article_date_str.replace(' ', '日').replace('/', '月')
            article_date_str1 = '/' + _article_date_str
        except BaseException:
            print 'cnm 页面不存在'

        try:
            r2 = result_title[0].get_text()
            article_title_str = '/' + r2 + '.txt'
            f = result2file('/网络聚焦/财经新闻', article_date_str1, article_title_str)
            if(f=='false'):
                continue
            f.write(r2 + '\n')
            for k in range(len(artcle_content)):
                f.write("<div><span style='font-size:16px;margin-top:15px;line-height:25px;text-indent:30px;display:block'> " + artcle_content[k].get_text() + "</span></div>")
                f.write("<div>&nbsp;</div>")

            f.close()
            print '《' + r2 + '》' + article_date[i].get_text()[:6].replace('/', '-')

        except IndexError:
            print 'result_title is None!'
    print ('----------------------------------------------共获取:%d条新闻'%len(title_list))


cjdt()
