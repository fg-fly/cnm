# coding=utf-8
import os
import sys

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
        print '写入失败'


def request_douban(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Cookie': 'wdcid=4ed8b1b673ccc8ce; PHPSESSID=2e5vsn21rifn8sno7g46k1hq32; wdses=0533268102b96c8a; csrf_cookie_name=c84e70031d465b958598e516ff75c403; wdlast=1567045320',
        'Connection': 'keep-alive'}
    try:
        response = requests.get(url, headers=headers)
        result = response.content.decode('utf-8')
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


def main():
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    l = ['101', '102', '103', '104', '105', '106', '107', '108']
    g = ['1', '2', '3', '4', '5', '6', '7', '8']
    for type_index in l:
        for page_index in g:
            try:
                url = 'http://jhsjk.people.cn/result/' + page_index + '?type=' + type_index
                html = request_douban(url)
                soup = BeautifulSoup(html, 'lxml')
                title_list = soup.select("div.fr > ul > li > a")
                article_date = soup.select("ul.con > li > span.f2")
                dic_title = soup.select("h1")[0].get_text()[:2]

                for i in range(len(title_list)):
                    article_url = 'http://jhsjk.people.cn/' + title_list[i].get("href")
                    try:
                        html1 = request_douban(article_url)
                        result_soup = BeautifulSoup(html1, 'lxml')
                        result_title = result_soup.select("h1")[0].get_text()
                        img_src = result_soup.select("div.d2txt_con > p > img")

                        artcle_content = result_soup.select("div.d2txt_con > p")
                        article_date_str1 = '/' + dic_title + '/'+page_index


                    except BaseException:
                        print 'cnm 页面不存在'

                    try:
                        print '=====================' + type_index
                        if len(img_src) == 0:
                            article_title_str = '/' + str(i) + result_title + '.txt'
                            f = result2file('/习近平重要讲话', article_date_str1, article_title_str)
                            f.write(result_title + '\n')
                            for k in range(len(artcle_content)):
                                f.write('  ' + artcle_content[k].get_text() + '\n')

                            f.close()
                            print '《' + result_title + '》'
                        else:
                            try:
                                article_title_str = '/' +str(i)+result_title + '.txt'
                                article_root_dic = '/习近平重要讲话' + article_date_str1
                                article_date_str1 = '/' + article_title_str
                                f = result2file(article_root_dic, article_date_str1, article_title_str)
                                f.write(result_title + '\n')
                                for k in range(len(artcle_content)):
                                    if len(artcle_content[k].get_text()) < 3 and len(artcle_content[k].get_text()) != 0:
                                        f.write('---------------------------------------- ' + '\n')
                                        f.write('-------------------这里有图片------------ \n' )
                                        f.write('---------------------------------------- ' + '\n')
                                    else:
                                        f.write('  ' + artcle_content[k].get_text() + '\n')

                                f.close()
                                print '《' + result_title + '》'
                                for x in range(len(img_src)):
                                    _img_src = img_src[x].get("src")
                                    img = requests.get(_img_src)
                                    article_title_str_img = '/' + str(x) + '.jpg'
                                    article_date_str1 = '/' + article_title_str + '/图片'
                                    img_file = result2file(article_root_dic, article_date_str1, article_title_str_img)
                                    img_file.write(img.content)
                                    print '图片保存成功'
                                    img_file.close()

                            except Exception:
                                print '保存失败'



                    except IndexError:
                        print 'result_title is None!'

                    # try:
                    #     if len(img_src) > 0:
                    #     parent_dic = '/习近平重要讲话'  + article_date_str1
                    #     img_f = result2file(parent_dic, article_date_str1, article_title_str)
                    #     img_src_href = img_src
                    #     f.write()

                print ('----------------------------------------------共获取:%d条新闻' % len(title_list))
            except Exception:
                print 'index out'


main()
