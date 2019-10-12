#coding=utf-8
import time
import aiohttp
import asyncio
import shutil

dldir = "C:\\Users\\zz\\Desktop\\2019-mg\\pic\\"
header = {'api_uid': '13073127','api_utoken': 'A22D4DD4A088AB2A860B6165B2D0F16D20190911101435','app_name': 'BabyFamily',\
    'debug': 'false','os_name': 'iOS','os_version': '12.400000'}

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def parser(html):
    print("parser--------------")

async def download(url):
    async with aiohttp.ClientSession(headers=header) as session:
        print("download start----"+url)
        html = await fetch(session, url)
        print("fetch   download  middle----"+url)
        await parser(html)
        print("download  end----"+url)

# 全部网页
urls = ['https://fzbd.faxuan.net/fzss/service/lawyersService!doGetLawyerList.do?recommend=2&page=%d&pageSize=1&fieldId='%i for i in range(1,10)]

# time
print('#' * 50)
t1 = time.time() 

# init
# shutil.rmtree(dldir)
print("*"*10+"start"+"*"*10)
# 异步IO处理
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(download(url)) for url in urls]
tasks = asyncio.gather(*tasks)
loop.run_until_complete(tasks)

t2 = time.time() # 结束时间
print('总共耗时：%s' % (t2 - t1))
print('#' * 50)