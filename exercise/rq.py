#!/usr/bin/python
# coding=utf-8
# Filename: baby.py

import requests

#处理请求
def request(method, url, header=None, data=None, timeout=5):
       # print("url：%s\nheaders：%s\nparams：%s" % (url,header,data))
        try:
            if method == 'GET':
                response = requests.get(url=url, params=data, headers=header, timeout=timeout)
            elif method == 'POST':
                response = requests.post(url=url, data=data, headers=header, timeout=timeout)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
        except Exception as e:
            print('Exception:{}-{}-{}-{}'.format(method,url,header,data))
            print(e)

        return response.json()

if __name__ == "__main__":
    url2="http://47.104.166.137:81/api/Device/Add"
    heads2={"Token":"9136e12993344a148c9f603495f63fa4"}
    d2={'Tel':'15844449933',"DeviceNumber":'199999',"CarNum":'15844449933',"CarType":"1",\
        "G_idcard":"d66f642fd49444789ef3b7524ae0c1b9","G_bx":"80f14976d99d4f1bae1e6b00841e60f6",\
        "G_carNum":"1ea58206fe70402ea1c7cd4ceb786cf2",\
        'G_car':'b2b651d226a040faa177bc9df5538db8%2C741d46634d7a4fadbebf184d13469b91'}
  #  a=request("POST",url2,heads2,d2)
    a=request("POST",url2,heads2,d2)
    print(a)