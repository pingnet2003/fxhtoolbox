# -*- coding: utf-8 -*-
# Time: 2020/05/08
#Author: Xiaohong
# 运行环境: OS: Windows 7
#  Python: 3.7
# 功能: 根据关键词 key 到baidu 下载 pic_number 张的图片
# https://www.jianshu.com/p/33bee611fa7d
# https://www.cnblogs.com/SeekHit/p/6284974.html

import json
import itertools
import urllib
import requests
import os
import re
import sys
import time

# 设立函数，来取得当前时间，作为文件名的一部分，以免文件名重复


def get_sysdate():
    now = time.strftime("%m%d-%H%M%S", time.localtime(time.time()))
    print(now)
    return now


str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}

char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}

# str 的translate方法需要用单个字符的十进制unicode编码作为key
# value 中的数字会被当成十进制unicode编码转换成字符
# 也可以直接用字符串作为value
char_table = {ord(key): ord(value) for key, value in char_table.items()}

# 解码图片URL


def decode(url):
    # 先替换字符串
    for key, value in str_table.items():
        url = url.replace(key, value)
    # 再替换剩下的字符
    return url.translate(char_table)

# 生成网址列表


def buildUrls(word):
    word = urllib.parse.quote(word)  # 屏蔽特殊的字符、比如如果url里面的空格！url里面是不允许出现空格的
    url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
    urls = (url.format(word=word, pn=x)
            for x in itertools.count(start=0, step=60))  # itertools是python内置的模块,count是生成无界限序列，从0开始，步长为60，无限循环
    return urls


# 解析JSON获取图片URL,
# 一个图片对应许多链接，经测试图片链接在 objURL 这个标签内。用正则找出
# 括号表示分组，将括号的内容捕获到分组当中
#  这个括号也就可以匹配网页中图片的url了
re_url = re.compile(r'"objURL":"(.*?)"')  # 根据包含正则表达式的字符串创建模式对象


def resolveImgUrl(html):
    imgUrls = [decode(x) for x in re_url.findall(html)]
    # print(imgUrls)
    return imgUrls
    # for x in re_url.findall(html):
    #     print('aaa:')
    #     print(x)
    #     imgUrls=decode(x)
    #     print('bbb:')
    #     print(imgUrls)
    # return imgUrls


def downImg(imgUrl, dirpath, imgName):
    filename = os.path.join(dirpath, imgName)
    try:
        res = requests.get(imgUrl, timeout=15)
        if str(res.status_code)[0] == "4":
            #    print(str(res.status_code), ":", imgUrl)
            return False
    except Exception as e:
        print("抛出异常：", imgUrl)
        print(e)
        return False
    with open(filename, "wb") as f:
        f.write(res.content)
    return True


def mkDir(dirName):
    dirpath = os.path.join(sys.path[0], dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath


def Tl_baidu_DownPic02(keyword, download_dir, pic_number):
    word = keyword

    dir2 = os.path.join(download_dir, word, get_sysdate())
    print(dir2)
    if not os.path.exists(dir2):
        os.makedirs(dir2)

#    dirpath = mkDir("results")
    dirpath = dir2

    urls = buildUrls(word)
    index = 0
    for url in urls:
        #    print("正在请求：", url)
        html = requests.get(url, timeout=10).content.decode(
            'utf-8')  # 变量html 保留了一份Json文件,其中 objURL 是 图片对应在网址
        #    print("正在请求：", html)
        imgUrls = resolveImgUrl(html)
        if len(imgUrls) == 0 or index >= pic_number:  # 没有图片则结束
            break
        for url in imgUrls:
            if downImg(url, dirpath, str(index) + ".jpg"):
                index += 1
                print("已下载 %s 张" % index)
                if index >= pic_number:
                    break


if __name__ == '__main__':
    #    print("欢迎使用百度图片下载脚本！\n目前仅支持单个关键词。")
    #    print("下载结果保存在脚本目录下的results文件夹中。")
    #    print("=" * 50)
    #    word = input("请输入你要下载的图片关键词：\n")
    Tl_baidu_DownPic02('Raspberry', 'e://', 50)


def call_DownPic02_main(keyword, download_dir, pic_number):
    #    print("欢迎使用百度图片下载脚本！\n目前仅支持单个关键词。")
    #    print("下载结果保存在脚本目录下的results文件夹中。")
    #    print("=" * 50)
    #    word = input("请输入你要下载的图片关键词：\n")
    # Tl_baidu_DownPic02('Raspberry',50)
    Tl_baidu_DownPic02(keyword, download_dir, pic_number)
