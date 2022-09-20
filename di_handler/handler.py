import logging
from typing import List

from dependency_injector.wiring import Provide, inject

from dependency_interface import ChkPreCon, GetHtml, ParseHtml, GetUrlList, SaveData
from di import Container

logger = logging.getLogger('detail')


@inject
def run_crawler(
        chk_pre_con: ChkPreCon = Provide[Container.chk_pre_con],
        get_url_list: GetUrlList = Provide[Container.get_url_list],
        get_html: GetHtml = Provide[Container.get_html],
        parse_html: ParseHtml = Provide[Container.parse_html],
        save_data: SaveData = Provide[Container.save_data]
) -> None:
    chk_result: bool = chk_pre_con.chk_pre_con()

    if chk_result is False:
        raise Exception('crawler chk result false')

    __url_list: List[str] = get_url_list.get_url_list()
    logger.info('url_list : %s', __url_list)

    __result_dict: dict = get_html.get_htmls(__url_list)
    logger.info('result_dict : %s', __result_dict)

    __parse_result_dict: dict = parse_html.parse_html(__result_dict)
    logger.info('parse_result_dict : %s', __parse_result_dict)

    save_data.save(__parse_result_dict)
