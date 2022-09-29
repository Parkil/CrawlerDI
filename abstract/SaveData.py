import abc
from typing import List

from abstract.vo import ParseHtmlInfo


class SaveData(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save(self, parse_html_list: List[ParseHtmlInfo]):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'save')
            and
            callable(subclass.save)
        )
