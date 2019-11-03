# coding=utf-8
import os
import sys
import zipfile

import requests
from bs4 import BeautifulSoup
import datetime
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


def request_douban(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Connection': 'keep-alive',
        'cookie':'wdcid=302592f5b27e15aa; wdlast=1571706481',
        'Upgrade-Insecure-Requests': '1'}

    try:
        response = requests.get(url, headers=headers)
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

def zipDir(dirpath,outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')

        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()
def compress_file(zipfilename, dirname):      # zipfilename是压缩包名字，dirname是要打包的目录
    os.chdir('/Users/Tuoxian/PycharmProjects/demo/test/报刊/人民日报')

    if os.path.isfile(dirname):
        with zipfile.ZipFile(zipfilename, 'w') as z:
            z.write(dirname)
    else:
        with zipfile.ZipFile(zipfilename, 'w') as z:
            for root, dirs, files in os.walk(dirname):
                for single_file in files:
                    if single_file != zipfilename:
                        filepath = os.path.join(root, single_file)
                        z.write(filepath)

def bjrb():
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    print '执行北京新闻--------'
    month = str(datetime.datetime.now().month)
    day = '0'+ str(datetime.datetime.now().day)

    # month = str(10)
    # day = str(30)
    # url = 'http://paper.people.com.cn/rmrb/html/2019-'+month+'/'+day+'/nbs.D110000renmrb_01.htm'
    url = 'http://bjrb.bjd.com.cn/html/2019-'+month+'/'+ day+'/node_108.htm'
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    title_list = soup.select("li[class='3'] > a")

    # # os.makedirs('/Users/Tuoxian/PycharmProjects/demo/test/报刊/人民日报')
    os.chdir('/Users/Tuoxian/PycharmProjects/demo/test/报刊/北京日报')
    index_content = 1
    for i in title_list:
        _url = 'http://bjrb.bjd.com.cn/html/2019-'+month+'/'+day+'/'
        _real_url = _url + i.get("href")
        print i.get("href")
        pdf_html = request_douban(_real_url)
        pdf_soup = BeautifulSoup(pdf_html,'lxml')
        pdf_src = pdf_soup.select("a[href$='.pdf']")[0].get("href")[-28:]
        _real_pdf_src = 'http://bjrb.bjd.com.cn' + pdf_src
        bjxw_pdf = requests.get(_real_pdf_src)
        content = bjxw_pdf.content
        file_name = '北京日报' + str(index_content) + '.pdf'
        with open(file_name, 'wb') as f:
            f.write(content)
        index_content += 1



    compress_file('北京日报.zip', '/Users/Tuoxian/PycharmProjects/demo/test/报刊/北京日报')      # 执行函数

bjrb()