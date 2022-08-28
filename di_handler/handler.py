from typing import List

from dependency_injector.wiring import Provide, inject

from dependency_interface import ChkPreCon, GetHtml
from di import Container


@inject
def chk_pre_con(
        chk_pre_con_di: ChkPreCon = Provide[Container.chk_pre_con],
) -> bool:
    return chk_pre_con_di.chk_pre_con()


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
