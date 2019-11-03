# coding=utf-8
import os
import sys
import zipfile

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
        print 'no such directory'
        return None


def request_douban(url,seed):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Connection': 'keep-alive',
        'cookie':'JSESSIONID=1ph9xq7ap0h6s1folqtimvu3q8; SERVERID=6d3fb4dcf986e1025098a4adc0881bbe|1571714415|1571713653',
        'Upgrade-Insecure-Requests': '1',
        'X-Requested-With':'XMLHttpRequest',
        'Referer':'http://10.165.241.107/portal/index.jsp',
        'Host':'10.165.241.107',
        'Origin':'http://10.165.241.107'}
    param = {
        'infoID':seed,
        'number':'7',
        'logon':'false',
        'titleWidth':'30'
    }


    try:
        response = requests.post(url, headers=headers,data=param)
        result = response.content.decode('utf-8')
        if response.status_code == 200:
            return result

    except requests.RequestException:
        print 'cnm'


def exchange_url(url):
    http_target_str = 'http://world.people.com.cn'
    if (http_target_str in url):
        # print (title_list[i].get("href"))
        return url
    else:
        # test = http_target_str + title_list[i].get("href")
        _url = http_target_str + url
        return _url


def bjxw(key,t):
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')

    # url = 'http://10.165.241.107/portal/index.jsp'
    url = 'http://10.165.241.107/portal/tag/doubleList_info.jsp'
    html = request_douban(url,key)
    soup = BeautifulSoup(html, 'lxml')
    title_list = soup.select("a")
    date_list = soup.select("td[width='65']")
    # article_date = soup.select("div.listBox > ul > li > span")
    flag_index = 0
    for i in title_list:
        try:
            zipfilename = i.get('title') + '.zip'
            date = date_list[flag_index].get_text()
            art_url = 'http://10.165.241.107/info/infoFile_dabao.action?id=_' + i.get("href")[-22:]
            print art_url
            art_file = requests.get(art_url, stream=False)
            # if art_file.status_code == 200:
            file_path = '/Users/Tuoxian/PycharmProjects/demo/test/通知公告' + '/' + t + '/' + date
            is_exist = os.path.exists(file_path)
            if not is_exist:
                os.makedirs(file_path)
            os.chdir(file_path)
            with zipfile.ZipFile(zipfilename, 'w') as z:
                z.write(art_file.content)
            print '写入成功-----------' + zipfilename
            flag_index += 1
        except Exception:
            flag_index +=1
            continue


param_list = {'rdfw':'_T22P0CFlEeKgOvWTncRVCQ','qwfw':'_WOqmUCFmEeKgOvWTncRVCQ','qzf':'_iaQrYCFkEeKgOvWTncRVCQ'}
for key in param_list:
    bjxw(param_list[key],key)

