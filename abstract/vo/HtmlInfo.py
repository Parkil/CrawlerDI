import dataclasses
from typing import Any

from util import JsonUtil


@dataclasses.dataclass
class HtmlInfo:
    __slots__ = ['url', 'html_con', 'add_info']

    url: str
    html_con: str
    add_info: Any

    def json_dict(self) -> dict:
        return {
            'url': self.url,
            'html_con': self.html_con,
            'add_info': self.add_info
        }

    def __str__(self):
        return JsonUtil.json_dump(self.json_dict())
