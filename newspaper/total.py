#coding=utf-8
import sys
import os

# reload(sys)  # reload 才能调用 setdefaultencoding 方法
# sys.setdefaultencoding('utf-8')
# init_path = '/Users/Tuoxian/PycharmProjects/demo/test/报刊'
# f = unicode(init_path,'utf-8')
# file_test = os.listdir(f)
# for i in file_test:
#     os.path.join(i,init_path)
from newspaper.bjrb import bjrb
from newspaper.haidianbao import hdb
from newspaper.rmrb import rmrb


def del_file(f):

    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    # path = unicode(f,'utf-8')
    path = f
    listdir = os.listdir(path)
    for i in listdir:
        if i != '.DS_Store':
            path_file = os.path.join(path, i)
            if os.path.isfile(path_file):
                print '即将删除--------:' + i
                os.remove(path_file)

            else:
                del_file(path_file)


print 1

del_file('/Users/Tuoxian/PycharmProjects/demo/test/报刊')

