# coding=utf-8
import os
import sys

import requests
from bs4 import BeautifulSoup
import xlwt
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
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': 'security_session_verify=41a3cc10d286a279c1b5f9c845d5bc70; banggoo.nuva.cookie=0|XWzcT|XWzcS; yfx_c_g_u_id_10006654=_ck19090217025316057428597430432; yfx_f_l_v_t_10006654=f_t_1567414973592__r_t_1567414973592__v_t_1567414973592__r_c_0',
        'Upgrade-Insecure-Requests': '1'}
    try:
        response = requests.get(url,headers=headers)
        result = response.content.decode('utf-8')
        if response.status_code == 200:
            return result

    except requests.RequestException:
        return 'cnm'


def exchange_url(url):
    http_target_str = 'http://www.nhc.gov.cn'
    _url = http_target_str + url
    return _url


def jkxw():
    try:
        reload(sys)  # reload 才能调用 setdefaultencoding 方法
        sys.setdefaultencoding('utf-8')
        url = 'http://www.nhc.gov.cn/wjw/xwdt/list.shtml'
        html = request_douban(url)
        soup = BeautifulSoup(html, 'lxml')
        title_list = soup.select("ul.zxxx_list > li > a")
        article_date = soup.select("ul.zxxx_list > li > span")
    except Exception:
        return 0

    for i in range(len(title_list)):
        article_url = 'http://www.nhc.gov.cn' + title_list[i].get("href")
        try:
            html1 = request_douban(article_url)
            result_soup = BeautifulSoup(html1, 'lxml')
            result_title = result_soup.select("title")
            artcle_content = result_soup.select("div.con > p")
            article_date_str = article_date[i].get_text()[5:]
            _article_date_str = article_date_str.replace('-', '月') + '日'
            article_date_str1 = '/' + _article_date_str
        except BaseException:
            continue

        try:
            r2 = result_title[0].get_text()
            print r2
            article_title_str = '/' + r2 + '.txt'
            f = result2file('/网络聚焦/健康新闻', article_date_str1, article_title_str)
            f.write(r2 + '\n')
            for k in range(len(artcle_content)):
                f.write("<div><span style='font-size:16px;margin-top:15px;line-height:25px;text-indent:30px;display:block'> " + artcle_content[k].get_text() + "</span></div>")
                f.write("<div>&nbsp;</div>")

            f.close()
            print '《' + r2 + '》' + article_date_str.replace('/', '')
        except IndexError:
            print 'result_title is None!'

    print ('----------------------------------------------共获取:%d条新闻' % len(title_list))

jkxw()

