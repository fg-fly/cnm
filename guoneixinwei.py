# coding=utf-8
import os

import requests
from bs4 import BeautifulSoup
import xlwt
import sys
import io


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def result2file(parent_dic, article_date, article_title):
    root_dic = '/Users/plantkon/Documents/WorkSpacePy/hdqw/test'
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
        result = response.content.decode('utf-8')
        if response.status_code == 200:
            return result

    except requests.RequestException:
        return None


def exchange_url(url):
    http_target_str = 'http://www.gov.cn'
    if (http_target_str in url):
        # print (title_list[i].get("href"))
        return url
    else:
        # test = http_target_str + title_list[i].get("href")
        _url = http_target_str + url
        return _url


def gnxw():
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    url = 'http://www.gov.cn/xinwen/yaowen.htm'
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    title_list = soup.select("h4 > a")
    article_date = soup.select("h4 > span.date")

    for i in range(len(title_list)):
        article_url = exchange_url(title_list[i].get("href"))
        html1 = request_douban(article_url)
        result_soup = BeautifulSoup(html1, 'lxml')
        result_title = result_soup.select("h1")
        artcle_content = result_soup.select("div.pages_content > p")
        try:
            # print result_title[0].get_text()
            # print article_date[i].get_text()
            # print artcle_content[0].get_text()
            r1 = article_date[i].get_text().strip()
            r2 = result_title[0].get_text().strip()
            article_date_str = '/' + r1
            article_title_str = '/' + r2 + '.txt'
            f = result2file('/网络聚焦/国内新闻', article_date_str, article_title_str)
            f.write(r2 + '\n')
            for k in range(len(artcle_content)):
                f.write("<div><span style='font-size:16px;margin-top:15px;line-height:25px;text-indent:30px;display:block'> " + artcle_content[k].get_text() + "</span></div>")
                f.write("<div>&nbsp;</div>")

            f.close()
            print '《' + r2 + '》' + article_date_str.replace('/', '')
        except IndexError:
            print 'result_title is None!'
        # for k in range(len(result_title)):
        #     print result_title[k].get_text()
    #     result_content = result_soup.select("div.TRS_Editor ")
    #     f = open('data.txt', 'a')
    #     f.write(result_title[0].get_text() + '\n')

    # print (result_title[0].get_text())

    # print (result_content)
    # for j in range(len(result_content)):
    #     print(result_content[j].get_text())
    #     f.write(result_content[j].get_text())
    # f.write('------------------------------------------')
    # f.write(datelist[i].get_text()+'\n')
    # f.close()
    print ('----------------------------------------------共获取:%d条新闻' % len(title_list))

gnxw()