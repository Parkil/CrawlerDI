import abc
from typing import List


class GetUrlList(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_url_list(self) -> List[str]:
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'get_url_list')
            and
            callable(subclass.get_url_list)
        )
