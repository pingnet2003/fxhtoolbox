#Time: 2020/05/08
#Author: Xiaohong
#运行环境: OS: Windows 7
#  Python: 3.7
#功能: 根据关键词 key 到baidu 下载 pic_number 张的图片
#参考页面 https://blog.csdn.net/qq_42554007/article/details/105948099
#2020/05/10: 本程序暂时没有在 本工具夹 中 被调用 

import os
import requests
import re
import time

#设立函数，来取得当前时间，作为文件名的一部分，以免文件名重复
def get_sysdate():
    now = time.strftime("%m%d-%H%M%S", time.localtime(time.time()))
    print(now)
    return now

def tl_baidu_downpic01(keyWord,dir1,pic_number):
    # keyWord  为 设置爬取图片的 关键字
    number = pic_number       # 爬取图片数量
    dir2=os.path.join(dir1,keyWord,get_sysdate())
    print(dir2)
    if not os.path.exists(dir2):
        os.makedirs(dir2)
    url = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq' \
        r'=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd' \
        r'=1497491098685%5E00_1519X735&word=' + keyWord
    get = requests.get(url)
    pciture_url = re.findall(r'objURL":"(.*?)",', get.text)
    a = 0        
    for i in pciture_url:
        p_type = i.split('.')[-1]
        a += 1
        try:
            picture = requests.get(i, timeout=10)                
            name = "%s/%s_%d.%s" % (dir2,keyWord, a, p_type)                        
            with open(name, 'wb') as f:
                f.write(picture.content)
            print('第%d张图片正在下载' % a)
        except:
            import sys
            print('第%d张图片下载失败！已跳过...' % a)             
            tuple = sys.exc_info()
            errmsg = ' 错误为:' + str(tuple[1])
            print(errmsg)
        if a >= number:
            break

if __name__ == "__main__":
    tl_baidu_downpic01("python",'e:\\xx',10)
