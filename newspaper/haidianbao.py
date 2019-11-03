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
        'Cookie': 'wdcid=215de2c42a245c93; Hm_lvt_634d72f7004dc0d4fb6aff00de988bf1=1571022745; Hm_lpvt_634d72f7004dc0d4fb6aff00de988bf1=1571022745; wdlast=1571022747; wdses=277c693c3d910dc4',
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

def hdb():
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    print '执行海淀报'
    month = str(datetime.datetime.now().month)
    day = '0' + str(datetime.datetime.now().day)
    # month = str(10)
    # day = str(30)
    # url = 'http://paper.people.com.cn/rmrb/html/2019-'+month+'/'+day+'/nbs.D110000renmrb_01.htm'
    url = 'http://www.haidian001.com:88/hdb/html/2019-'+month+'/'+day+'/node_49.htm'
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    title_list = soup.select("a[href$='.pdf']")
    # os.makedirs('/Users/Tuoxian/PycharmProjects/demo/test/报刊/人民日报')
    os.chdir('/Users/Tuoxian/PycharmProjects/demo/test/报刊/海淀报')
    index_content = 1
    for i in title_list:
        print 1
        _url = 'http://www.haidian001.com:88/hdb'
        _real_url = _url + i.get("href")[-39:]
        print _real_url
        rmrb_pdf = requests.get(_real_url)
        content = rmrb_pdf.content
        file_name = '海淀报' + str(index_content) + '.pdf'
        with open(file_name, 'wb') as f:
            f.write(content)
        index_content += 1

    # article_date = soup.select("div.listBox > ul > li > span")
    # print title_list[0].get_text()
    #
    # for i in range(len(title_list)):
    #     article_url = title_list[i].get("href")
    #     try:
    #         html1 = request_douban(article_url)
    #         result_soup = BeautifulSoup(html1, 'lxml')
    #         # result_title = result_soup.select("div.header > h1")
    #         result_title = title_list[i].get_text()
    #         artcle_content = result_soup.select("div.TRS_Editor > p")
    #         article_date_str = article_date[i].get_text()[5:]
    #         _article_date_str = article_date_str.replace('-', '月') + '日'
    #         article_date_str1 = '/' + _article_date_str
    #     except BaseException:
    #         continue
    #         print 'cnm 页面不存在'
    #
    #     try:
    #         r2 = result_title
    #         article_title_str = '/' + r2 + '.txt'
    #         f = result2file('/网络聚焦/北京新闻', article_date_str1, article_title_str)
    #         if f is None:
    #             continue
    #         f.write(r2 + '\n')
    #         for k in range(len(artcle_content)):
    #             f.write("<div><span style='font-size:16px;margin-top:15px;line-height:25px;text-indent:30px'> " +
    #                     artcle_content[k].get_text() + "</span></div>")
    #             f.write("<div>&nbsp;</div>")
    #
    #
    #         f.close()
    #         print '《' + r2 + '》' + article_date[i].get_text()[5:].replace('-', '月') + '日'
    #
    #     except IndexError:
    #         print 'result_title is None!'
    # print ('----------------------------------------------共获取:%d条新闻' % len(title_list))
hdb()

compress_file('海淀报.zip', '/Users/Tuoxian/PycharmProjects/demo/test/报刊/海淀报')      # 执行函数

