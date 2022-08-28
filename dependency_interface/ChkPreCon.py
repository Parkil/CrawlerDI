import abc
from typing import Any


class ChkPreCon(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def chk_pre_con(self) -> bool:
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'chk_pre_con')
            and
            callable(subclass.chk_pre_con)
        )
