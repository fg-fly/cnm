#coding=utf-8
import datetime

import os
import sys
import zipfile

print datetime.datetime.now().month
print datetime.datetime.now().day

def zipDir(dirpath,outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')
        print filenames

        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()

# zipDir('/Users/Tuoxian/PycharmProjects/demo/test/报刊/人民日报','yasuo.zip')

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

compress_file('a.zip', '/Users/Tuoxian/PycharmProjects/demo/test/报刊/人民日报')      # 执行函数