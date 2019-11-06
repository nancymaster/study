#!/usr/bin/python
# coding=utf-8

import asyncio
import time

import aiohttp
import requests


# tongbu
def geturl(url):
    response = requests.get(url)

def run():
    # url = 'http://www.t.ifaxuan.com/gwss/fservice/newsService!doRecommonNewsList.do?start=1000&length=1&id=2'
    url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-'
    for i in range(1000):
        if i%100 == 0:
            print(i)
        geturl(url+str(i))

# yibu
url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-'


async def geturls(url,semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.read()

async def geturlsession(url,semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            for i in range(1000):
                async with session.get(url+str(i)) as response:
                    return await response.read()

if __name__ == '__main__':
    t1 = time.time()
    for i in range(1000):
        loop = asyncio.get_event_loop()
        semaphore = asyncio.Semaphore(400) # 限制并发量
        # tasks = [asyncio.ensure_future(geturls(url+str(i),semaphore)) for i in range(1000)]
        # tasks = asyncio.gather(*tasks)
        loop.run_until_complete(geturlsession(url,semaphore))
    t2 = time.time()
    print('#' * 50)
    print('使用Session，总共耗时：%s' % (t2 - t1))
    print('#' * 50)
