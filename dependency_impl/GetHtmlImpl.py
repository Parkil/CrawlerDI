import asyncio
from typing import List

import aiohttp

from dependency_interface.GetHtml import GetHtml


class GetHtmlImpl(GetHtml):
    __event_loop = None

    def __init__(self):
        self.__event_loop = asyncio.get_event_loop()

    def get_html(self, url: str) -> dict:
        __url_list: list = [url]
        return self.__event_loop.run_until_complete(self.__run_async_io(__url_list))

    def get_htmls(self, url_list: List[str]) -> dict:
        return self.__event_loop.run_until_complete(self.__run_async_io(url_list))

    async def __fetch(self, session: aiohttp.ClientSession, url: str) -> str:
        async with session.get(url) as response:
            return await response.text()

    async def __run_async_io(self, url_list: List[str]) -> dict:
        __temp_list: list = list()
        async with aiohttp.ClientSession() as session:
            for url in url_list:
                html_str: str = await self.__fetch(session, url)
                __temp_list.append((url, html_str))

        return dict(__temp_list)
