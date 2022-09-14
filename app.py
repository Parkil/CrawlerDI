from typing import List

from di import Container
from di_handler.handler import chk_pre_con, get_htmls, parse_html, get_url_list


def run_crawler():
    Container()

    chk_result: bool = chk_pre_con()
    print('chk_result : ', chk_result)

    url_list: List[str] = get_url_list()
    print(url_list)

    result_dict: dict = get_htmls(url_list)
    print('result_dict : ', result_dict)

    parse_result_dict: dict = parse_html(result_dict)
    print(parse_result_dict)


if __name__ == "__main__":
    run_crawler()
