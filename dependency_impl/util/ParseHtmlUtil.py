from typing import List

import bs4
from bs4 import BeautifulSoup

from dependency_impl.vo import NovelSubject


class ParseHtmlUtil:

    @staticmethod
    def get_all_links(html_con: str) -> List[NovelSubject]:
        __soup_obj: BeautifulSoup = BeautifulSoup(html_con, 'html5lib', from_encoding='UTF-8')

        __url_list: list = list()
        if __soup_obj is not None:
            """
                a link html
                <a href="https://novel.munpia.com/312393"
                class="title col-xs-6"
                title="미친 용사가 세상을 불태울 뿐인 이야기">미친 용사가 세상을 불태울 뿐인 이야기</a> 
            """
            __a_link_list = __soup_obj.find_all('a', 'title col-xs-6')
            __url_list = list(map(lambda a_link: ParseHtmlUtil.__create_novel_subject(a_link), __a_link_list))

        return __url_list

    @staticmethod
    def __create_novel_subject(a_link: bs4.element.Tag) -> NovelSubject:
        __subject_str = a_link.get_text().replace("\n", "").replace("\r", "")
        __url = a_link.get('href')

        return NovelSubject(__subject_str, __url)
