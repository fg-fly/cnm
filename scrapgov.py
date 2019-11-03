# coding=utf-8
import traceback

import requests
from bs4 import BeautifulSoup


class GovWebSite(object):
    def __init__(self, INIT_URL, SELECTOR):
        self.INIT_URL = INIT_URL
        self.SELECTOR = SELECTOR


def get_govclass_list():
    gov_url_list = (
        ['http://hdqw.bjhd.gov.cn/qwyw/cwhd/', 'content_selector', 'date_selector', '领导活动'],
        ['http://hdrd.bjhd.gov.cn/xwzx/jdxw/', 'content_selector', 'date_selector', '领导活动'])


def page_request(url):
    try:
        response = requests.get(url)
        result = response.content.decode('utf-8')
        if response.status_code == 200:
            return result

    except requests.RequestException:
        return None


def deal_html(url, start_date):
    try:
        html = page_request(url)
        soup = BeautifulSoup(html, 'lxml')
        result_list = []

    except Exception as e:
        print('Error: ', e)
        traceback.print_exc()
