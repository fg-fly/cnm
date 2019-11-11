# coding=utf-8
import os
import traceback

import requests
from bs4 import BeautifulSoup
import xlwt
import sys
import io

# from pathlib2 import Path


def page_request(url):
    try:
        response = requests.get(url)
        result = response.content.decode('utf-8')
        if response.status_code == 200:
            return result
    except requests.RequestException:
        return None


def select_html(url, selector, html):
    try:
        html = page_request(url)
        soup = BeautifulSoup(html, 'lxml')
        resultant = soup.select(selector)
        return resultant
    except Exception as e:
        print('Error: ', e)
        traceback.print_exc()


def result2file(parent_dic, article_date, article_title):
    root_dic = '/Users/plantkon/Documents/WorkSpacePy/hdqw/test'
    target_dic = root_dic + parent_dic + article_date
    is_exists = os.path.exists(target_dic)
    filename = target_dic + article_title
    if not is_exists:
        os.makedirs(target_dic)
    f = open(filename, 'w')
    return f


def ldhd():
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    gov_url_list = (
        ['http://hdqw.bjhd.gov.cn/qwyw/cwhd/', 'ul.secList > li > a', 'ul.secList > li > b', 'div.titleCon > h1',
         'div.TRS_Editor > p', '领导活动'],
        ['http://hdrd.bjhd.gov.cn/xwzx/jdxw/', 'ul.txtList > li > a', 'ul.txtList > li > span', 'h1',
         'div.TRS_Editor > p', '领导活动'],
        ['http://zyk.bjhd.gov.cn/zwdt/hdyw/', 'ul.slideList > li > a', 'ul.slideList > li > span', 'h1',
         'div.Custom_UnionStyle > p', '领导活动'],

    )
    for i in range(len(gov_url_list)):
        url = gov_url_list[i][0]
        print url
        content_selector = gov_url_list[i][1]
        article_date_selector = gov_url_list[i][2]
        content_date_selector = gov_url_list[i][2]
        article_title_selector = gov_url_list[i][3]
        article_content_selector = gov_url_list[i][4]
        html = page_request(url)
        title_list = select_html(url, content_selector, html)
        date_list = select_html(url, content_date_selector, html)
        for j in range(len(title_list)):
            article_url = url + title_list[j].get("href")
            print article_url
            article_html = page_request(article_url)
            article_content_list = select_html(article_url, article_content_selector, article_html)
            article_title_list = select_html(article_url, article_title_selector, article_html)
            article_date_list_str = date_list[j].get_text()
            result_parent_dic = '/' + article_date_list_str
            result_file_name = '/' + article_title_list[0].get_text() + '.txt'
            target_dic = '/' + gov_url_list[i][5]
            result_file = result2file(target_dic, result_parent_dic, result_file_name)
            result_file.write(article_title_list[0].get_text())
            for k in range(len(article_content_list)):
                p_content_text = article_content_list[k].get_text().strip()
                if len(p_content_text) < 5:
                    continue
                else:
                    result_file.write(
                        "<div><span style='font-size:16px;margin-top:15px;line-height:25px;text-indent:30px;display:block'> " +
                        p_content_text + "</span></div>")
                    result_file.write("<div>&nbsp;</div>")

            result_file.close()


ldhd()
