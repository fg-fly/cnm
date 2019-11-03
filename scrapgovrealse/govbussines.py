# coding=utf-8
import os
import sys

import requests
from bs4 import BeautifulSoup
import beijingxinwen
from caijingdongtai import cjdt
from guojixinwen import gjxw
from guoneixinwei import gnxw
from jiankangxinwen import jkxw
from realsescrapgov import ldhd

beijingxinwen.bjxw()
cjdt()
gjxw()
gnxw()
jkxw()
ldhd()