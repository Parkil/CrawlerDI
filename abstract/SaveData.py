import abc


class SaveData(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save(self, parse_html_result: dict):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'save')
            and
            callable(subclass.save)
        )
