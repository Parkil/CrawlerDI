import logging
from typing import List

from impl.util import ParseHtmlUtil, JsonUtil
from impl.vo import NovelSubject
from abstract import ParseHtml


class ParseHtmlImpl(ParseHtml):

    logger = logging.getLogger('detail')

    def __init__(self):
        self.logger.info('ParseHtmlImpl init')

    def __parse_single_data(self, html_con: str) -> str:
        ret_list: List[NovelSubject] = ParseHtmlUtil.get_all_links(html_con)
        return JsonUtil.json_dump(ret_list)

    def parse_html(self, get_html_result: dict) -> dict:
        __ret_list: list = list()

        for url, html_con in get_html_result.items():
            __parse_json: str = self.__parse_single_data(html_con)
            __ret_list.append((url, __parse_json))

        return dict(__ret_list)