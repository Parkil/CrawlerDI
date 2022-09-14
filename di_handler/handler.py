from typing import List

from dependency_injector.wiring import Provide, inject

from dependency_interface import ChkPreCon, GetHtml, ParseHtml, GetUrlList
from di import Container


@inject
def chk_pre_con(
        chk_pre_con_di: ChkPreCon = Provide[Container.chk_pre_con],
) -> bool:
    return chk_pre_con_di.chk_pre_con()


@inject
def get_url_list(
        get_url_list_di: GetUrlList = Provide[Container.get_url_list],
) -> List[str]:
    return get_url_list_di.get_url_list()


@inject
def get_html(
        url: str,
        get_html_di: GetHtml = Provide[Container.get_html]
) -> dict:
    return get_html_di.get_html(url)


@inject
def get_htmls(
        url_list: List[str],
        get_html_di: GetHtml = Provide[Container.get_html]
) -> dict:
    return get_html_di.get_htmls(url_list)


@inject
def parse_html(
        html_dict: dict,
        parse_html_di: ParseHtml = Provide[Container.parse_html]
) -> dict:
    return parse_html_di.parse_html(html_dict)
