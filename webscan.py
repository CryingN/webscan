#!/bin/python
#by:CryingN
#这里是一个简单的网页扫描工具,通过urllib库与requests库进行扫描探测

import urllib.request as ur
import time
import os
import requests as rs
#url = "http://10.0.2.15:5555"

number = "v0.0.1"
logo = """\033[31m=========================================
               |
  \ \  \ / -_)  _ \(_-<  _|  _` |   \\
   \_/\_/\___|_.__/___/\__|\__,_|_| _|
地  址:https://github.com/CryingN/webscan
版本号:{numbers}
邮  箱:CryingNights7v@gmail.com
==========================================\033[0m
""".format(numbers=number)

proxy_list = [
    {'http':'58.211.134.98:38480'},
    {'http':'171.35.163.230:9999'}
]
true = "\033[32m[True]\033[0m "
false = "\033[31m[False]\033[0m "
warn = "\033[33m[Warn]\033[0m "
choose_ = "\033[34m[Choose]\033[0m "
all_print = True
proxy_handler = ur.ProxyHandler(proxy_list[1])
opener = ur.build_opener(proxy_handler)

def url_bool(url):
    lists = os.listdir("data")
    print(lists)
    the_list = input("选择检测字典:")
    dictionary = open("data/{the_list}".format(the_list=the_list),"r")
    for dic in dictionary:
        get_url = url + "/" + dic
        try:
            data = ur.urlopen(get_url)
            type_data = rs.get(get_url)
            print(type_data.text)
            if data.read() == b'' and all_print:
                print(false+get_url+" (\033[31mx\033[0m)")
            else:
                print(true+get_url+" (\033[32mo\033[0m)" )
        except:
            print(false+get_url+" (\033[31mx\033[0m)")
        time.sleep(10)
print(logo)
url = input("输入url:")
url_bool(url)
