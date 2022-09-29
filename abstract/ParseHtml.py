import abc
from typing import List

from abstract.vo import HtmlInfo, ParseHtmlInfo


class ParseHtml(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def parse_html(self, html_info: HtmlInfo) -> List[ParseHtmlInfo]:
        raise NotImplementedError

    @abc.abstractmethod
    def parse_htmls(self, html_info_list: List[HtmlInfo]) -> List[ParseHtmlInfo]:
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'parse_html')
            and
            callable(subclass.parse_html)
            and
            hasattr(subclass, 'parse_htmls')
            and
            callable(subclass.parse_htmls)
        )
