#!/usr/bin/python
# coding=utf-8
# Filename: baby.py
'''
    获取当日所有图文内容+饮食图，发送至微信群里
'''
import requests
import time
import os
import shutil
import aiohttp
import asyncio
import aiofiles

#全局参数
url_info = "https://admin.appbaby.net/v4/api/Timeline/GetTimelines?max_public_no=&school_id=&stud_id=&top=10" 
dm_file = "https://qiniu.appbaby.net/"
#https://qiniu.appbaby.net/android-b9a658a042ded11f3be2ce43b840a594.jpg?imageView2/2/w/375/h/375/q/75&v=20190912
nowtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
dldir = "C:\\Users\\zz\\Desktop\\2019-mg\\pic\\"

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
        #return response.text

# baidu token
def gettoken():
    host='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=9AyXVGIuKUq2kQ2ruwYUDzj7&client_secret=Nr8vZI3of8Bv5scWaNxwIRQxqb02i37x'
    hed = {'Content-Type': 'application/json; charset=UTF-8'}
    response = request("POST",host,hed,"{}")
    return response['access_token']

# 解析所需数据
def parase(ret):
    content = ret['content']
    sedtext = []
    sedpic = []
    count = 0
    for i in range(len(content)):
        cttime = content[i]['public_time']
        if nowtime == cttime.split()[0]:
            sedtext.append(cttime.split()[1]+'===='+content[i]['timeline_text'])   #获取文本内容
            for j in range(len(content[i]['files'])):
                sedpic.append(content[i]['files'][j]['file_url'].split('Host]/')[1])  #获取全部图片
        else:
            count += 1
    if(count == len(content)):
        print("今天还未发布任何内容！")
    return sedtext,sedpic

def wtfile(path,content):
    with open(path,'wb') as f:
        f.write(content)
        f.close()

def dlpic(picname):
    path = dldir+picname
    url = dm_file+picname
    try:
        if not os.path.exists(dldir):
            os.mkdir(dldir)
        if not os.path.exists(path):
            r=requests.get(url)
            r.raise_for_status()
            wtfile(path,r.content)
        else:
            print("图片已存在")
    except:
        print("图片获取失败")

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.read()
		
async def download(picname):
    print("*"*5+picname+"*"*5+dm_file+picname+"*"*5+dldir+picname)
    async with aiohttp.ClientSession() as session:
        picontent = await fetch(session, dm_file+picname)
        async with aiofiles.open(dldir+picname, 'wb') as f:
            f.write(picontent)

if __name__ == "__main__":
    #token = gettoken()
    start = time.time()
    shutil.rmtree(dldir)
    os.mkdir(dldir)

    # 构造参数
    hed = {'api_uid': '13073127','api_utoken': '6AD9F26535CD6720962900BD426C1B3B20191018171544','app_name': 'BabyFamily',\
    'debug': 'false','os_name': 'iOS','os_version': '12.400000'}
    ret = request("GET",url_info,hed,"{}")
    assert ret['success'] == True,"error：列表请求失败"
    # 获取数据
    sedtext,sedpic=parase(ret)

    # 异步IO处理
    t1 = time.time()
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(download(picname)) for picname in sedpic]
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)
    
    t2 = time.time()
    print(t2-t1)

    wtfile(dldir+'text.txt',str(sedtext).encode())

    end = time.time()
    print(end-start)