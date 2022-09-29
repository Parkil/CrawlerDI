import abc
from typing import List

from abstract.vo import HtmlInfo


class GetHtml(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_html(self, url: str) -> HtmlInfo:
        raise NotImplementedError

    @abc.abstractmethod
    def get_htmls(self, url_list: List[str]) -> List[HtmlInfo]:
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'get_html')
            and
            callable(subclass.get_html)
            and
            hasattr(subclass, 'get_htmls')
            and
            callable(subclass.get_htmls)
        )
