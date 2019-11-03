# coding=utf-8
import os
import sys

import logging

import requests

logging.basicConfig()


class TextBeen:

    def __init__(self, v1, v2, v3, v4, v5):
        self.userName = v1
        self.realName = v2
        self.password = v3
        self.roleName = v3
        self.devFlag = v5

        pass

    def get_been(self):
        return {'userName': self.userName.replace('\n', ''),'devFlag':self.devFlag.replace('\n', '')}


def readtext(dic):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # loger.info('1')
    list = ['']
    if os.path.exists(dic):
        with open(dic) as f:
            while True:
                line = f.readline()
                list.append(line)
                if not line:
                    break
        # for te in range(len(list)):
        # print list[te]

        if len(list) > 0:
            # print '读取完了'
            textbeen = TextBeen(list[1], list[2], list[3], list[4], list[5])
            return textbeen.get_been()
    else:
        print '该文件夹不存在'


# loger = logging.getLogger('readtext')
def request_douban(url, datas):
    print datas
    datas1 = {'userName': '小爬虫', 'devFlag': '0'}
    print type(datas)

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': 'i18n_browser_Lang=zh-cn; JEECGINDEXSTYLE=hplus; JSESSIONID=E8970F5EF61C7EB53BAAD89709568A27; Hm_lvt_098e6e84ab585bf0c2e6853604192b8b=1567391196; Hm_lpvt_098e6e84ab585bf0c2e6853604192b8b=1567672118; ZINDEXNUMBER=2000',
        'Upgrade-Insecure-Requests': '1'}

    try:
        response = requests.post(url, data=datas
                                 , headers=headers)
        result = response.content.decode('utf-8')
        if response.status_code == 200:
            return result

    except requests.RequestException:
        print 'cnm'


data = readtext('/Users/Tuoxian/PycharmProjects/demo/test/testdata.txt')
html = request_douban('http://localhost:8080/jeecg_war/userController.do?saveUser', data)
print html
