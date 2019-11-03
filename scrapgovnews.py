# coding=utf-8
import os
import traceback

import requests
from bs4 import BeautifulSoup
import xlwt
import sys
import io

from pathlib2 import Path


def page_request(url):
    try:
        response = requests.get(url)
        result = response.content.decode('utf-8')
        if response.status_code == 200:
            return result
    except requests.RequestException:
        return None


def select_html(selector, html):
    #try:
        soup = BeautifulSoup(html, 'lxml')
        resultant = soup.select(selector)
        return resultant
    #except Exception as e:
        #print('Error: ', e)
        #traceback.print_exc()


def result2file(parent_dic, article_date, article_title):
    root_dic = '/Users/Tuoxian/PycharmProjects/demo/test'
    target_dic = root_dic + parent_dic + article_date
    is_exists = os.path.exists(target_dic)
    filename = target_dic + article_title
    if not is_exists:
        os.makedirs(target_dic)
    f = open(filename, 'w')
    return f


def main():
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    url = 'http://www.gov.cn/xinwen/index.htm'
    html_title_selector = 'h4'
    #html_date_selector = 'div.zl_channel_body zl_channel_bodyxw > dl > dd > h4 > span'
    # for i in range(len(gov_url_list)):
    #     url = gov_url_list[i][0]
    #     print url
    #     content_selector = gov_url_list[i][1]
    #     article_date_selector = gov_url_list[i][2]
    #     content_date_selector = gov_url_list[i][2]
    #     article_title_selector = gov_url_list[i][3]
    #     article_content_selector = gov_url_list[i][4]
    html = page_request(url)
    title_list = select_html(html, html_title_selector)
    #date_list = select_html(html, html_date_selector)

    for j in range(len(title_list)):
        article_url = title_list[j].get("href")
        print article_url
        # article_html = page_request(article_url)
        # article_content_list = select_html(article_url, article_content_selector, article_html)
        # article_title_list = select_html(article_url, article_title_selector, article_html)
        # article_date_list = select_html(article_url, article_date_selector, article_html)
        # if len(article_date_list[0].get_text()) > 11:
        #     article_date_list_str = article_date_list[0].get_text()[-11:]
        #     print '------------------large'
        #     print article_date_list_str
        # else:
        #     article_date_list_str = article_date_list[0].get_text()
        #     print '------------------less'
        #     print article_date_list_str
        # article_date_list_str = date_list[j].get_text()
        # result_parent_dic = '/' + article_date_list_str
        #
        # result_file_name = '/' + article_title_list[0].get_text() + '.txt'
        #
        # target_dic = '/' + gov_url_list[i][5]
        # result_file = result2file(target_dic, result_parent_dic, result_file_name)
        #
        # for k in range(len(article_content_list)):
        #     result_file.write(article_content_list[k].get_text())
        #
        # result_file.close()


main()

