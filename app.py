import logging
from typing import List

from config.log import config_logging
from di import Container
from di_handler.handler import chk_pre_con, get_htmls, parse_html, get_url_list, save_data

config_logging()

logger = logging.getLogger('detail')


def run_crawler():
    Container()

    chk_result: bool = chk_pre_con()
    logger.info('chk_result : %s', chk_result)

    url_list: List[str] = get_url_list()
    logger.info('url_list : %s', url_list)

    result_dict: dict = get_htmls(url_list)
    logger.info('result_dict : %s', result_dict)

    parse_result_dict: dict = parse_html(result_dict)
    logger.info('parse_result_dict : %s', parse_result_dict)

    save_data(parse_result_dict)


if __name__ == "__main__":
    run_crawler()

