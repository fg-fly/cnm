# coding=utf-8
import sys
import requests
import os

def test():
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    url = 'http://imgsrc.baidu.com/forum/w%3D580%3B/sign=749ed018cecec3fd8b3ea77de6b3d63f/83025aafa40f4bfb3661b3800e4f78f0f63618b4.jpg'
    root_path = '/Users/Tuoxian/PycharmProjects/demo/test/picture/zhaoliying'

    # 利用split()函数获取url最后的文件名
    img_name = url.split('/')[-1]

    img_path = root_path + r'\{0}'.format(img_name)

    try:
        if not os.path.exists(root_path):
            os.makedirs(root_path)

        if not os.path.exists(img_path):

            r = requests.get(url)

            with open(img_path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("执行出错")


test()