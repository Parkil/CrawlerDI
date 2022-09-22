import abc
from typing import List


class GetHtml(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_html(self, url: str) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def get_htmls(self, url_list: List[str]) -> dict:
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
