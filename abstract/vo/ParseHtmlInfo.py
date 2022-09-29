import dataclasses
from typing import Any

from util import JsonUtil


@dataclasses.dataclass
class ParseHtmlInfo:
    __slots__ = ['url', 'parse_data', 'add_info']

    url: str
    parse_data: dict
    add_info: Any

    def json_dict(self) -> dict:
        return {
            'url': self.url,
            'parse_data': self.parse_data,
            'add_info': self.add_info
        }

    def __str__(self):
        return JsonUtil.json_dump(self.json_dict())
