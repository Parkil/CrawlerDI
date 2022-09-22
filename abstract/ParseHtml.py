import abc


class ParseHtml(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def parse_html(self, get_html_result: dict):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'parse_html')
            and
            callable(subclass.parse_html)
        )
