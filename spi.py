# coding=utf-8

import requests, re
import os
from bs4 import BeautifulSoup

url = 'https://mm.taobao.com/self/aiShow.htm?spm=719.7763510.1998643336.1.9zAfIW&userId=56540137'
login_url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F'

session = requests.session()
session.post(login_url, {'username': '###', 'password': '###'})
s = session.get(url)
html = BeautifulSoup(s.text)

urls = html.find_all(name="img", attrs={"style": re.compile(r'float: none;.？*')})
for url in urls:
    url = 'http:' + url['src']
    print(url)
# print(s.text)
