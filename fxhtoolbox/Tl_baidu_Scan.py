import urllib.request
import json
import time
# 程序缺点：
# 1.识别率不高，经常无法识别，导致无法取的 ocr['words_result'] 的值，产生KeyError 错误
# 2.暂没有加入 本地图片的识别


#设立函数，来取得当前时间，作为文件名的一部分，以免文件名重复
def get_sysdate():
    now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
    print(now)
    return now

def Tl_badiu_Scan(website):
    ak='f2wosFQ4weetEEAmzGiFhLDp'
    sk='Yb0Gs7W2Q6UQhO3Aj4r6jESPVEOo5nEo'
#设立返回列表,保存各阶段执行时间点及返回值
    ret_val=[]

    try:
        # baidu 身份验证
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' %(ak,sk)

        request = urllib.request.Request(host)
        #request.add_header('Content-Type','application/x-www-form-urlencoded;charset=UTF-8')
        request.add_header('Content-Type','application/json;charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()

        json_all=json.loads(content)
        access_token=json_all['access_token']

        # baidu 图片识别的固定网址
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s' %access_token
        ret_val.append('1:'+get_sysdate())
        print(ret_val)
        # data = urllib.parse.urlencode({'url':'https://www.python.org/static/img/python-logo.png'}).encode()
        ret_val.append('2:' + get_sysdate())
        data = urllib.parse.urlencode({'url':website}).encode()
        req=urllib.request.Request(url,method='POST')
        ret_val.append('3:' + get_sysdate())
        req.add_header('Content-Type','application/x-www-form-urlencoded')
        ret_val.append('4:' + get_sysdate())
        res= urllib.request.urlopen(req,data).read().decode('utf-8')
        ret_val.append('5:' + get_sysdate())
        ocr = json.loads(res)
        ret_val.append('6:' + get_sysdate())
        for item in ocr['words_result']:
            print(item['words'])
            ret_val.append('7:' + get_sysdate())
            ret_val.append('7: Result is:' + item['words'] )
    except KeyError as ke:
        ret_val.append('X:' + get_sysdate())
        ret_val.append('X: 错误发生:KeyError,请稍后再试' )
    except :
        import sys
        tuple = sys.exc_info()
        errmsg = ' 错误为:' + str(tuple[1])
        ret_val.append('Z:' + get_sysdate())
        ret_val.append('Z: 未知错误发生,请稍后再试:' +errmsg)
    finally:
        return ret_val
        print(ret_val)

if __name__ == "__main__":
    Tl_badiu_Scan('https://www.python.org/static/img/python-logo.png')