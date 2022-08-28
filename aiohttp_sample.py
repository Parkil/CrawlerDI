from datetime import datetime

import aiohttp
import asyncio

import requests as requests


def async_sample():
    print('start : ', datetime.now())

    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.text()

    async def main() -> list:
        temp_list = list()
        async with aiohttp.ClientSession() as session:
            for idx in range(15):
                html = await fetch(session, 'http://python.org')
                temp_list.append(html[:15])
            """
            print("Status1:", response.status)
            print("Content-type1:", response.headers['content-type'])
    
            html = await response.text()
            print("Body1:", html[:15], "...")
            """
        return temp_list

    loop = asyncio.get_event_loop()
    aaa: list = loop.run_until_complete(main())

    print(aaa)

    for val in aaa:
        print(val+'\n')

    print('end : ', datetime.now())


def sync_sample():
    print('start : ', datetime.now())
    for idx in range(15):
        response = requests.get('http://python.org')
        html = response.text
        print(f"Body:{idx}", html[:15], "...")

    print('end : ', datetime.now())


# async_sample()

persons = [('김기수', 30)]
mydict = dict(persons)
print(len(mydict))
print(mydict.popitem())

# aaa = ['<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>', '<!doctype html>']
# mydict = dict(aaa)
# print(mydict)
