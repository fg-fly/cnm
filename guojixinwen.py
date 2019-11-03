# coding=utf-8
import os
import sys

import requests
from bs4 import BeautifulSoup
import xlwt
import io


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def result2file(parent_dic, article_date, article_title):
    root_dic = '/Users/Tuoxian/PycharmProjects/demo/test'
    target_dic = root_dic + parent_dic + article_date
    is_exists = os.path.exists(target_dic)
    filename = target_dic + article_title
    if not is_exists:
        os.makedirs(target_dic)
    f = open(filename, 'w')
    return f


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


def gjxw():
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    url = 'http://world.people.com.cn/'
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    title_list = soup.select("ul.list_14b > li >a")
    # #article_date = soup.select("h4 > span.date")

    for i in range(len(title_list)):
        try:
            article_url = exchange_url(title_list[i].get("href"))
            html1 = request_douban(article_url)
            result_soup = BeautifulSoup(html1, 'lxml')
            result_title = result_soup.select("h1")
            artcle_content = result_soup.select("div.box_con > p")
            article_date = result_soup.select("div.box01 > div.fl")
            article_date_str = '/' + article_date[0].get_text()[5:11]
        except Exception:
            print '页面不存在'
        try:
            # print result_title[0].get_text()
            # print article_date[i].get_text()
            # print artcle_content[0].get_text()
            r2 = result_title[0].get_text().strip()
            article_title_str = '/' + r2 + '.txt'
            f = result2file('/网络聚焦/国际新闻', article_date_str, article_title_str)
            f.write(r2 + '\n')
            for k in range(len(artcle_content)):
                f.write("<div><span style='font-size:16px;margin-top:15px;line-height:25px;text-indent:30px;display:block'> " + artcle_content[k].get_text() + "</span></div>")
                f.write("<div>&nbsp;</div>")
            f.close()
            print '《' + r2 + '》' + article_date_str.replace('/','')
        except IndexError:
            print 'result_title is None!'

    # print (result_content)
    # for j in range(len(result_content)):
    #     print(result_content[j].get_text())
    #     f.write(result_content[j].get_text())
    # f.write('------------------------------------------')
    # f.write(datelist[i].get_text()+'\n')
    # f.close()
    print ('----------------------------------------------共获取:%d条新闻' % len(title_list))


gjxw()
